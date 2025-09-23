# I was trying to do config replacement with sessions, but couldn't get it to work. This cleared out all the superfluous sessions. 

import ssl 
from jsonrpclib import Server 

_create_unverified_https_context = ssl._create_unverified_context
ssl._create_default_https_context = _create_unverified_https_context

username = "arista"
password = "0la430sqf5jk8uk6"
device = "leaf1"
url = "https://{username}:{password}@{device}/command-api".format(username=username, password=password, device=device)


switch = Server(url) 
response = switch.runCmds(1, ["show configuration sessions"]) 

for session in response[0]['sessions']:
    clear_reponse = switch.runCmds(1, [f"configure session {session} abort"])
    print(f"Cleared session {session}")