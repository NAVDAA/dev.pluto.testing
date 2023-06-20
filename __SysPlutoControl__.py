"""
Default PLUTO configuration.
Editing may cause problems!
"""
import random as __SysRandomizer__
_RunID_ = __SysRandomizer__.randint(10000, 99999)


# Pluto
PlutoAuthorSM = "NAVDAA"
PlutoAuthorBG = "NAVDAA Software"
PlutoSysNameSM = "Pluto"
PlutoSysNameBG = "Codename Pluto"
PlutoCodename = "sys.pluto-dev_init"
PlutoPythonPath = ".\\sys.pluto-python_NEW\\python.exe"
PlutoPipPath = ".\\sys.pluto-python_NEW\\python.exe -m pip"
PlutoLogFile = ".\\com.pluto.init.log"
PlutoLogFileV2 = ".\\com.pluto-init.log"
PlutoPID = "2365"
PlutoVer = "0.0.0.2-PreALPHA"
PlutoArchitectureSupported = "64" # 64 = 64-bit; 32 = 32-bit; ARM = 32-bit ARM; ARM64 = 64-bit ARM64
PlutoCopyright = "Copyright (c) %s by %s. All rights reserved."

# Errors
EU0x0000 = "This is a \"0\" bug report. Used for testing only."
ES0x0000 = "ERROR USED FOR TESTING ONLY! PROGRAM RETURNED \'0\'!"

EU0x0012 = "This version of %s is not compatible with %s. Consider upgrading your %s version." # 1st %s == 3rd %s
ES0x0012 = "THIS VERION OF %s IS NOT SUPPORTED BY %s! PROGRAM RETURNED \'0\'!"

EU0x0014 = "%s is not compatible with %s."
ES0x0014 = "%s IS NOT COMPATIBLE WITH %s! PROGRAM RETURNED \'0\'!"

EU0x0022 = "%s is not able to determine your %s version. Unable to continue."
ES0x0022 = "%s IS NOT ABLE TO DETERMINE %s VERSION! PROGRAM RETURNED \'0\'!"

EU0x0023 = "Error while importing %s!"
ES0x0023 = "IMPORT ERROR WITH %s! PROGRAM RETURNED \'0\'!"

EU0x6969 = "%s passed without errors, but still returned %s?"
ES0x6969 = "%s PASSED WITHOUT ERRORS! PROGRAM RETURNED %s! ERROR??"

IU0x0001 = "%s passed without errors."
IS0x0001 = "%s RETURNED \'1\'! NO ERRORS DETECTED!"