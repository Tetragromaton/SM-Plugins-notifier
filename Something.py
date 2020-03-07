from listeners import OnServerOutput
from core import OutputReturn
from commands.typed import TypedClientCommand
from players._base import *
from messages import SayText2
from messages import *
from commands.client import ClientCommand
from commands.typed import TypedServerCommand
from commands.typed import filter_str
from commands.say import SayCommand
from weapons.entity import Weapon
from weapons import *
from config.manager import ConfigManager


@ClientCommand('sm')
def ShowExceptionStreak(command_info, pindex):
    client = Player(pindex)
    gg = 420
    if "sm plugins" in command_info.command_string:
        name = client.name
        sid = client.steamid
        print("[SM PLUGINS] This player listed plugins: " + name + ' ' + sid)
