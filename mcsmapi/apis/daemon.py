from typing import Any
from ..pool import ApiPool
from ..request import send
from ..models.daemon import DaemonConfig


class Daemon:
    def add(self, config: dict) -> str:
        """
        新增一个节点。

        参数:
        - config (dict): 节点的配置信息，以字典形式提供，缺失内容由DaemonConfig模型补全。

        返回:
        - str: 新增节点的ID
        """
        return send(
            "POST",
            f"{ApiPool.SERVICE}/remote_service",
            data=DaemonConfig(**config).dict(),
        )

    def delete(self, daemonId: str) -> bool:
        """
        删除一个节点。

        参数:
        - daemonId (str): 节点的唯一标识符。

        返回:
        - bool: 删除成功后返回True
        """
        return send(
            "DELETE", f"{ApiPool.SERVICE}/remote_service", params={"uuid": daemonId}
        )

    def link(self, daemonId: str) -> bool:
        """
        连接一个节点。

        参数:
        - daemonId (str): 节点的唯一标识符。

        返回:
        - bool: 连接成功后返回True
        """
        return send(
            "GET", f"{ApiPool.SERVICE}/link_remote_service", params={"uuid": daemonId}
        )

    def update(self, daemonId: str, config: dict[str, Any]) -> bool:
        """
        更新一个节点的配置。

        参数:
        - daemonId (str): 节点的唯一标识符。
        - config (dict): 节点的配置信息，以字典形式提供，缺失内容由DaemonConfig模型补全。

        返回:
        - bool: 更新成功后返回True
        """
        return send(
            "PUT",
            f"{ApiPool.SERVICE}/remote_service",
            params={"uuid": daemonId},
            data=DaemonConfig(**config).dict(),
        )
