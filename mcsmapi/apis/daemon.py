from typing import Any
from mcsmapi.pool import ApiPool
from mcsmapi.request import send
from mcsmapi.models.daemon import DaemonConfig, DaemonModel
from mcsmapi.models.daemon.instance import InstanceDetail


class Daemon:
    def show(self) -> list[DaemonConfig]:
        """
        获取全部节点配置信息

        返回:
        - List[DaemonConfig]: 节点的配置信息列表
        """
        daemons = send(
            "GET",
            f"{ApiPool.SERVICE}/remote_services_list",
        )
        return [DaemonConfig(**daemon) for daemon in daemons]
        
    def system(self) -> list[DaemonModel]:
        """
        获取全部节点的系统信息
        
        返回:
        - List[DaemonModel]: 节点系统信息列表
        """
        daemons = send(
            "GET",
            f"{ApiPool.SERVICE}/remote_services_system",
        )
        return [DaemonModel(**daemon) for daemon in daemons]
    
    def instances(self, daemonId: str, page: int = 0, page_size: int = 10, instance_name: str = "", status: int = 0, tag: list[str] | None = None) -> list[InstanceDetail]:
        """
        查询指定节点下的实例详细信息
        
        参数:
        - `daemonId` (str): 要查询的守护进程（Daemon）的唯一标识符。
        - `page` (int, 默认=0): 分页查询的页码（从 0 开始）。
        - `page_size` (int, 默认=10): 每页返回的实例数量。
        - `instance_name` (str, 默认=""): 过滤指定名称的实例。
        - `status` (int, 默认=0): 过滤指定状态的实例，如运行中、已停止等。
        - `tag` (List[str] | None, 默认=None): 根据标签筛选实例（可选参数）。
      
        返回:
        - `List[InstanceDetail]`: 包含实例详细信息的列表。
      
        注意:
        - 此方法尚未实现 (`raise RuntimeError`)，因为 MCSM 官方文档未提供足够的信息。
        - 由于根据 MCSM 源代码的测试无法获取有效数据，目前无法完成该功能的开发。
        - 如果你有具体的实现思路，请在 issue 中提出
        - 可供参考 MCSM 源码: [daemon_router.ts 第 32 行](https://github.com/MCSManager/MCSManager/blob/master/panel%2Fsrc%2Fapp%2Frouters%2Fdaemon_router.ts#L32-L32)
        - 模型定义代码: https://github.com/MCSManager/MCSManager/blob/master/frontend%2Fsrc%2Fservices%2Fapis%2Findex.ts#L86-L86
        - 测试地址示例:
            `http://localhost:23333/api/service/remote_service_instances?apikey=xxx&daemonId=xxx&page=0&page_size=10&status=3&instance_name=`
        """
        raise RuntimeError("此方法尚未实现")

    def add(self, config: dict[str, Any]) -> str:
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
        
        **不建议直接使用此函数，建议调用overview()后在remote属性内使用updateConfig方法按需更新**

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
