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
MinuteTMP = _SysGetDateTime_.second
MinuteTMPStr = str(MinuteTMP)
MinuteTMPLenght = len(MinuteTMPStr)
if MinuteTMPLenght == 1:
    _SysGetDateTime_minute = "0" + MinuteTMPStr
    pass
else:
    _SysGetDateTime_minute = MinuteTMPStr
    pass
HourTMP = _SysGetDateTime_.second
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
        pass
    else:
        _SysGetDateTime_day = "0" + DayTMPStr
        pass
    pass
else:
    if MonthTMPLenght == 1:
        _SysGetDateTime_day = DayTMPStr + " "
        pass
    else:
        _SysGetDateTime_day = DayTMPStr
        pass
    pass
_SysGetDateTimeFormat_ = f"{_SysGetDateTime_.year}-{_SysGetDateTime_month}-{_SysGetDateTime_day} {_SysGetDateTime_hour}:{_SysGetDateTime_minute}:{_SysGetDateTime_second}"

def __PlutoSecuritySystem__():
    
    
    
    
    # get the security system working, someday
    
    
    
    pass

def __SysReport__(ReportType, ReportLogFile, ReportMsgLog, ReportCode, ReportMsgUser):
    # Report Types: Error, ErrorUsr, Warn, WarnUsr, Info, InfoUsr
    if ReportType == "Error":
        with open(ReportLogFile, 'a') as ReportLog:
            ReportLog.write(f"\n [RUN ID: {_RunID_}]: [ERROR: {ReportCode}] @ [{_SysGetDateTimeFormat_}] {ReportMsgLog}")
        exit()
    elif ReportType == "ErrorUsr":
        with open(ReportLogFile, 'a') as ReportLog:
            ReportLog.write(f"\n [RUN ID: {_RunID_}]: [ERROR: {ReportCode}] @ [{_SysGetDateTimeFormat_}] {ReportMsgLog}")
        __ConsoleWrtiteline__(f" [ERROR: {ReportCode}] {ReportMsgUser}")
        exit()
    elif ReportType == "Warn":
        if ReportCode == "":
            with open(ReportLogFile, 'a') as ReportLog:
                ReportLog.write(f"\n [RUN ID: {_RunID_}]: [WARN         ] @ [{_SysGetDateTimeFormat_}] {ReportMsgLog}")
        else:
            with open(ReportLogFile, 'a') as ReportLog:
                ReportLog.write(f"\n [RUN ID: {_RunID_}]: [WARN:  {ReportCode}] @ [{_SysGetDateTimeFormat_}] {ReportMsgLog}")
    elif ReportType == "WarnUsr":
        if ReportCode == "":
            with open(ReportLogFile, 'a') as ReportLog:
                ReportLog.write(f"\n [RUN ID: {_RunID_}]: [WARN         ] @ [{_SysGetDateTimeFormat_}] {ReportMsgLog}")
            __ConsoleWrtiteline__(f" [WARN         ] {ReportMsgUser}")
        else:
            with open(ReportLogFile, 'a') as ReportLog:
                ReportLog.write(f"\n [RUN ID: {_RunID_}]: [WARN:  {ReportCode}] @ [{_SysGetDateTimeFormat_}] {ReportMsgLog}")
            __ConsoleWrtiteline__(f" [WARN:  {ReportCode}] {ReportMsgUser}")
    elif ReportType == "Info":
        with open(ReportLogFile, 'a') as ReportLog:
                ReportLog.write(f"\n [RUN ID: {_RunID_}]: [INFO:  {ReportCode}] @ [{_SysGetDateTimeFormat_}] {ReportMsgLog}")
    elif ReportType == "InfoUsr":
        with open(ReportLogFile, 'a') as ReportLog:
                ReportLog.write(f"\n [RUN ID: {_RunID_}]: [INFO:  {ReportCode}] @ [{_SysGetDateTimeFormat_}] {ReportMsgLog}")
        __ConsoleWrtiteline__(f" [INFO: {ReportCode}] {ReportMsgUser}")
        pass



# __SysReport__("ErrorUsr", __SysPlutoControl__.PlutoLogFile, __SysPlutoControl__.ES0x0000, "0x0000", __SysPlutoControl__.EU0x0000)
# __SysReport__("")
# try:
#     if __SysPlatformSetting__() == "Windows":
#         pass
#     else:
#         __SysReportError__("0x0022", __SysPlutoControl__.PlutoLogFile, __SysPlutoControl__.E0x0022 % (__SysPlutoControl__.PlutoSysNameSM, __SysPlatformSetting__()))
# except:
#     __SysReportError__("0x0022", __SysPlutoControl__.PlutoLogFile, __SysPlutoControl__.E0x0022 % (__SysPlutoControl__.PlutoSysNameSM, __SysPlatformSetting__()))


# __SysReportLEGACY__("PASSED", __SysPlutoControl__.PlutoLogFile, __SysPlutoControl__.PlutoPassedMsg % __SysPathControl__.basename(__file__))

##
#
#     if __SysPlatformSetting__() == "Windows":
#         if __SysPlatformRelease__ == "10" or __SysPlatformRelease__ == "post2022":
#             pass
#         elif __SysPlatformRelease__ == "8":
#             __SysReportError__("0x0012", __SysPlutoControl__.PlutoLogFile, __SysPlutoControl__.E0x0012 % (__SysPlatformSetting__(), __SysPlutoControl__.PlutoSysNameSM, __SysPlatformSetting__()))
#         else:
#            
#     else:
#         __SysReportError__("0x0014", __SysPlutoControl__.PlutoLogFile, __SysPlutoControl__.E0x0014 % (__SysPlatformSetting__(), __SysPlutoControl__.PlutoSysNameSM))
#
#     
