from mcsmapi.pool import ApiPool
from mcsmapi.request import Request, send, upload
from mcsmapi.models.file import CommonConfig, FileList
import urllib.parse
import os


class File:
    def show(
        self,
        daemonId: str,
        uuid: str,
        target: str = "",
        page: int = 0,
        page_size: int = 100,
        file_name: str = ""
    ) -> FileList:
        """
        获取文件列表

        **参数:**
        - daemonId (str): 守护进程的唯一标识符。
        - uuid (str): 文件实例的唯一标识符。
        - target (str, 可选): 用于文件过滤的目标路径。默认为空字符串，表示不按路径过滤。
        - page (int, 可选): 指定分页的页码。默认为0。
        - page_size (int, 可选): 指定每页的文件数量。默认为100。
        - file_name (str, 可选): 用于在文件列表中过滤出名称包含指定字符串的文件或文件夹

        **返回:**
        - FileList: 包含文件列表信息和分页详情的FileList模型。
        """
        result = send(
            "GET",
            f"{ApiPool.FILE}/list",
            params={
                "daemonId": daemonId,
                "uuid": uuid,
                "target": target,
                "page": page,
                "page_size": page_size,
                "file_name": file_name,
            },
        )
        return FileList(**result, daemonId=daemonId, uuid=uuid)

    def content(self, daemonId: str, uuid: str, target: str) -> str | bytes:
        """
        获取文件内容

        **参数:**
        - daemonId (str): 守护进程的唯一标识符。
        - uuid (str): 文件实例的唯一标识符。
        - target (str): 文件的目标路径。

        **返回:**
        - str: 文件的内容信息。
        """
        return send(
            "PUT",
            f"{ApiPool.FILE}",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"target": target},
        )

    def update(self, daemonId: str, uuid: str, target: str, text: str) -> bool:
        """
        更新文件内容

        **参数:**
        - daemonId (str): 守护进程的唯一标识符。
        - uuid (str): 文件实例的唯一标识符。
        - target (str): 文件的目标路径。
        - text (str): 新的文件内容。

        **返回:**
        - bool: 更新成功后返回True。
        """
        return send(
            "PUT",
            f"{ApiPool.FILE}",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"target": target, "text": text},
        )

    def download(self, daemonId: str, uuid: str, file_name: str) -> str:
        """
        下载文件

        **参数:**
        - daemonId (str): 守护进程的唯一标识符。
        - uuid (str): 文件实例的唯一标识符。
        - file_name (str): 要下载的文件名。路径+名字, 示例: /backup/world.zip

        **返回:**
        - str: 文件下载URL。
        """

        result = send(
            "POST",
            f"{ApiPool.FILE}/download",
            params={"daemonId": daemonId, "uuid": uuid, "file_name": file_name},
        )
        result = CommonConfig(**result)
        protocol = Request.mcsm_url.split("://")[0]
        base_url = urllib.parse.urljoin(f"{protocol}://{result.addr}", "download")
        return urllib.parse.urljoin(base_url, f"{result.password}/{file_name}")

    async def upload(
        self, daemonId: str, uuid: str, file: bytes, upload_dir: str
    ) -> bool:
        """
        上传文件

        **参数:**
        - daemonId (str): 守护进程的唯一标识符。
        - uuid (str): 文件实例的唯一标识符。
        - file (bytes): 要上传的文件内容。
        - upload_dir (str): 文件上传到的目标路径。

        **返回:**
        - bool: 上传成功后返回True。
        """
        result = send(
            "POST",
            f"{ApiPool.FILE}/upload",
            params={"daemonId": daemonId, "uuid": uuid, "upload_dir": upload_dir},
        )
        result = CommonConfig(**result)
        protocol = Request.mcsm_url.split("://")[0]
        base_url = urllib.parse.urljoin(f"{protocol}://{result.addr}", "upload")
        final_url = urllib.parse.urljoin(base_url, result.password)
        await upload(final_url, file)
        return True

    def copy(self, daemonId: str, uuid: str, copy_map: dict[str, str]) -> bool:
        """
        复制多个文件夹或文件到指定位置。

        **参数:**
        - daemonId (str): 守护进程的唯一标识符。
        - uuid (str): 文件实例的唯一标识符。
        - copy_map (dict): 复制映射，格式为 {源路径: 目标路径}

        **返回:**
        - bool: 上传成功后返回True。
        """
        targets = [[source, target] for source, target in copy_map.items()]
        return send(
            "POST",
            f"{ApiPool.FILE}/copy",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"targets": targets},
        )

    def copyOne(self, daemonId: str, uuid: str, source: str, target: str) -> bool:
        """
        复制单个文件或文件夹到指定位置。

        **参数:**
        - daemonId (str): 守护进程的唯一标识符。
        - uuid (str): 实例的唯一标识符。
        - source (str): 源文件或文件夹的路径。
        - target (str): 目标文件或文件夹的路径。

        **返回:**
        - bool: 移动成功后返回True。
        """
        return self.copy(daemonId, uuid, {source: target})

    def move(self, daemonId: str, uuid: str, copy_map: dict[str, str]) -> bool:
        """
        移动多个文件或文件夹到指定位置。

        参数:
        - daemonId (str): 守护进程的唯一标识符。
        - uuid (str): 实例的唯一标识符。
        - copy_map (dict): 移动映射，格式为 {源路径: 目标路径}

        返回:
        - bool: 移动成功后返回True。
        """
        targets = [[source, target] for source, target in copy_map.items()]
        return send(
            "PUT",
            f"{ApiPool.FILE}/move",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"targets": targets},
        )

    def moveOne(self, daemonId: str, uuid: str, source: str, target: str) -> bool:
        """
        从源路径移动单个文件或文件夹到目标路径。

        参数:
        - daemonId (str): 守护进程的唯一标识符。
        - uuid (str): 实例的唯一标识符。
        - source (str): 源文件或文件夹的路径。
        - target (str): 目标文件或文件夹的路径。

        返回:
        - bool: 移动成功后返回True。
        """
        return self.move(daemonId, uuid, {source: target})

    def rename(self, daemonId: str, uuid: str, source: str, new_name: str) -> bool:
        """
        重命名单个文件或文件夹。

        **参数:**
        - daemonId (str): 守护进程的唯一标识符。
        - uuid (str): 实例的唯一标识符。
        - source (str): 源文件或文件夹的路径。
        - new_name (str): 源文件或文件夹的新名字。

        **返回:**
        - bool: 重命名成功后返回True。
        """
        directory = os.path.dirname(source)
        target = os.path.join(directory, new_name)
        return self.moveOne(daemonId, uuid, source, target)

    def zip(self, daemonId: str, uuid: str, source: str, targets: list[str]) -> bool:
        """
        压缩多个文件或文件夹到指定位置。

        **参数:**
        - daemonId (str): 守护进程的唯一标识符。
        - uuid (str): 实例的唯一标识符。
        - source (str): 需要压缩的文件路径。
        - targets (list): 要压缩到的目标文件的路径。

        **返回:**
        - bool: 压缩成功后返回True。
        """
        return send(
            "POST",
            f"{ApiPool.FILE}/compress",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"type": 1, "code": "utf-8", "source": source, "targets": targets},
        )

    def unzip(
        self, daemonId: str, uuid: str, source: str, target: str, code: str = "utf-8"
    ) -> bool:
        """
        解压缩指定的zip文件到目标位置。

        **参数:**
        - daemonId (str): 守护进程的唯一标识符。
        - uuid (str): 实例的唯一标识符。
        - source (str): 需要解压的zip文件路径。
        - target (str): 解压到的目标路径。
        - code (str, optional): 压缩文件的编码方式，默认为"utf-8"。
            可选值: utf-8, gbk, big5

        **返回:**
        - bool: 解压成功后返回True。
        """
        return send(
            "POST",
            f"{ApiPool.FILE}/compress",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"type": 2, "code": code, "source": source, "targets": target},
        )

    def delete(self, daemonId: str, uuid: str, targets: list[str]) -> bool:
        """
        删除多个文件或文件夹。

        **参数:**
        - daemonId (str): 守护进程的唯一标识符。
        - uuid (str): 实例的唯一标识符。
        - targets (list): 要删除的文件或文件夹的路径。

        **返回:**
        - bool: 删除成功后返回True。
        """
        return send(
            "DELETE",
            ApiPool.FILE,
            params={"daemonId": daemonId, "uuid": uuid},
            data={"targets": targets},
        )

    def createFile(self, daemonId: str, uuid: str, target: str) -> bool:
        """
        创建文件。

        **参数:**
        - daemonId (str): 守护进程的唯一标识符。
        - uuid (str): 实例的唯一标识符。
        - target (str): 目标文件的路径，包含文件名。

        **返回:**
        - bool: 创建成功后返回True。
        """
        return send(
            "POST",
            f"{ApiPool.FILE}/touch",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"target": target},
        )

    def createFloder(self, daemonId: str, uuid: str, target: str) -> bool:
        """
        创建文件夹

        **参数:**
        - daemonId (str): 守护进程的唯一标识符。
        - uuid (str): 实例的唯一标识符。
        - target (str): 目标文件夹的路径。

        **返回:**
        - bool: 创建成功后返回True。
        """
        return send(
            "POST",
            f"{ApiPool.FILE}/mkdir",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"target": target},
        )
