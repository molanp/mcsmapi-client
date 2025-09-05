from typing import Literal
from mcsmapi.pool import ApiPool
from mcsmapi.request import Request, send, upload
from mcsmapi.models.file import FileDownloadConfig, FileList
import urllib.parse
import os


class File:
    @staticmethod
    def show(
        daemonId: str,
        uuid: str,
        target: str = "",
        page: int = 0,
        page_size: int = 100,
        file_name: str = "",
    ) -> FileList:
        """
        获取文件列表

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params target: 用于文件过滤的目标路径
        :params page: 指定分页的页码
        :params page_size: 指定每页的文件数量
        :params file_name: 用于在文件列表中过滤出名称包含指定字符串的文件或文件夹

        :returns: 包含文件列表信息和分页详情的FileList模型
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

    @staticmethod
    def content(daemonId: str, uuid: str, target: str) -> str:
        """
        获取文件内容

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params target: 文件的目标路径

        :returns: 文件的内容信息
        """
        return send(
            "PUT",
            f"{ApiPool.FILE}",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"target": target},
        )

    @staticmethod
    def update(daemonId: str, uuid: str, target: str, text: str) -> bool:
        """
        更新文件内容

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params target: 目标文件的路径
        :params text: 新的文件内容

        :returns: 更新成功后返回True
        """
        return send(
            "PUT",
            f"{ApiPool.FILE}",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"target": target, "text": text},
        )

    @staticmethod
    def download(daemonId: str, uuid: str, file_name: str) -> str:
        """
        下载文件

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params file_name: 要下载的文件的实例内完整路径, eg: /backup/world.zip

        :returns: 文件下载URL
        """

        result = send(
            "POST",
            f"{ApiPool.FILE}/download",
            params={"daemonId": daemonId, "uuid": uuid, "file_name": file_name},
        )
        result = FileDownloadConfig(**result)
        protocol = Request.mcsm_url.split("://")[0]
        base_url = urllib.parse.urljoin(f"{protocol}://{result.addr}", "download")
        return urllib.parse.urljoin(base_url, f"{result.password}/{file_name}")

    @staticmethod
    async def upload(daemonId: str, uuid: str, file: bytes, upload_dir: str) -> bool:
        """
        上传文件

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params file: 要上传的文件内容
        :params upload_dir: 文件上传到的目标路径

        :returns: 上传成功后返回True
        """
        result = send(
            "POST",
            f"{ApiPool.FILE}/upload",
            params={"daemonId": daemonId, "uuid": uuid, "upload_dir": upload_dir},
        )
        result = FileDownloadConfig(**result)
        protocol = Request.mcsm_url.split("://")[0]
        base_url = urllib.parse.urljoin(f"{protocol}://{result.addr}", "upload")
        final_url = urllib.parse.urljoin(base_url, result.password)
        await upload(final_url, file)
        return True

    @staticmethod
    def copy(daemonId: str, uuid: str, copy_map: dict[str, str]) -> bool:
        """
        复制多个文件夹或文件到指定位置

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params copy_map: 复制映射，格式为 {源路径: 目标路径}

        :returns: 复制成功后返回True
        """
        targets = [[source, target] for source, target in copy_map.items()]
        return send(
            "POST",
            f"{ApiPool.FILE}/copy",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"targets": targets},
        )

    @staticmethod
    def copyOne(daemonId: str, uuid: str, source: str, target: str) -> bool:
        """
        复制单个文件或文件夹到指定位置

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params source: 源文件或文件夹的路径
        :params target: 目标文件或文件夹的路径

        :return: 移动成功后返回True
        """
        return File.copy(daemonId, uuid, {source: target})

    @staticmethod
    def move(daemonId: str, uuid: str, copy_map: dict[str, str]) -> bool:
        """
        移动多个文件或文件夹到指定位置

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params copy_map: 移动映射，格式为 {源路径: 目标路径}

        :returns: 移动成功后返回True
        """
        targets = [[source, target] for source, target in copy_map.items()]
        return send(
            "PUT",
            f"{ApiPool.FILE}/move",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"targets": targets},
        )

    @staticmethod
    def moveOne(daemonId: str, uuid: str, source: str, target: str) -> bool:
        """
        从源路径移动单个文件或文件夹到目标路径

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params source: 源文件或文件夹的路径
        :params target: 目标文件或文件夹的路径

        :returns: 移动成功后返回True
        """
        return File.move(daemonId, uuid, {source: target})

    @staticmethod
    def rename(daemonId: str, uuid: str, source: str, new_name: str) -> bool:
        """
        重命名单个文件或文件夹

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params source: 源文件或文件夹的路径
        :params new_name: 源文件或文件夹的新名字

        :returns: 重命名成功后返回True
        """
        directory = os.path.dirname(source)
        target = os.path.join(directory, new_name)
        return File.moveOne(daemonId, uuid, source, target)

    @staticmethod
    def zip(daemonId: str, uuid: str, source: str, targets: list[str]) -> bool:
        """
        压缩多个文件或文件夹到指定位置

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params source: 要压缩到的目标文件的路径
        :params targets: 需要压缩的文件路径

        **返回:**
        - bool: 压缩成功后返回True
        """
        return send(
            "POST",
            f"{ApiPool.FILE}/compress",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"type": 1, "code": "utf-8", "source": source, "targets": targets},
        )

    @staticmethod
    def unzip(
        daemonId: str,
        uuid: str,
        source: str,
        targets: str,
        code: Literal["utf-8", "gbk", "big5"] = "utf-8",
    ) -> bool:
        """
        解压缩指定的zip文件到目标位置

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params source: 需要解压的zip文件路径
        :params targets: 解压到的目标路径
        :params code: 压缩文件的编码方式

        :returns: 解压成功后返回True
        """
        return send(
            "POST",
            f"{ApiPool.FILE}/compress",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"type": 2, "code": code, "source": source, "targets": targets},
        )

    @staticmethod
    def delete(daemonId: str, uuid: str, targets: list[str]) -> bool:
        """
        删除多个文件或文件夹

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params targets: 要删除的文件或文件夹的路径

        :returns: 删除成功后返回True
        """
        return send(
            "DELETE",
            ApiPool.FILE,
            params={"daemonId": daemonId, "uuid": uuid},
            data={"targets": targets},
        )

    @staticmethod
    def createFile(daemonId: str, uuid: str, target: str) -> bool:
        """
        创建文件

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params target: 目标文件的路径，包含文件名

        :returns: 创建成功后返回True
        """
        return send(
            "POST",
            f"{ApiPool.FILE}/touch",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"target": target},
        )

    @staticmethod
    def createFolder(daemonId: str, uuid: str, target: str) -> bool:
        """
        创建文件夹

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params target: 目标文件夹的路径

        :returns: 创建成功后返回True
        """
        return send(
            "POST",
            f"{ApiPool.FILE}/mkdir",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"target": target},
        )
