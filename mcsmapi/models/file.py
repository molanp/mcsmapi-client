from pydantic import BaseModel
from typing import List
import os


class FileItem(BaseModel):
    name: str = "New File"
    size: int = 0  # byte
    time: str = ""
    mode: int = 777  # Linux file permission
    type: int = 0  # 0 = Folder, 1 = File
    daemonId: str = ""
    uuid: str = ""
    target: str = ""

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


class FileList(BaseModel):
    items: List[FileItem]
    page: int = 0
    pageSize: int = 100
    total: int = 0
    absolutePath: str = "\\"
    daemonId: str = ""
    uuid: str = ""
    target: str = ""

    def __init__(self, **data: str):
        super().__init__(**data)
        for item in self.items:
            item.daemonId = self.daemonId
            item.uuid = self.uuid
            item.target = self.target



class CommonConfig(BaseModel):
    password: str = ""
    addr: str = ""
