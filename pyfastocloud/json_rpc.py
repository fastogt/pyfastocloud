import json

JSON_RPC_OK_RESULT = 'OK'

_METHOD_FIELD = 'method'
_PARAMS_FIELD = 'params'
_JSON_RPC_FIELD = 'jsonrpc'
_JSON_RPC_VERSION_FIELD = '2.0'
_ID_FIELD = 'id'
_RESULT_FIELD = 'result'
_ERROR_FIELD = 'error'


class JsonRPCErrorCode:
    JSON_RPC_PARSE_ERROR = -32700
    JSON_RPC_INVALID_REQUEST = -32600
    JSON_RPC_METHOD_NOT_FOUND = -32601
    JSON_RPC_INVALID_PARAMS = -32602
    JSON_RPC_INTERNAL_ERROR = -32603
    JSON_RPC_SERVER_ERROR = -32000
    JSON_RPC_NOT_RFC_ERROR = -32001


class Request:
    def __str__(self):
        return str(self.to_dict())

    def __init__(self, command_id, method: str, params: dict):
        self.id = command_id
        self.method = method
        self.params = params

    def is_valid(self):
        return self.method

    def is_notification(self):
        return self.id is None

    def to_dict(self) -> dict:
        if not self.is_notification():
            return {
                _METHOD_FIELD: self.method,
                _PARAMS_FIELD: self.params,
                _JSON_RPC_FIELD: _JSON_RPC_VERSION_FIELD,
                _ID_FIELD: self.id
            }
        return {
            _METHOD_FIELD: self.method,
            _PARAMS_FIELD: self.params,
            _JSON_RPC_FIELD: _JSON_RPC_VERSION_FIELD
        }


class Response:
    def __str__(self):
        return str(self.to_dict())

    def __init__(self, command_id: str, result=None, error=None):
        self.id = command_id
        self.result = result
        self.error = error

    def is_valid(self):
        return self.id is not None

    def is_error(self):
        return self.error is not None

    def is_message(self):
        return self.result is not None

    def to_dict(self) -> dict:
        if self.is_error():
            return {
                _ERROR_FIELD: self.error,
                _JSON_RPC_FIELD: _JSON_RPC_VERSION_FIELD,
                _ID_FIELD: self.id
            }

        if self.is_message():
            return {
                _RESULT_FIELD: self.result,
                _JSON_RPC_FIELD: _JSON_RPC_VERSION_FIELD,
                _ID_FIELD: self.id
            }

        return {}


# rpc functions
def parse_response_or_request(data: str) -> (Request, Response):
    try:
        resp_req = json.loads(data)
    except ValueError:
        return None, None

    if _METHOD_FIELD in resp_req:
        params = None
        if _PARAMS_FIELD in resp_req:
            params = resp_req[_PARAMS_FIELD]

        command_id = None
        if _ID_FIELD in resp_req:
            command_id = resp_req[_ID_FIELD]

        return Request(command_id, resp_req[_METHOD_FIELD], params), None

    if _RESULT_FIELD in resp_req:
        return None, Response(resp_req[_ID_FIELD], resp_req[_RESULT_FIELD], None)

    if _ERROR_FIELD in resp_req:
        return None, Response(resp_req[_ID_FIELD], None, resp_req[_ERROR_FIELD])

    return None, None
