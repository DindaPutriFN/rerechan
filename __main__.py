from rerechan import *
from importlib import import_module
from rerechan.modules import ALL_MODULES
for module_name in ALL_MODULES:
        imported_module = import_module("rerechan.modules." + module_name)
bot.run_until_disconnected()

usr.local.bin

