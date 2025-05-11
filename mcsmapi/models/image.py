from typing import List, Optional, Union
from pydantic import BaseModel


class DockerConfig(BaseModel):
    """容器配置"""

    """容器名称"""
    containerName: str = ""
    """镜像名称"""
    image: str = ""
    """容器分配内存(单位: MB)"""
    memory: int = 0  # in MB
    """容器端口映射"""
    ports: List[str] = []  # ["25565:25565/tcp"]
    """额外挂载卷路径"""
    extraVolumes: List[str] = []
    """容器可使用的最大磁盘空间(单位: MB)"""
    maxSpace: Optional[int] = None
    """网络配置，可以是网络名称或ID"""
    network: Optional[Union[str, int]] = None
    """容器的 IO 限制"""
    io: Optional[Union[str, int]] = None
    """网络模式(例如: bridge, host)"""
    networkMode: str = "bridge"
    """网络别名列表"""
    networkAliases: List[str] = []
    """绑定的 CPU 核心"""
    cpusetCpus: str = ""  # 例如 `0,1`
    """CPU 使用率(单位: %)"""
    cpuUsage: int = 100
    """工作目录"""
    workingDir: str = ""
    """环境变量设置"""
    env: List[str] = []


class DockerImageItem(BaseModel):
    """Docker 镜像信息"""

    """镜像唯一 ID"""
    Id: str = ""
    """父镜像 ID"""
    ParentId: str = ""
    """镜像仓库标签"""
    RepoTags: List[str] = []  # 例如 ["ubuntu:latest"]
    """镜像摘要"""
    RepoDigests: List[str] = []
    """镜像创建时间(Unix 时间戳)"""
    Created: int = 0
    """镜像大小(单位: 字节)"""
    Size: int = 0
    """镜像的虚拟大小"""
    VirtualSize: int = 0
    """共享存储空间大小"""
    SharedSize: int = 0
    """镜像标签"""
    Labels: dict[str, str] = {}
    """依赖该镜像运行的容器数量"""
    Containers: int = 0


class DockerContainerItemPort(BaseModel):
    """Docker 容器端口映射"""

    """容器内部端口"""
    PrivatePort: int = 0
    """映射到宿主机的端口"""
    PublicPort: Optional[int] = None
    """端口类型(tcp/udp)"""
    Type: str = ""


class DockerContainerItemNetworkSettingsNetwork(BaseModel):
    """Docker 容器网络设置信息"""

    """网络 ID"""
    NetworkID: str = ""
    """网络端点 ID"""
    EndpointID: str = ""
    """网关地址"""
    Gateway: str = ""
    """分配的 IP 地址"""
    IPAddress: str = ""
    """IP 地址前缀长度"""
    IPPrefixLen: int = 0
    """IPv6 网关地址"""
    IPv6Gateway: str = ""
    """IPv6 地址"""
    GlobalIPv6Address: str = ""
    """IPv6 地址前缀长度"""
    GlobalIPv6PrefixLen: int = 0
    """MAC 地址"""
    MacAddress: str = ""


class DockerContainerItemNetworkSettings(BaseModel):
    """Docker 容器的网络配置信息"""

    """容器连接的所有网络"""
    Networks: dict[str, DockerContainerItemNetworkSettingsNetwork] = {}


class DockerContainerItemMount(BaseModel):
    """容器挂载点信息"""

    """挂载名称"""
    Name: str = ""
    """源路径"""
    Source: str = ""
    """目标路径"""
    Destination: str = ""
    """驱动类型"""
    Driver: str = ""
    """挂载模式"""
    Mode: str = ""
    """是否允许读写"""
    RW: bool = False
    """传播模式"""
    Propagation: str = ""


class DockerContainerItemHostConfig(BaseModel):
    """Docker 宿主机配置"""

    """网络模式"""
    NetworkMode: str = ""


class DockerContainerItem(BaseModel):
    """Docker 容器详细信息"""

    """容器 ID"""
    Id: str = ""
    """容器名称列表"""
    Names: List[str] = []
    """运行的镜像名称"""
    Image: str = ""
    """镜像 ID"""
    ImageID: str = ""
    """容器启动命令"""
    Command: str = ""
    """容器创建时间(Unix 时间戳)"""
    Created: int = 0
    """容器状态"""
    State: str = ""
    """容器运行状态描述"""
    Status: str = ""
    """端口映射信息"""
    Ports: List[DockerContainerItemPort] = []
    """容器标签信息"""
    Labels: dict[str, str] = {}
    """读写层大小(单位: 字节)"""
    SizeRw: int = 0
    """根文件系统大小(单位: 字节)"""
    SizeRootFs: int = 0
    """宿主机配置"""
    HostConfig: DockerContainerItemHostConfig = DockerContainerItemHostConfig()
    """容器网络配置"""
    NetworkSettings: DockerContainerItemNetworkSettings = DockerContainerItemNetworkSettings()
    """容器挂载信息"""
    Mounts: List[DockerContainerItemMount] = []


class DockerNetworkItemIPAMConfig(BaseModel):
    """Docker 网络 IPAM 配置信息"""

    """子网地址"""
    Subnet: str = ""


class DockerNetworkItemIPAM(BaseModel):
    """Docker 网络的 IP 地址管理"""

    """驱动类型"""
    Driver: str = ""
    """IPAM 配置"""
    Config: List[DockerNetworkItemIPAMConfig] = []


class DockerNetworkItem(BaseModel):
    """Docker 网络详细信息"""

    """网络名称"""
    Name: str = ""
    """网络 ID"""
    Id: str = ""
    """网络创建时间"""
    Created: str = ""
    """网络作用范围(local/global)"""
    Scope: str = ""
    """网络驱动类型"""
    Driver: str = ""
    """是否启用 IPv6"""
    EnableIPv6: bool = False
    """是否为内部网络"""
    Internal: bool = False
    """是否可附加"""
    Attachable: bool = False
    """是否为入口网络"""
    Ingress: bool = False
    """IPAM 配置信息"""
    IPAM: DockerNetworkItemIPAM = DockerNetworkItemIPAM()
    """网络选项"""
    Options: dict[str, str] = {}
    """连接到此网络的容器信息"""
    Containers: Optional[dict[str, dict]] = {}