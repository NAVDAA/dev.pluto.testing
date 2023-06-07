"""
Default PLUTO configuration.
Editing may cause problems!
"""

PlutoSysNameSM = "Pluto"
PlutoSysNameBG = "Codename Pluto"
PlutoCodename = "sys.pluto-dev_init"
PlutoPythonPath = ".\\sys.pluto.python\\python.exe"
PlutoLogFile = ".\\com.pluto.init.log"

SysBootloaderModulesInital = ["os", "time", "random", "platform", "datetime", "argparse"]

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