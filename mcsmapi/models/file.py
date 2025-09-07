from enum import IntEnum
from typing import Any, Literal
from pydantic import BaseModel, field_validator
import os


class FileType(IntEnum):
    """文件类型"""

    FOLDER = 0
    FILE = 1


class FileItem(BaseModel):
    """文件信息"""

    name: str
    """文件或文件夹名称"""
    size: int
    """文件大小(单位: byte)"""
    time: str
    """文件修改时间"""
    mode: int
    """文件操作权限(仅适用于Linux)"""
    type: FileType
    """文件类型"""
    daemonId: str = ""
    """远程节点uuid"""
    uuid: str = ""
    """实例的uiid"""
    target: str = ""
    """文件所在路径"""
    file_name: str
    """当前文件列表过滤条件"""

    def rename(self, newName: str):
        """
        重命名该文件或文件夹

        :params new_name: 源文件或文件夹的新名字

        :returns: 操作成功后返回True
        """
        from mcsmapi.apis.file import File

        return File.rename(
            self.daemonId, self.uuid, os.path.join(self.target, self.name), newName
        )

    def delete(self):
        """
        删除该文件或文件夹

        :returns: 操作成功后返回True
        """
        from mcsmapi.apis.file import File

        return File.delete(
            self.daemonId, self.uuid, [os.path.join(self.target, self.name)]
        )

    def copy2(self, target: str):
        """
        复制该文件或文件夹到目标路径

        :param target: 目标路径

        :returns: 操作成功后返回True
        """
        from mcsmapi.apis.file import File

        return File.copyOne(
            self.daemonId, self.uuid, os.path.join(self.target, self.name), target
        )

    def move(self, target: str):
        """
        移动该文件或文件夹到目标路径

        :params target: 目标文件或文件夹的路径

        :returns: 操作成功后返回True
        """
        from mcsmapi.apis.file import File

        return File.moveOne(
            self.daemonId, self.uuid, os.path.join(self.target, self.name), target
        )

    def content(self):
        """
        获取文件内容

        :returns: 文件内容
        """
        from mcsmapi.apis.file import File

        return File.content(
            self.daemonId, self.uuid, os.path.join(self.target, self.name)
        )

    def zip(self, targets: list[str]):
        """
        压缩该文件或文件夹到指定位置

        :params targets: 要压缩到的目标文件的路径

        :returns: 操作成功后返回True
        """
        from mcsmapi.apis.file import File

        return File.zip(
            self.daemonId, self.uuid, os.path.join(self.target, self.name), targets
        )

    def unzip(self, target: str, code: Literal["utf-8", "gbk", "big5"] = "utf-8"):
        """
        解压缩该 zip 文件到目标位置

        :params target: 解压到的目标路径
        :params code: 压缩文件的编码方式

        :returns: 操作成功后返回True
        """
        from mcsmapi.apis.file import File

        return File.unzip(
            self.daemonId, self.uuid, os.path.join(self.target, self.name), target, code
        )

    def update(self, text: str):
        """
        更新该文件内容

        :params text: 文件内容

        :returns: 操作成功后返回True
        """
        from mcsmapi.apis.file import File

        return File.update(
            self.daemonId, self.uuid, os.path.join(self.target, self.name), text
        )

    def download(self):
        """
        下载该文件

        :returns: 文件下载的URL
        """
        from mcsmapi.apis.file import File

        return File.download(
            self.daemonId, self.uuid, os.path.join(self.target, self.name)
        )


class FileList(BaseModel):
    """文件列表"""

    items: list[FileItem]
    """文件信息列表"""
    page: int
    """当前页数"""
    pageSize: int
    """文件列表单页大小"""
    total: int
    """总页数"""
    absolutePath: str
    """当前路径在远程节点的绝对路径"""
    daemonId: str
    """远程节点uuid"""
    uuid: str
    """实例uuid"""
    target: str
    """文件（名称或目录）路径"""

    @field_validator("items", mode="before")
    @classmethod
    def fill_info(cls, v: Any, info) -> Any:
        """在验证 items 字段前填充基本信息"""
        if isinstance(info.data, dict):
            daemon_id = info.data.get("daemonId", "")
            uuid = info.data.get("uuid", "")
            target = info.data.get("target", "")
            if isinstance(v, list):
                for item in v:
                    if isinstance(item, dict):
                        item["daemonId"] = daemon_id
                        item["uuid"] = uuid
                        item["target"] = target
        return v

    async def upload(self, file: bytes, upload_dir: str) -> bool:
        """
        上传文件到实例

        :params file: 要上传的文件内容
        :params upload_dir: 文件上传到的目标路径

        :returns: 操作成功返回True
        """
        from mcsmapi.apis.file import File

        return await File.upload(self.daemonId, self.uuid, file, upload_dir)

    def createFile(self, target: str) -> bool:
        """
        创建文件

        :params target: 目标文件的路径，包含文件名

        :returns: 操作成功后返回True
        """
        from mcsmapi.apis.file import File

        return File.createFile(self.daemonId, self.uuid, target)

    def createFolder(self, target: str) -> bool:
        """
        创建文件夹

        :params target: 目标文件夹的路径

        :returns: 操作成功后返回True
        """
        from mcsmapi.apis.file import File

        return File.createFolder(self.daemonId, self.uuid, target)


class FileDownloadConfig(BaseModel):

    password: str
    """文件下载密码"""
    addr: str
    """文件下载地址"""
