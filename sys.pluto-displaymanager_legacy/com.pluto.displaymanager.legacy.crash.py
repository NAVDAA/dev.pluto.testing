import __SysPlutoControl__
import json as _Json_
from os import system as __SysCommandControl__
from os import path as __SysPathControl__
from time import sleep as __SysSleepSec__
from platform import system as __SysPlatformSetting__
from platform import release as __SysPlatformRelease__
import os as __SysControl__
import time as __SysTimeControl__
import platform as __SysPlatformControl__
import datetime as __SysDateControl__
import random as __SysRandomizer__
from argparse import ArgumentParser as __SysArgumentParser__
import argparse as __SysArgumentControl__
_RunID_ = __SysRandomizer__.randint(10000, 99999)
_SysGetDateTime_ = __SysDateControl__.datetime.now()
__ConsoleWrtiteline__ = print
__GetUserInputData__ = input
SecTMP = _SysGetDateTime_.second
SecTMPStr = str(SecTMP)
SecTMPLenght = len(SecTMPStr)
if SecTMPLenght == 1:
    _SysGetDateTime_second = "0" + SecTMPStr
    pass
else:
    _SysGetDateTime_second = SecTMPStr
    pass
MinuteTMP = _SysGetDateTime_.minute
MinuteTMPStr = str(MinuteTMP)
MinuteTMPLenght = len(MinuteTMPStr)
if MinuteTMPLenght == 1:
    _SysGetDateTime_minute = "0" + MinuteTMPStr
    pass
else:
    _SysGetDateTime_minute = MinuteTMPStr
    pass
HourTMP = _SysGetDateTime_.hour
HourTMPStr = str(HourTMP)
HourTMPLenght = len(HourTMPStr)
if HourTMPLenght == 1:
    _SysGetDateTime_hour = "0" + HourTMPStr
    pass
else:
    _SysGetDateTime_hour = HourTMPStr
    pass
MonthTMP = _SysGetDateTime_.month
MonthTMPStr = str(MonthTMP)
MonthTMPLenght = len(MonthTMPStr)
_SysGetDateTime_month = MonthTMPStr
DayTMP = _SysGetDateTime_.day
DayTMPStr = str(DayTMP)
DayTMPLenght = len(DayTMPStr)
if DayTMPLenght == 1:
    if MonthTMPLenght == 1:
        _SysGetDateTime_day = "0" + DayTMPStr + " "
        _SysGetDateTime_month = "0" + MonthTMPStr
        pass
    else:
        _SysGetDateTime_day = "0" + DayTMPStr
        pass
    pass
else:
    if MonthTMPLenght == 1:
        _SysGetDateTime_day = DayTMPStr + " "
        _SysGetDateTime_month = "0" + MonthTMPStr
        pass
    else:
        _SysGetDateTime_day = DayTMPStr
        pass
    pass
_SysGetDateTimeFormat_ = f"{_SysGetDateTime_.year}-{_SysGetDateTime_month}-{_SysGetDateTime_day} {_SysGetDateTime_hour}:{_SysGetDateTime_minute}:{_SysGetDateTime_second}"