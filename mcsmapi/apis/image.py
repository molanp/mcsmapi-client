from mcsmapi.pool import ApiPool
from mcsmapi.request import send
from mcsmapi.models.image import DockerImageItem, DockerContainerItem, DockerNetworkItem


class Image:
    @staticmethod
    def images(daemonId: str) -> list[DockerImageItem]:
        """
        获取镜像列表

        :params daemonId: 节点的UUID

        :returns: 包含镜像列表详情的 ImageModel 模型的列表
        """
        result = send(
            "GET",
            f"{ApiPool.IMAGE}/image",
            params={
                "daemonId": daemonId,
            },
        )

        return [DockerImageItem(**item) for item in result]

    @staticmethod
    def containers(daemonId: str) -> list[DockerContainerItem]:
        """
        获取容器列表

        :params daemonId: 节点的UUID

        :params: 包含容器列表详情的 DockerContainerItem 模型的列表
        """
        result = send(
            "GET",
            f"{ApiPool.IMAGE}/containers",
            params={
                "daemonId": daemonId,
            },
        )

        return [DockerContainerItem(**item) for item in result]

    @staticmethod
    def network(daemonId: str) -> list[DockerNetworkItem]:
        """
        获取网络接口列表

        :params daemonId: 节点的UUID

        :returns: 包含网络接口列表详情的 DockerNetworkItem 模型的列表
        """
        result = send(
            "GET",
            f"{ApiPool.IMAGE}/network",
            params={
                "daemonId": daemonId,
            },
        )
        return [DockerNetworkItem(**item) for item in result]

    @staticmethod
    def add(daemonId: str, dockerFile: str, name: str, tag: str) -> bool:
        """
        新增一个镜像

        :params daemonId: 节点的UUID
        :params dockerFile: DockerFile Config 内容
        :params name: 镜像名称
        :params tag: 镜像版本

        :returns: 新增镜像成功后返回True
        """
        return send(
            "POST",
            f"{ApiPool.IMAGE}/image",
            params={"daemonId": daemonId},
            data={"dockerFile": dockerFile, "name": name, "tag": tag},
        )

    @staticmethod
    def progress(daemonId: str) -> dict[str, int]:
        """
        获取镜像构建进度

        :params daemonId: 节点的UUID

        :returns: {容器名称: 当前状态}

        状态码对照:
        ```
        -1: 镜像构建失败
         1: 镜像构建中
         2: 镜像构建完成
        """
        return send(
            "GET",
            f"{ApiPool.IMAGE}/progress",
            params={"daemonId": daemonId},
        )
