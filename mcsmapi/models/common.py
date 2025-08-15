from pydantic import BaseModel


class CpuMemChart(BaseModel):
    """节点资源使用率信息"""

    cpu: float
    """cpu使用率"""
    mem: float
    """内存使用率"""


class ProcessInfo(BaseModel):
    """节点进程详细信息"""

    cpu: int
    """远程节点使用的cpu资源(单位: byte)"""
    memory: int
    """远程节点使用的内存资源(单位: byte)"""
    cwd: str
    """远程节点的工作路径"""


class InstanceInfo(BaseModel):
    """实例统计信息"""

    running: int
    """运行中实例数量"""
    total: int
    """全部实例数量"""
