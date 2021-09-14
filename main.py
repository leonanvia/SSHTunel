import json
from SSHLibrary import SSHLibrary
import sys

list_of_arguments = sys.argv
ssh = SSHLibrary()


if len(list_of_arguments) == 1:

    with open(r"conf.json", "r") as file:
        data = json.load(file)

    ssh.enable_ssh_logging("./log")

    ssh.open_connection(data["ip"])
    ssh.login(data["user"], data["pass"])    

    for p in data["tunel"]:
        porta = p["porta"]
        host = p["ip"]
        
        ssh.create_local_ssh_tunnel(porta,host,porta)
        print('Created Tunel for -> '+porta+':'+host+':'+porta)    
else:
    if list_of_arguments[1] == 'stop':
        ssh.close_all_connections()
        print('All connections closed')