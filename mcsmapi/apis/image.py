from mcsmapi.pool import ApiPool
from mcsmapi.request import send
from mcsmapi.models.image import DockerImageItem, DockerContainerItem, DockerNetworkItem


class Image:
    def images(self, daemonId: str) -> list[DockerImageItem]:
        """
        获取镜像列表

        **参数:**
        - daemonId (str): 守护进程的唯一标识符。

        **返回:**
        - list[ImageModel]: 包含镜像列表详情的 ImageModel 模型的列表。
        """
        result = send(
            "GET",
            f"{ApiPool.IMAGE}/image",
            params={
                "daemonId": daemonId,
            },
        )

        return [DockerImageItem(**item) for item in result]

    def containers(self, daemonId: str) -> list[DockerContainerItem]:
        """
        获取容器列表

        **参数:**
        - daemonId (str): 守护进程的唯一标识符。

        **返回:**
        - list[DockerContainerItem]: 包含容器列表详情的 DockerContainerItem 模型的列表。
        """
        result = send(
            "GET",
            f"{ApiPool.IMAGE}/containers",
            params={
                "daemonId": daemonId,
            },
        )

        return [DockerContainerItem(**item) for item in result]

    def network(self, daemonId: str) -> list[DockerNetworkItem]:
        """
        获取网络接口列表

        **参数:**
        - daemonId (str): 守护进程的唯一标识符。

        **返回:**
        - list[DockerNetworkItem]: 包含网络接口列表详情的 DockerNetworkItem 模型的列表。
        """
        result = send(
            "GET",
            f"{ApiPool.IMAGE}/network",
            params={
                "daemonId": daemonId,
            },
        )
        return [DockerNetworkItem(**item) for item in result]

    def add(self, daemonId: str, dockerFile: str, name: str, tag: str) -> bool:
        """
        新增一个镜像

        **参数:**
        - daemonId (str): 守护进程的唯一标识符。
        - dockerFile (str): DockerFile Config
        - name (str): 镜像名称。
        - tag (str): 镜像版本。

        **返回:**
        - bool: 新增镜像成功后返回True。
        """
        return send(
            "POST",
            f"{ApiPool.IMAGE}/image",
            params={"daemonId": daemonId},
            data={"dockerFile": dockerFile, "name": name, "tag": tag},
        )

    def progress(self, daemonId: str) -> dict[str, int]:
        """
        获取镜像构建进度

        ## **由于文档此部分内容不详，未使用模型**

        **参数:**
        - daemonId (str): 守护进程的唯一标识符。

        **返回:**
        - dict[str, int]: 包含构建进度信息的字典。
        """
        return send(
            "GET",
            f"{ApiPool.IMAGE}/progress",
            params={"daemonId": daemonId},
        )
