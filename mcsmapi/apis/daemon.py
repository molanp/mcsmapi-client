from typing import Any
from mcsmapi.pool import ApiPool
from mcsmapi.request import send
from mcsmapi.models.daemon import DaemonConfig, DaemonModel


class Daemon:
    @staticmethod
    def show() -> list[DaemonConfig]:
        """
        获取全部节点配置信息

        :returns: 节点的配置信息列表
        """
        daemons = send(
            "GET",
            f"{ApiPool.SERVICE}/remote_services_list",
        )
        return [DaemonConfig(**daemon) for daemon in daemons]

    @staticmethod
    def system() -> list[DaemonModel]:
        """
        获取全部节点的系统信息

        :returns: 节点系统信息列表
        """
        daemons = send(
            "GET",
            f"{ApiPool.SERVICE}/remote_services_system",
        )
        return [DaemonModel(**daemon) for daemon in daemons]

    @staticmethod
    def add(config: dict[str, Any]) -> str:
        """
        新增一个节点

        :params config: 节点的配置信息，以字典形式提供，缺失内容由DaemonConfig模型补全

        :returns: 新增节点的UUID
        """
        return send(
            "POST",
            f"{ApiPool.SERVICE}/remote_service",
            data=DaemonConfig(**config).model_dump(),
        )

    @staticmethod
    def delete(daemonId: str) -> bool:
        """
        删除一个节点

        :params daemonId: 节点的UUID

        :returns: 删除成功后返回True
        """
        return send(
            "DELETE", f"{ApiPool.SERVICE}/remote_service", params={"uuid": daemonId}
        )

    @staticmethod
    def link(daemonId: str) -> bool:
        """
        连接一个节点

        :params daemonId: 节点的UUID

        :returns: 连接成功后返回True
        """
        return send(
            "GET", f"{ApiPool.SERVICE}/link_remote_service", params={"uuid": daemonId}
        )

    @staticmethod
    def update(daemonId: str, config: dict[str, Any]) -> bool:
        """
        更新一个节点的配置

        **不建议直接使用此函数，建议调用overview()后在remote属性内使用节点对象的updateConfig方法按需更新**

        :params daemonId: 节点的UUID
        :params config: 节点的配置信息，以字典形式提供，缺失内容由DaemonConfig模型补全

        :returns: 更新成功后返回True
        """
        return send(
            "PUT",
            f"{ApiPool.SERVICE}/remote_service",
            params={"uuid": daemonId},
            data=DaemonConfig(**config).model_dump(),
        )
