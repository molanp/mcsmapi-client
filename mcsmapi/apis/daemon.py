from typing import Any
from mcsmapi.pool import ApiPool
from mcsmapi.request import send
from mcsmapi.models.daemon import (
    DaemonConfig,
    DaemonInfo,
    DaemonSystemInfo,
    DaemonStatus,
    DaemonUpdateConfig,
)


class Daemon:
    @staticmethod
    def config() -> list[DaemonStatus]:
        """
        获取全部节点配置信息

        :returns: 节点的配置信息列表
        """
        daemons = send(
            "GET",
            f"{ApiPool.SERVICE}/remote_services_list",
        )
        return [DaemonStatus(**daemon) for daemon in daemons]

    @staticmethod
    def info() -> list[DaemonInfo]:
        """
        获取全部节点信息

        :returns: 节点信息列表
        """
        daemons = send(
            "GET",
            f"{ApiPool.SERVICE}/remote_services",
        )
        return [DaemonInfo(**daemon) for daemon in daemons]

    @staticmethod
    def system() -> list[DaemonSystemInfo]:
        """
        获取全部节点的系统信息

        :returns: 节点系统信息列表
        """
        daemons = send(
            "GET",
            f"{ApiPool.SERVICE}/remote_services_system",
        )
        return [DaemonSystemInfo(**daemon) for daemon in daemons]

    @staticmethod
    def add(config: DaemonConfig) -> str:
        """
        新增一个节点

        :params config: 节点的配置信息

        :returns: 新增节点的UUID
        """
        return send(
            "POST",
            f"{ApiPool.SERVICE}/remote_service",
            data=config.model_dump(),
        )

    @staticmethod
    def delete(daemonId: str) -> bool:
        """
        删除一个节点

        :params daemonId: 节点的UUID

        :returns: 操作成功后返回True
        """
        return send(
            "DELETE", f"{ApiPool.SERVICE}/remote_service", params={"uuid": daemonId}
        )

    @staticmethod
    def link(daemonId: str) -> bool:
        """
        连接一个节点

        :params daemonId: 节点的UUID

        :returns: 操作成功后返回True
        """
        return send(
            "GET", f"{ApiPool.SERVICE}/link_remote_service", params={"uuid": daemonId}
        )

    @staticmethod
    def update(daemonId: str, config: dict[str, Any]) -> bool:
        """
        更新一个节点的配置

        :params daemonId: 节点的UUID
        :params config: 节点的配置信息，以字典形式提供，缺失内容由DaemonUpdateConfig模型补全

        :returns: 操作成功后返回True
        """
        return send(
            "PUT",
            f"{ApiPool.SERVICE}/remote_service",
            params={"uuid": daemonId},
            data=DaemonUpdateConfig(**config).model_dump(),
        )
