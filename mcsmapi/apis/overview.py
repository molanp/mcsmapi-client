from mcsmapi.pool import ApiPool
from mcsmapi.request import send
from mcsmapi.models.overview import OverviewModel


class Overview:
    def init(self):
        """
        初始化方法，用于获取API概览信息并构建概览模型。

        本方法通过发送GET请求获取API概览信息，确保返回的数据类型为字典，
        然后使用这些数据来构建一个OverviewModel实例。

        :return: 返回一个OverviewModel实例，该实例使用获取的API概览信息进行初始化。
        """
        result = send("GET", ApiPool.OVERVIEW)
        return OverviewModel(**result)
