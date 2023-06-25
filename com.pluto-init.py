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
from argparse import ArgumentParser as __SysArgumentParser__
import argparse as __SysArgumentControl__
import shutil as __SysFileControl__
import random as __SysRandomizer__
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

def __PlutoSecuritySystem__():
    pass # get the security system working, someday

terminal_size = __SysFileControl__.get_terminal_size()
_TerminalWidth_ = terminal_size.columns
_TerminalHeight_ = terminal_size.lines

def __SysReport__(ReportType, ReportLogFile, ReportMsgLog, ReportMsgUser, ReportCode="0x????"):
    """PLUTO Report System.

    Args:
        ReportType (str): Type of Report, Error, ErrorUsr, Warn, WarnUsr, Info, InfoUsr.
        ReportLogFile (str): Provide log file path here. exaple: __SysPlutoControl__.PlutoLogFile.
        ReportMsgLog (str): String printed to log file.
        ReportMsgUser (str): String printed to user console.
        ReportCode (str, optional): Report code, included in log and user console. Defaults to "0x????".
    """
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
        with open(ReportLogFile, 'a') as ReportLog:
            ReportLog.write(f"\n [RUN ID: {_RunID_}]: [WARN:  {ReportCode}] @ [{_SysGetDateTimeFormat_}] {ReportMsgLog}")
    elif ReportType == "WarnUsr":
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

def __SysReport__V2(ReportType, ReportLogFile, ReportMsgLog, ReportMsgUser, ReportCode="0x????"):
    """
    `V2 - Rewrite needed.`
    """

    pass

def _WriteLineLogo_(LogoSize="2", LogoNumber=1):
    if LogoSize == "2" and LogoNumber == 1:
        __ConsoleWrtiteline__(
            "███ █   █ █ ▀█▀ ███",
            "\n█   █▄▄ █▄█  █  ███")
    elif LogoSize == "2" and LogoNumber == 2:
        __ConsoleWrtiteline__(
            "█▀ █ ▄▀▄ █ █ ██▄ ▄▀▄",
            "\n█ ▄█ █ █ ▀▄▀ ██▀ █ █")

def __PlutoImportJSON__(format, url=None, file=None):
    if format == "pluto":
        if url is None and file is not None:
            with open(file, "r") as File:
                _JSON_Import_ = _Json_.load(File)
            
            __ConsoleWrtiteline__(f"TMP LOADING JSON")
            if _JSON_Import_["SysPluto"][0]["AppOrServerValue"][0]["IsApp"] == "True" and _JSON_Import_["SysPluto"][0]["AppOrServerValue"][0]["IsServer"] == "False":
                
                pass
            elif _JSON_Import_["SysPluto"][0]["AppOrServerValue"][0]["IsApp"] == "False" and _JSON_Import_["SysPluto"][0]["AppOrServerValue"][0]["IsServer"] == "True":

                pass
            elif _JSON_Import_["SysPluto"][0]["AppOrServerValue"][0]["IsApp"] == "True" and _JSON_Import_["SysPluto"][0]["AppOrServerValue"][0]["IsServer"] == "True":
                __SysReport__("ErrorUsr",
                              __SysPlutoControl__.PlutoLogFile,
                              __SysPlutoControl__.ES0x0023 % (_JSON_Import_["SysPluto"][0]["DisplayValue"][0]["Title"].upper().replace(" ", "-")),
                              __SysPlutoControl__.EU0x0023 % (_JSON_Import_["SysPluto"][0]["DisplayValue"][0]["Title"]),
                              "0x0023")
                exit()
            pass
    
    
    pass

def __PlutoImportJSON__V2(format, url=None, file=None):
    
    pass

def __SysTermCheck__():
    
    
    
    pass

def __SysPlatformCheck__():
    
    
    
    pass

def __SysArchitectureCheck__():
    
    
    
    
    pass

def _SysPlutoRun_(FileName, Attribute1=""):
    __SysCommandControl__(f"{__SysPlutoControl__.PlutoPythonPath} {Attribute1} {FileName}")
    pass

def ___SysPlutoINIT___(IsCapitalized=True):
    if IsCapitalized == True:
        __ConsoleWrtiteline__(f"\n %s (Codename: %s); Version [%s]." % (__SysPlutoControl__.PlutoSysNameSM, __SysPlutoControl__.PlutoCodename, __SysPlutoControl__.PlutoVer), f"\n Pip executeable: [%s]" % __SysPlutoControl__.PlutoPipPath, f"Python executeable: [%s]" % __SysPlutoControl__.PlutoPythonPath, f"\n\n %s\n\n" % __SysPlutoControl__.PlutoCopyright % ("2023", __SysPlutoControl__.PlutoAuthorBG))
    elif IsCapitalized == False:
        __ConsoleWrtiteline__(f"\n %s (Codename: %s); Version [%s]." % (__SysPlutoControl__.PlutoSysNameSM, __SysPlutoControl__.PlutoCodename, __SysPlutoControl__.PlutoVer), f"\n Pip executeable: [%s]" % __SysPlutoControl__.PlutoPipPath, f"Python executeable: [%s]" % __SysPlutoControl__.PlutoPythonPath, f"\n\n %s\n\n" % __SysPlutoControl__.PlutoCopyright % ("2023", __SysPlutoControl__.PlutoAuthorBG))
    else:
        __ConsoleWrtiteline__(f"\n %s (Codename: %s); Version [%s]." % (__SysPlutoControl__.PlutoSysNameSM, __SysPlutoControl__.PlutoCodename, __SysPlutoControl__.PlutoVer), f"\n Pip executeable: [%s]" % __SysPlutoControl__.PlutoPipPath, f"Python executeable: [%s]" % __SysPlutoControl__.PlutoPythonPath, f"\n\n %s\n\n" % __SysPlutoControl__.PlutoCopyright % ("2023", __SysPlutoControl__.PlutoAuthorBG))
    pass

___SysPlutoINIT___()

################################################################
    

__SysReport__("InfoUsr",
              __SysPlutoControl__.PlutoLogFile,
              __SysPlutoControl__.IS0x0001 % (__SysPlutoControl__.PlutoCodename.upper()),
              __SysPlutoControl__.IU0x0001 % (__SysPlutoControl__.PlutoCodename),
              "0x0001")