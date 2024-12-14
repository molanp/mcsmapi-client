from enum import Enum


class ApiPool(Enum):
    def __str__(self):
        return self.value

    LOGIN = "api/auth/login"
    AUTH = "api/auth"
    OVERVIEW = "api/overview"
    INSTANCE = "api/instance"
    IMAGE = "api/image"
    FILE = "api/file"
    DAEMON = "api/daemon"
    USERS = "api/users"
