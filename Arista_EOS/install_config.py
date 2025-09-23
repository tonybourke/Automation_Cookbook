# This method doesn't use PyeAPI

import requests
import json
import uuid
import urllib3
urllib3.disable_warnings()

username = "arista"
password = "0la430sqf5jk8uk6"
device = "leaf1"

url = f"https://{device}/command-api"
cs_id = uuid.uuid4()

file_handler = open("leaf1.cfg", "r")
new_config = file_handler.read()
json_payload = {
        "jsonrpc": "2.0",
        "method": "runCmds",
        "params": {
            "version": 1,
            "cmds": [
                {
                    "cmd": "enable"
                },
                {
                    "cmd": "copy terminal: flash:new_config.cfg",
                    "input": new_config,
                },
                "configure replace flash:new_config.cfg",
                "delete flash:new_config.cfg"
            ],
            "format": "json",
            "timestamps": False,
            "autoComplete": False,
            "expandAliases": False,
            "stopOnError": True,
            "streaming": False,
            "includeErrorDetail": False
        },
        "id": "EapiExplorer-1"
}

request = requests.post(
    url, 
    data=json.dumps(json_payload),
    auth=(username, password),
    verify=False,
    headers={"Content-Type": "application/json"}
)

