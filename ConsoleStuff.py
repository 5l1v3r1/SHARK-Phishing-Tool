import requests
import os
import time
import platform
import coloredlogs
import logging

logger = logging.getLogger(__name__)
fmt = ("[%(asctime)s] %(message)s")
coloredlogs.install(fmt=fmt, logger=logger)

def Banner():
	banner = ["\r", "      ,|\r", "     / ;\r", "    /  \\\r", "   : ,'(\r", "   |( `.\\\r", "   : \\  `\\       \\.\r", "    \\ `.         | `.\r", "     \\  `-._     ;   \\\r", "      \\     ``-.'.. _ `._\r", "       `. `-.            ```-...__\r", "        .'`.        --..          ``-..____\r", "      ,'.-'`,_-._            ((((   <o.   ,'\r", "           `' `-.)``-._-...__````  ____.-'\r", "               ,'    _,'.--,---------'\r", "           _.-' _..-'   ),'\r", "          ``--''        `\r", "   \tProject S.H.A.R.K by Sheepy\n\n"]
	for line in banner:
		print(line)
		time.sleep(0.03)

def GetOSType():
	return platform.system()

def Clear():
	if GetOSType() == "Linux":
		os.system('clear')
	else:
		os.system('cls')

def Startup():
	logger.info(f"Detected os type [{GetOSType()}]")
	logger.info(f"Starting...")
	Clear()
	Banner()

	

