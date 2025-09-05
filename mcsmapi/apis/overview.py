from mcsmapi.pool import ApiPool
from mcsmapi.request import send
from mcsmapi.models.overview import OverviewModel, LogDetail


class Overview:
    @staticmethod
    def overview():
        """
        获取面板基本信息
        """
        result = send("GET", ApiPool.OVERVIEW)
        return OverviewModel(**result)

    @staticmethod
    def logs():
        """
        获取面板操作日志
        """
        result = send("GET", ApiPool.LOG)
        return [LogDetail(**item) for item in result]
