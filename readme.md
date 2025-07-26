## ToNPiShock
This is a script for players of the VRChat game "Terrors of Nowhere" by Beyond, which allows using a PiShock with the game, allowing you to get physical feedback when you receive damage or die in that game.

This script works by reading the websocket API output from ChrisFeline's [ToNSaveManager](https://github.com/ChrisFeline/ToNSaveManager). 

This script is intended for use by consenting individuals only. Do not let anyone force you to run it if you do not wish to. Remember to read and follow all safety documentation on PiShock's website - do not place a PiShock shocker near your neck, head, or spine. Always know your limits and when to stop. Use of this script is at your own risk.

### Prerequisites
This script depends on [ToNSaveManager](https://github.com/ChrisFeline/ToNSaveManager) to read data from the game. Once you have ToNSaveManager installed and running, go into the settings and make sure the `WebSocket API` setting is enabled.

### Setup
#### Precompiled Version
Simply download the latest version from the releases page, unzip it, edit the config.json file, and double-click ToNPiShock.exe to run the script.

#### Running from Code
Clone this repository. Navigate to the folder and run `pip install -r requirements.txt` to install the prerequisite libraries. Edit the config.json file, and then run `python ToNPiShock.py` to start the script.

### Configuration File
| Name             | Value                      | Example                              | Description                                                                                      |
|------------------|----------------------------|--------------------------------------|--------------------------------------------------------------------------------------------------|
| pishock\_username | (Your PiShock username)    | ThistleBunny                         | Your PiShock username, from the [account](https://pishock.com/#/account) page.                   |
| pishock\_apikey   | (Your PiShock API key)     | 4c37f842-902a-4d12-a890-33c09831ac26 | Your PiShock API key, from the [account](https://pishock.com/#/account) page.                    |
| pishock\_code     | (Shocker share code)       | 8762147BE12                          | The "share code" for the shocker you want to control.                                            |
| vrchat\_username  | (Your VRChat username)     | ThistleBunny                         | Your VRChat username.                                                                            |
| action\_damage    | shock, vibrate, beep, none | vibrate                              | The action for the shocker to take when you receive damage.                                      |
| duration\_damage  | 1-15                       | 1                                    | How long the damage action should occur, in seconds.                                             |
| action\_death     | shock, vibrate, beep, none | shock                                | The action for the shocker to take when you die.                                                 |
| duration\_death   | 1-15                       | 2                                    | How long the death action should occur, in seconds.                                              |
| strength\_max     | 1-100                      | 50                                   | The maximum strength of shocks/vibrates. Everything is a percentage of this.                     |
| death\_delay      | any integer                | 3                                    | How long, in seconds, to delay the death action.                                                 |
| death\_roundend   | 0-1                        | 0                                    | Set to 0 for a death action to occur after death, 1 for the action to occur once the round ends. |

Make sure everything is surrounded by quotation marks.

To get your username and API key for the first two options, go to the [account](https://pishock.com/#/account) page on PiShock's control panel. The username is the first option. Click the "Generate API Key" to copy it.

To get a shocker share code, go to the [control](https://pishock.com/#/control) page for the PiShock. Click the share button, and then "+Code" to generate a share code. If you'd like to set limits (recommended), click the gear icon. Be sure that the duration_damage, duration_death, and strength_max options are all set at or below any limits you set on PiShock's website.

The action_damage and action_death values should always be lowercase. If they are not typed exactly as above, the script will skip these actions. 

The strength_max setting is the maximum power of shock/vibrate actions. Deaths will always be 100% of this value, while damage will be a percentage of this value. For example, if you set strength_max to 50, and then take 40% damage from a hit, you'd get 40% of 50%, meaning 20% of a shock/vibrate. If you die, you'll get a 50% shock/vibrate. 

The death_delay option is how many seconds after a death (or round-end) to wait before triggering the death action. This is useful if there's latency and people want to see you. Set to 0 to disable.

Setting death_roundend to 0 will cause the death_action to apply when you die in ToN. If you set it to 1, it will track if you die and then trigger the action once the round concludes. This is useful if you want the entire lobby to be present when the action happens. 