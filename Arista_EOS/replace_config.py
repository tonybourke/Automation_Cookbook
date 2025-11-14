# This method doesn't use PyeAPI

import requests
import json
import uuid
import urllib3
urllib3.disable_warnings()

username = "admin"
password = "admin"
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
                    "cmd": f"configure session {cs_id}"
                },
                {
                    "cmd": "rollback clean-config"
                },
                {
                    "cmd": "copy terminal: session-config",
                    "input": new_config,
                },
                "commit",
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
