import websocket
import _thread
import time
import rel
import json
import requests

config = json.load(open("config.json"))
pishock_username = config["pishock_username"]
pishock_apikey = config["pishock_apikey"]
pishock_code = config["pishock_code"]
vrchat_username = config["vrchat_username"]
action_damage = config["action_damage"]
duration_damage = config["duration_damage"]
action_death = config["action_death"]
duration_death = config["duration_death"]
strength_max = config["strength_max"]
death_delay = int(config["death_delay"])
death_roundend = bool(int(config["death_roundend"]))

roundend_shock = False

def shock(shock_strength,shock_action,shock_duration):
    match shock_action:
        case "shock":
            shock_op = "0"
        case "vibrate":
            shock_op = "1"
        case "beep":
            shock_op = "2"
        case _:
            return
    shock_strength = round((int(strength_max)/100)*int(shock_strength))
    api_url = "https://do.pishock.com/api/apioperate"
    api_data = {
        "Username" : pishock_username,
        "Apikey" : pishock_apikey,
        "Name" : "ToNPiShock",
        "Code" : pishock_code,
        "Intensity" : shock_strength,
        "Duration" : shock_duration,
        "Op" : shock_op
    }
    api_headers = {
        "Content-type" : "application/json"
    }
    print("Delivering " + shock_action + " at " + str(shock_strength) + "% for " + shock_duration + " seconds")
    requests.post(api_url, data=json.dumps(api_data), headers=api_headers)

def on_message(ws, message):
    global roundend_shock
    payload = json.loads(message)
    payload_type = payload["Type"]

    if payload_type == "DAMAGED":
        print("Damage received: " + str(payload['Value']) + "%")
        if payload["Value"] > 100:
            payload_value = str(100)
        else:
            payload_value = str(payload['Value'])
        shock(payload_value,action_damage,duration_damage)
    elif payload_type == "DEATH":
        if payload["Name"] == vrchat_username:
            print("Died")
            if death_roundend == True:
                print("Waiting for round to end before taking action")
                roundend_shock = True
            else:
                if death_delay != 0:
                    time.sleep(death_delay)
                shock("100",action_death,duration_death)
    elif (payload_type == "STATS") and (payload["Name"] == "IsStarted") and (payload["Value"] == True):
        print("Round has started")
    elif (payload_type == "STATS") and (payload["Name"] == "IsStarted") and (payload["Value"] == False):
        print("Round is not active")
        if (death_roundend == True) and (roundend_shock == True):
            roundend_shock = False
            if death_delay != 0:
                time.sleep(death_delay)
                shock("100",action_death,duration_death)

def on_error(ws, error):
    print("Error: " + error)

def on_close(ws, close_status_code, close_msg):
    print("Failed to communicate with ToNSaveManager.")
    print("Please ensure TonSaveManager is running and that the Websocket API is enabled in settings.")
    print("Afterwards, please restart this script.")
    input("Press Enter to continue")
    quit()

def on_open(ws):
    print("*********************************************************************")
    print("** Terrors of Nowhere PiShock-Based Immersion Enhancement Script")
    print("** Version Beta-2")
    print("** By ThistleBunny")
    print("**")
    print("** Remember: Always know your limits and follow the safety")
    print("** information on PiShock's Website. Never put a shocker on")
    print("** your head, neck, or near your spine.")
    print("**")
    print("** This script is for use by consenting individuals only. Do not")
    print("** let someone force you to use it if you don't wish to.")
    print("*********************************************************************")
    print("Connected to ToNSaveManager")

if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("ws://localhost:11398",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever(dispatcher=rel, reconnect=5)
    rel.signal(2, rel.abort)
    rel.dispatch()