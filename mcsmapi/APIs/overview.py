from mcsmapi.pool import ApiPool
from mcsmapi.request import send
from mcsmapi.models.overview import OverviewModel


class Overview:
    def init(self):
        self.raw_data = send("GET", ApiPool.OVERVIEW)
        assert isinstance(self.raw_data, dict)
        return OverviewModel(self.raw_data)
