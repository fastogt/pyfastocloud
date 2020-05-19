from pyfastocloud.client import Client, make_utc_timestamp_msec, RequestReturn
from pyfastocloud.client_constants import ClientStatus
from pyfastocloud.client_handler import IClientHandler


class Commands:
    # service
    ACTIVATE_COMMAND = 'activate_request'
    PREPARE_SERVICE_COMMAND = 'prepare_service'
    SYNC_SERVICE_COMMAND = 'sync_service'
    STOP_SERVICE_COMMAND = 'stop_service'
    SERVICE_PING_COMMAND = 'ping_service'
    STATISTIC_SERVICE_COMMAND = 'statistic_service'
    CLIENT_PING_COMMAND = 'ping_client'  # ping from service
    GET_LOG_SERVICE_COMMAND = 'get_log_service'


class Fields:
    TIMESTAMP = 'timestamp'
    LICENSE_KEY = 'license_key'
    PATH = 'path'
    DELAY = 'delay'


class FastoCloudLbClient(Client):
    def __init__(self, host: str, port: int, handler: IClientHandler, socket_mod):
        super(FastoCloudLbClient, self).__init__(None, ClientStatus.INIT, handler, socket_mod)
        self._host = host
        self._port = port

    @property
    def host(self) -> str:
        return self._host

    @property
    def port(self) -> int:
        return self._port

    def connect(self) -> bool:
        if self.is_connected():
            return True

        sock = self.create_tcp_connection(self._host, self._port)
        if not sock:
            return False

        self._socket = sock
        self._set_state(ClientStatus.CONNECTED)
        return True

    def activate(self, command_id: int, license_key: str) -> RequestReturn:
        command_args = {Fields.LICENSE_KEY: license_key}
        return self._send_request(command_id, Commands.ACTIVATE_COMMAND, command_args)

    @Client.is_active_decorator
    def ping(self, command_id: int) -> RequestReturn:
        command_args = {Fields.TIMESTAMP: make_utc_timestamp_msec()}
        return self._send_request(command_id, Commands.SERVICE_PING_COMMAND, command_args)

    @Client.is_active_decorator
    def prepare_service(self, command_id: int) -> RequestReturn:
        command_args = {}
        return self._send_request(command_id, Commands.PREPARE_SERVICE_COMMAND, command_args)

    @Client.is_active_decorator
    def sync_service(self, command_id: int) -> RequestReturn:
        command_args = {}
        return self._send_request(command_id, Commands.SYNC_SERVICE_COMMAND, command_args)

    @Client.is_active_decorator
    def stop_service(self, command_id: int, delay: int) -> RequestReturn:
        command_args = {Fields.DELAY: delay}
        return self._send_request(command_id, Commands.STOP_SERVICE_COMMAND, command_args)

    @Client.is_active_decorator
    def get_log_service(self, command_id: int, path: str) -> RequestReturn:
        command_args = {Fields.PATH: path}
        return self._send_request(command_id, Commands.GET_LOG_SERVICE_COMMAND, command_args)

    def process_commands(self, data: bytes):
        if not data:
            return

        req, resp = self._decode_response_or_request(data)
        if req:
            if req.method == Commands.CLIENT_PING_COMMAND:
                self.__pong(req.id)

            if self._handler:
                self._handler.process_request(self, req)
        elif resp:
            saved_req = self._request_queue.pop(resp.id, None)
            if saved_req and saved_req.method == Commands.ACTIVATE_COMMAND and resp.is_message():
                self._set_state(ClientStatus.ACTIVE)
            elif saved_req and saved_req.method == Commands.STOP_SERVICE_COMMAND and resp.is_message():
                self._reset()

            if self._handler:
                self._handler.process_response(self, saved_req, resp)

    # private
    @Client.is_active_decorator
    def __pong(self, command_id: str):
        ts = make_utc_timestamp_msec()
        self._send_response(command_id, {Fields.TIMESTAMP: ts})
