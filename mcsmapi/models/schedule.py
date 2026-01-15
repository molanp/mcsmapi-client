from enum import Enum, IntEnum
from pydantic import BaseModel


class ScheduleActionType(Enum):
    """计划任务动作"""

    COMMAND = "command"
    """发送命令"""
    DELAY = "delay"
    """等待x秒"""
    STOP = "stop"
    """停止实例"""
    START = "start"
    """启动实例"""
    RESTART = "restart"
    """重启实例"""
    KILL = "kill"
    """强制停止实例"""


class ScheduleType(IntEnum):
    """计划任务类型"""

    INTERVAL = 1
    """间隔时间任务"""
    CYCLE = 2
    """周期时间任务"""
    SPECIFY = 3
    """指定时间任务"""


class ScheduleAction(BaseModel):
    """计划任务动作"""

    type: ScheduleActionType
    """动作类型"""
    payload: str
    """动作参数"""


class SchedulePostBody(BaseModel):
    """计划任务配置参数"""

    name: str
    """计划任务名称"""
    count: int
    """执行次数, -1表无限"""
    time: str
    """除了间隔时间任务是间隔秒数，其他都是rcon字符串"""
    actions: list[ScheduleAction]
    """计划任务动作链"""
    type: ScheduleType


class ScheduleDetail(SchedulePostBody):
    """计划任务信息"""

    instanceUuid: str
    """实例uuid"""
    daemonId: str
    """节点id"""

    def delete(self):
        """删除计划任务"""
        from mcsmapi.apis.schedule import Schedule

        return Schedule.delete(self.daemonId, self.instanceUuid, self.name)

    def update(self, config: SchedulePostBody):
        """
        更新计划任务

        :param config: 计划任务配置

        :returns: 是否成功
        """
        from mcsmapi.apis.schedule import Schedule

        return Schedule.update(self.daemonId, self.instanceUuid, config)
