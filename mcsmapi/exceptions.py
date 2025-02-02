class MCSMError(Exception):
    def __init__(self, status_code, data=None):
        self.status_code = status_code
        self.data = data
        super().__init__(status_code, data)
