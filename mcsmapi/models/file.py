from pydantic import BaseModel
from typing import List
import os


class FileItem(BaseModel):
    """文件信息"""

    """文件名称"""
    name: str = ""
    """文件大小(单位: byte)"""
    size: int = 0  # byte
    """文件修改时间"""
    time: str = ""
    """文件操作权限(仅适用于Linux)"""
    mode: int = 777  # Linux file permission
    """文件类型，`0`为文件夹，`1`为文件"""
    type: int = 0  # 0 = Folder, 1 = File
    """远程节点uuid"""
    daemonId: str = ""
    """实例的uiid"""
    uuid: str = ""
    """文件所在路径"""
    target: str = ""
    """当前文件列表过滤条件"""
    file_name: str = ""

    def rename(self, newName: str) -> bool:
        """
        重命名该文件或文件夹。

        **参数:**
        - new_name (str): 源文件或文件夹的新名字。

        **返回:**
        - bool: 重命名成功后返回True。
        """
        from mcsmapi.apis.file import File

        return File().rename(
            self.daemonId, self.uuid, os.path.join(self.target, self.name), newName
        )

    def delete(self) -> bool:
        """
        删除该文件或文件夹。

        **返回:**
        - bool: 重命名成功后返回True。
        """
        from mcsmapi.apis.file import File

        return File().delete(
            self.daemonId, self.uuid, [os.path.join(self.target, self.name)]
        )

    def copy(self, target: str) -> bool:
        from mcsmapi.apis.file import File

        return File().copyOne(
            self.daemonId, self.uuid, os.path.join(self.target, self.name), target
        )

    def move(self, target: str) -> bool:
        """
        移动该文件或文件夹到目标路径。

        **参数:**
        - target (str): 目标文件或文件夹的路径。

        **返回:**
        - bool: 移动成功后返回True。
        """
        from mcsmapi.apis.file import File

        return File().moveOne(
            self.daemonId, self.uuid, os.path.join(self.target, self.name), target
        )

    def content(self):
        """
        获取文件内容。
        **返回:**
        - str | bytes: 文件内容。
        """
        from mcsmapi.apis.file import File

        return File().content(
            self.daemonId, self.uuid, os.path.join(self.target, self.name)
        )

    def zip(self, targets: list[str]) -> bool:
        """
        压缩多个文件或文件夹到指定位置。

        **参数:**
        - targets (list): 要压缩到的目标文件的路径。

        **返回:**
        - bool: 压缩成功后返回True。
        """
        from mcsmapi.apis.file import File

        return File().zip(
            self.daemonId, self.uuid, os.path.join(self.target, self.name), targets
        )

    def unzip(self, target: str, code: str = "utf-8") -> bool:
        """
        解压缩该 zip 文件到目标位置。

        **参数:**
        - target (str): 解压到的目标路径。
        - code (str, optional): 压缩文件的编码方式，默认为"utf-8"。
            可选值: utf-8, gbk, big5

        **返回:**
        - bool: 解压成功后返回True。
        """
        from mcsmapi.apis.file import File

        return File().unzip(
            self.daemonId, self.uuid, os.path.join(self.target, self.name), target, code
        )

    def update(self, text: str) -> bool:
        """
        更新该文件内容。
        **参数:**
        - text (str): 文件内容。
        **返回:**
        - bool: 更新成功后返回True。
        """
        from mcsmapi.apis.file import File

        return File().update(
            self.daemonId, self.uuid, os.path.join(self.target, self.name), text
        )

    def download(self) -> str:
        """
        下载该文件。
        **返回:**
        - str: 文件下载的URL。
        """
        from mcsmapi.apis.file import File

        return File().download(
            self.daemonId, self.uuid, os.path.join(self.target, self.name)
        )


class FileList(BaseModel):
    """文件列表"""

    """文件信息列表"""
    items: List[FileItem]
    """当前页数"""
    page: int = 0
    """文件列表单页大小"""
    pageSize: int = 100
    """总页数"""
    total: int = 0
    """当前路径在远程节点的绝对路径"""
    absolutePath: str = "\\"
    """远程节点uuid"""
    daemonId: str = ""
    """实例uuid"""
    uuid: str = ""
    """文件（名称或目录）路径"""
    target: str = ""

    def __init__(self, **data: str):
        super().__init__(**data)
        for item in self.items:
            item.daemonId = self.daemonId
            item.uuid = self.uuid
            item.target = self.target

    async def upload(self, file: bytes, upload_dir: str) -> bool:
        """
        上传文件到实例。

        **参数:**
        - file (bytes): 要上传的文件内容。
        - upload_dir (str): 上传文件的目标目录(包含文件名)。

        **返回:**
        - bool: 返回操作结果，成功时返回True。
        """
        from mcsmapi.apis.file import File

        return await File().upload(self.daemonId, self.uuid, file, upload_dir)

    def createFile(self, target: str) -> bool:
        """
        创建文件。

        **参数:**
        - target (str): 目标文件的路径，包含文件名。

        **返回:**
        - bool: 创建成功后返回True。
        """
        from mcsmapi.apis.file import File

        return File().createFile(self.daemonId, self.uuid, target)

    def createFloder(self, target: str) -> bool:
        """
        创建文件夹

        **参数:**
        - target (str): 目标文件夹的路径。

        **返回:**
        - bool: 创建成功后返回True。
        """
        from mcsmapi.apis.file import File

        return File().createFloder(self.daemonId, self.uuid, target)


class CommonConfig(BaseModel):
    """文件下载密码"""
    password: str = ""
    """文件下载地址"""
    addr: str = ""
