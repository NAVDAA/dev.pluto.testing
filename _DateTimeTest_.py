import datetime as __SysDateControl__
# [...inny kod tutaj]
_SysGetDateTime_ = __SysDateControl__.datetime.now()
# [...inny kod tutaj]
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
print(_SysGetDateTimeFormat_)
