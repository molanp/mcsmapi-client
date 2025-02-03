from enum import Enum


class ApiPool(Enum):
    def __str__(self):
        return self.value

    AUTH = "api/auth"
    OVERVIEW = "api/overview"
    INSTANCE = "api/instance"
    PROTECTED_INSTANCE = "api/protected_instance"
    SERVICE = "api/service"
    FILE = "api/files"
    IMAGE = "api/environment"
