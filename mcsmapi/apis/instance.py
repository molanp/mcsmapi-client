from typing import Any, Literal
from mcsmapi.pool import ApiPool
from mcsmapi.request import send
from mcsmapi.models.instance import (
    InstanceSearchList,
    InstanceDetail,
    InstanceCreateResult,
    InstanceConfig,
    batchOperationDetail,
)


class Instance:
    @staticmethod
    def search(
        daemonId: str,
        page: int = 1,
        page_size: int = 20,
        instance_name: str = "",
        status: Literal[-1, 0, 1, 2, 3, ""] = "",
        tag: list[str] | None = None,
    ) -> InstanceSearchList:
        """
        根据指定的参数搜索实例信息

        :params daemonId: 节点的UUID
        :params page: 页码，用于指示返回数据的页数
        :params page_size: 每页大小，用于指定每页包含的数据条数
        :params instance_name: 用于过滤的实例名称
        :params status: 用于过滤的实例状态
        :params tag: 用于过滤的实例标签列表

        :returns: 包含搜索结果的模型
        """
        if tag is None:
            tag = []
        result = send(
            "GET",
            "api/service/remote_service_instances",
            params={
                "daemonId": daemonId,
                "page": page,
                "page_size": page_size,
                "instance_name": instance_name,
                "status": status,
                "tag": tag,
            },
        )
        return InstanceSearchList(**result, daemonId=daemonId)

    @staticmethod
    def detail(daemonId: str, uuid: str) -> InstanceDetail:
        """
        获取指定实例的详细信息

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID

        :returns: 包含实例详细信息的模型
        """
        result = send(
            "GET",
            ApiPool.INSTANCE,
            params={"uuid": uuid, "daemonId": daemonId},
        )
        return InstanceDetail(**result)

    @staticmethod
    def create(daemonId: str, config: dict[str, Any]) -> InstanceCreateResult:
        """
        创建一个实例

        :params daemonId: 节点的UUID，用于关联新创建的实例
        :params config: 实例的配置信息，以字典形式提供，缺失内容由InstanceConfig模型补全

        :returns: 一个包含新创建实例信息的结果对象，内容由InstanceCreateResult模型定义
        """
        result = send(
            "POST",
            ApiPool.INSTANCE,
            params={"daemonId": daemonId},
            data=InstanceConfig(**config).model_dump(),
        )
        return InstanceCreateResult(**result)

    @staticmethod
    def updateConfig(daemonId: str, uuid: str, config: dict[str, Any]) -> str:
        """
        更新实例配置

        **不建议直接使用此函数，建议调用search后使用实例对象的updateConfig方法按需更新**

        :params daemonId: 节点的标识符
        :params uuid: 实例的UUID
        :params config: 新的实例配置，以字典形式提供，缺失内容由InstanceConfig模型补全

        :returns: 更新成功后返回更新的实例UUID
        """
        result = send(
            "PUT",
            ApiPool.INSTANCE,
            params={"uuid": uuid, "daemonId": daemonId},
            data=InstanceConfig(**config).model_dump(),
        )
        return result["instanceUuid"]

    @staticmethod
    def delete(daemonId: str, uuids: list[str], deleteFile: bool = False) -> list[str]:
        """
        删除实例

        :params daemonId: 节点的标识符
        :params uuids: 要删除的实例UUID列表
        :params deleteFile: 是否删除关联的文件

        :returns: 被删除的实例UUID列表
        """
        return send(
            "DELETE",
            ApiPool.INSTANCE,
            params={"daemonId": daemonId},
            data={"uuids": uuids, "deleteFile": deleteFile},
        )

    @staticmethod
    def start(daemonId: str, uuid: str) -> str:
        """
        启动实例

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID

        :returns: 返回被操作的实例的UUID
        """
        result = send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/open",
            params={"daemonId": daemonId, "uuid": uuid},
        )
        return result["instanceUuid"]

    @staticmethod
    def stop(daemonId: str, uuid: str) -> str:
        """
        关闭实例

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID

        :returns: 返回被操作的实例的UUID
        """
        result = send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/stop",
            params={"daemonId": daemonId, "uuid": uuid},
        )
        return result["instanceUuid"]

    @staticmethod
    def restart(daemonId: str, uuid: str) -> str:
        """
        重启实例

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID

        :returns: 返回被操作的实例的UUID
        """
        result = send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/restart",
            params={"daemonId": daemonId, "uuid": uuid},
        )
        return result["instanceUuid"]

    @staticmethod
    def kill(daemonId: str, uuid: str) -> str:
        """
        强制关闭实例

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID

        :returns: 返回被操作的实例的UUID
        """
        result = send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/kill",
            params={"daemonId": daemonId, "uuid": uuid},
        )
        return result["instanceUuid"]

    @staticmethod
    def batchOperation(
        instances: list[batchOperationDetail],
        operation: Literal["start", "stop", "restart", "kill"],
    ) -> bool:
        """
        对多个实例进行批量操作

        :params instances: 包含多个实例信息的列表
        :params operation: 要执行的操作

        :returns: 操作成功返回True
        """
        return send("POST", f"{ApiPool.INSTANCE}/multi_{operation}", data=instances)

    @staticmethod
    def update(daemonId: str, uuid: str) -> bool:
        """
        更新实例

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID

        :returns: 操作成功返回True
        """
        return send(
            "POST",
            f"{ApiPool.PROTECTED_INSTANCE}/asynchronous",
            params={"daemonId": daemonId, "uuid": uuid, "task_name": "update"},
        )

    @staticmethod
    def command(daemonId: str, uuid: str, command: str) -> str:
        """
        向实例发送命令

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params command: 要发送的命令

        :params: 返回被操作的实例的UUID
        """
        result = send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/command",
            params={"daemonId": daemonId, "uuid": uuid, "command": command},
        )
        return result["instanceUuid"]

    @staticmethod
    def get_output(daemonId: str, uuid: str, size: int | None = None) -> str:
        """
        获取实例输出

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params size: 获取的输出大小: 1KB ~ 2048KB，如果未设置，则返回所有日志
        """
        return send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/outputlog",
            params={"daemonId": daemonId, "uuid": uuid, "size": size},
        )

    @staticmethod
    def reinstall(
        daemonId: str,
        uuid: str,
        targetUrl: str,
        title: str = "",
        description: str = "",
    ) -> bool:
        """
        重装实例

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params targetUrl: 重装文件的目标URL
        :params title: 重装文件的标题
        :params description: 重装文件的描述

        :returns: 操作成功返回True
        """
        return send(
            "POST",
            f"{ApiPool.PROTECTED_INSTANCE}/install_instance",
            params={"uuid": uuid, "daemonId": daemonId},
            data={"targetUrl": targetUrl, "title": title, "description": description},
        )
