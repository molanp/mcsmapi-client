from typing import List, Optional, Union
from pydantic import BaseModel


class DockerConfig(BaseModel):
    containerName: str = ""
    image: str = "mcsm-ubuntu:22.04"
    memory: int = 1024  # in MB
    ports: List[str] = ["25565:25565/tcp"]
    extraVolumes: List[str] = []
    maxSpace: Optional[int] = None
    network: Optional[Union[str, int]] = None
    io: Optional[Union[str, int]] = None
    networkMode: str = "bridge"
    networkAliases: List[str] = []
    cpusetCpus: str = ""
    cpuUsage: int = 100
    workingDir: str = ""
    env: List[str] = []


class DockerImageItem(BaseModel):
    Id: str = ""
    ParentId: str = ""
    RepoTags: List[str] = []
    RepoDigests: List[str] = []
    Created: int = 0
    Size: int = 0
    VirtualSize: int = 0
    SharedSize: int = 0
    Labels: dict[str, str] = {}
    Containers: int = 0


class DockerContainerItemPort(BaseModel):
    PrivatePort: int = 0
    PublicPort: Optional[int] = None
    Type: str = ""


class DockerContainerItemNetworkSettingsNetwork(BaseModel):
    NetworkID: str = ""
    EndpointID: str = ""
    Gateway: str = ""
    IPAddress: str = ""
    IPPrefixLen: int = 0
    IPv6Gateway: str = ""
    GlobalIPv6Address: str = ""
    GlobalIPv6PrefixLen: int = 0
    MacAddress: str = ""


class DockerContainerItemNetworkSettings(BaseModel):
    Networks: dict[str, DockerContainerItemNetworkSettingsNetwork] = {}


class DockerContainerItemMount(BaseModel):
    Name: str = ""
    Source: str = ""
    Destination: str = ""
    Driver: str = ""
    Mode: str = ""
    RW: bool = False
    Propagation: str = ""


class DockerContainerItemHostConfig(BaseModel):
    NetworkMode: str = ""


class DockerContainerItem(BaseModel):
    Id: str = ""
    Names: List[str] = []
    Image: str = ""
    ImageID: str = ""
    Command: str = ""
    Created: int = 0
    State: str = ""
    Status: str = ""
    Ports: List[DockerContainerItemPort] = []
    Labels: dict[str, str] = {}
    SizeRw: int = 0
    SizeRootFs: int = 0
    HostConfig: DockerContainerItemHostConfig = DockerContainerItemHostConfig()
    NetworkSettings: DockerContainerItemNetworkSettings = (
        DockerContainerItemNetworkSettings()
    )
    Mounts: List[DockerContainerItemMount] = []


class DockerNetworkItemIPAMConfig(BaseModel):
    Subnet: str = ""


class DockerNetworkItemIPAM(BaseModel):
    Driver: str = ""
    Config: List[DockerNetworkItemIPAMConfig] = []


class DockerNetworkItem(BaseModel):
    Name: str = ""
    Id: str = ""
    Created: str = ""
    Scope: str = ""
    Driver: str = ""
    EnableIPv6: bool = False
    Internal: bool = False
    Attachable: bool = False
    Ingress: bool = False
    IPAM: DockerNetworkItemIPAM = DockerNetworkItemIPAM()
    Options: dict[str, str]
    Containers: Optional[dict[str, dict]] = {}
