from typing import Any
from mcsmapi.pool import ApiPool
from mcsmapi.request import send
from mcsmapi.models.instance import (
    InstanceSearchList,
    InstanceDetail,
    InstanceCreateResult,
    InstanceConfig,
)


class Instance:
    def search(
        self,
        daemonId: str,
        page: int = 1,
        page_size: int = 20,
        instance_name: str = "",
        status: str = "",
        tag: list[str] | None = None,
    ) -> InstanceSearchList:
        """
        根据指定的参数搜索实例信息

        **参数:**
        - daemonId (str): 守护进程的唯一标识符
        - page (int): 页码，用于指示返回数据的页数。默认为1，表示返回第一页数据
        - page_size (int): 每页大小，用于指定每页包含的数据条数。默认为20，表示每页包含20条数据
        - instance_name (str): 实例的名称。默认为空字符串，表示不进行实例名称过滤
        - status (str): 实例的状态。默认为空字符串，表示不进行状态过滤
        - tag (list[str] | None): 实例的标签列表。默认为None，表示不进行标签过滤

        **返回:**
        - InstanceSearchList: 包含搜索结果的模型。该模型包含了符合搜索条件的实例信息列表，以及总数据条数、总页数等分页信息。
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

    def detail(self, daemonId: str, uuid: str) -> InstanceDetail:
        """
        获取指定实例的详细信息

        **参数:**
        - daemonId (str): 守护进程的唯一标识符
        - uuid (str): 实例的唯一标识符

        **返回:**
        - InstanceDetail: 包含实例详细信息的模型。
        """
        result = send(
            "GET",
            ApiPool.INSTANCE,
            params={"uuid": uuid, "daemonId": daemonId},
        )
        return InstanceDetail(**result)

    def create(self, daemonId: str, config: dict[str, Any]) -> InstanceCreateResult:
        """
        创建一个实例。

        **参数:**
        - daemonId (str): 守护进程的唯一标识符，用于关联新创建的实例。
        - config (dict[str, Any]): 实例的配置信息，以字典形式提供，缺失内容由InstanceConfig模型补全。

        **返回:**
        - InstanceCreateResult: 一个包含新创建实例信息的结果对象，内容由InstanceCreateResult模型定义。
        """
        result = send(
            "POST",
            ApiPool.INSTANCE,
            params={"daemonId": daemonId},
            data=InstanceConfig(**config).dict(),
        )
        return InstanceCreateResult(**result)

    def updateConfig(self, daemonId: str, uuid: str, config: dict) -> str | bool:
        """
        更新实例配置。
        
        **不建议直接使用此函数，建议调用search后在data属性内使用updateConfig方法按需更新**

        **参数:**
        - daemonId (str): 守护进程的标识符。
        - uuid (str): 实例的唯一标识符。
        - config (dict): 新的实例配置，以字典形式提供，缺失内容由InstanceConfig模型补全。

        **返回:**
        - str|bool: 更新成功后返回更新的实例UUID，如果未找到该字段，则默认返回True。
        """
        result = send(
            "PUT",
            ApiPool.INSTANCE,
            params={"uuid": uuid, "daemonId": daemonId},
            data=InstanceConfig(**config).dict(),
        )
        return result.get("uuid", True)

    def delete(
        self, daemonId: str, uuids: list[str], deleteFile: bool = False
    ) -> list[str]:
        """
        删除实例。

        **参数:**
        - daemonId (str): 守护进程的标识符。
        - uuids (list): 要删除的实例UUID列表。
        - deleteFile (bool, optional): 是否删除关联的文件，默认为False。

        **返回:**
        - list[str]: 删除操作后返回的UUID列表。
        """
        return send(
            "DELETE",
            ApiPool.INSTANCE,
            params={"daemonId": daemonId},
            data={"uuids": uuids, "deleteFile": deleteFile},
        )

    def start(self, daemonId: str, uuid: str) -> str | bool:
        """
        启动实例。

        **参数:**
        - daemonId (str): 守护进程的ID，用于标识特定的守护进程。
        - uuid (str): 实例的唯一标识符，用于指定需要启动的实例。

        **返回:**
        - str|bool: 返回结果中的 "instanceUuid" 字段值，如果未找到该字段，则默认返回True。
        """
        result = send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/open",
            params={"daemonId": daemonId, "uuid": uuid},
        )
        return result.get("instanceUuid", True)

    def stop(self, daemonId: str, uuid: str) -> str | bool:
        """
        关闭实例。

        **参数:**
        - daemonId (str): 守护进程的ID，用于标识特定的守护进程。
        - uuid (str): 实例的唯一标识符，用于指定需要关闭的实例。

        **返回:**
        - str|bool: 返回结果中的 "instanceUuid" 字段值，如果未找到该字段，则默认返回True。
        """
        result = send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/stop",
            params={"daemonId": daemonId, "uuid": uuid},
        )
        return result.get("instanceUuid", True)

    def restart(self, daemonId: str, uuid: str) -> str | bool:
        """
        重启实例。

        **参数:**
        - daemonId (str): 守护进程的ID，用于标识特定的守护进程。
        - uuid (str): 实例的唯一标识符，用于指定需要重启的实例。

        **返回:**
        - str|bool: 返回结果中的 "instanceUuid" 字段值，如果未找到该字段，则默认返回True。
        """
        result = send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/restart",
            params={"daemonId": daemonId, "uuid": uuid},
        )
        return result.get("instanceUuid", True)

    def kill(self, daemonId: str, uuid: str) -> str | bool:
        """
        强制关闭实例。

        **参数:**
        - daemonId (str): 守护进程的ID，用于标识特定的守护进程。
        - uuid (str): 实例的唯一标识符，用于指定需要强制关闭的实例。

        **返回:**
        - str|bool: 返回结果中的 "instanceUuid" 字段值，如果未找到该字段，则默认返回True。
        """
        result = send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/kill",
            params={"daemonId": daemonId, "uuid": uuid},
        )
        return result.get("instanceUuid", True)

    def batchOperation(self, instances: list[dict[str, str]], operation: str) -> bool:
        """
        对多个实例进行批量操作。

        **参数:**
        - instances (list[dict[str,str]]): 包含多个实例信息的列表，每个实例信息为一个字典，包含 "uuid" 和 "daemonId" 字段。
        - operation (str): 要执行的操作，可以是 "start", "stop", "restart", 或 "kill"。

        **返回:**
        - list[dict[str,str]]:包含每个实例操作结果的列表，每个结果为一个字典，包含 "uuid" 和 "result" 字段。
        """
        if operation in {"start", "stop", "restart", "kill"}:
            return send("POST", f"{ApiPool.INSTANCE}/multi_{operation}", data=instances)
        else:
            raise ValueError("operation must be one of start, stop, restart, kill")

    def update(self, daemonId: str, uuid: str) -> bool:
        """
        升级实例。

        **参数:**
        - daemonId (str): 守护进程的ID，用于标识特定的守护进程。
        - uuid (str): 实例的唯一标识符，用于指定需要升级的实例。

        **返回:**
        - bool: 返回操作结果，成功时返回True。
        """
        return send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/asynchronous",
            params={"daemonId": daemonId, "uuid": uuid, "task_name": "update"},
        )

    def command(self, daemonId: str, uuid: str, command: str) -> str:
        """
        向实例发送命令。

        **参数:**
        - daemonId (str): 守护进程的ID，用于标识特定的守护进程。
        - uuid (str): 实例的唯一标识符，用于指定需要发送命令的实例。
        - command (str): 要发送的命令。

        **返回:**
        - str|bool: 返回结果中的 "instanceUuid" 字段值，如果未找到该字段，则默认返回True。
        """
        result = send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/command",
            params={"daemonId": daemonId, "uuid": uuid, "command": command},
        )
        return result.get("instanceUuid", True)

    def get_output(self, daemonId: str, uuid: str, size: int | str = "") -> str:
        """
        获取实例输出。

        **参数:**
        - daemonId (str): 守护进程的ID，用于标识特定的守护进程。
        - uuid (str): 实例的唯一标识符，用于指定需要获取输出的实例。
        - size (int, optional): 获取的日志大小: 1KB ~ 2048KB，如果未设置，则返回所有日志

        **返回:**
        - str: 返回结果中的 "instanceUuid" 字段值，如果未找到该字段，则默认返回True。
        """
        return send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/outputlog",
            params={"daemonId": daemonId, "uuid": uuid, "size": size},
        )

    def reinstall(
        self,
        daemonId: str,
        uuid: str,
        targetUrl: str,
        title: str = "",
        description: str = "",
    ) -> bool:
        """
        重装实例。

        **参数:**
        - daemonId (str): 守护进程的ID，用于标识特定的守护进程。
        - uuid (str): 实例的唯一标识符。
        - targetUrl (str): 重装文件的目标URL。
        - title (str): 重装文件的标题。
        - description (str, optional): 重装文件的描述，默认为空字符串。

        **返回:**
        - bool: 返回操作结果，成功时返回True。
        """
        return send(
            "POST",
            f"{ApiPool.PROTECTED_INSTANCE}/install_instance",
            params={"uuid": uuid, "daemonId": daemonId},
            data={"targetUrl": targetUrl, "title": title, "description": description},
        )
