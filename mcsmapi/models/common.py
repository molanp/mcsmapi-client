from pydantic import BaseModel


class CpuMemChart(BaseModel):
    """资源使用率信息"""

    cpu: float
    """cpu使用率"""
    mem: float
    """内存使用率"""


class ProcessInfo(BaseModel):
    """进程详细信息"""

    cpu: int
    """CPU 使用率（百分比）"""
    memory: int
    """内存使用量（MB）"""
    cwd: str
    """工作路径"""


class InstanceInfo(BaseModel):
    """实例统计信息"""

    running: int
    """运行中实例数量"""
    total: int
    """全部实例数量"""
