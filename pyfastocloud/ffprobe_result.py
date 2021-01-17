class FFprobeResult:
    MAX_DURATION = 24 * 60 * 60 * 1000

    def __init__(self):
        self._payload = {}

    @classmethod
    def make_entry(cls, json: dict):
        cl = cls()
        cl.update_entry(json)
        return cl

    def update_entry(self, json: dict):
        if json is None:
            raise ValueError('Invalid input')

        self._payload = json

    @property
    def streams(self) -> dict:
        return self._payload['streams']

    @property
    def format(self) -> dict:
        return self._payload['format']

    def is_live(self):
        return not 'duration' in self.format

    @property
    def duration(self) -> int:
        if 'duration' in self.format:
            return int(float(self.format['duration']) * 1000)

        return FFprobeResult.MAX_DURATION
