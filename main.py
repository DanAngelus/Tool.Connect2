from wox import Wox
import os
import json
from subprocess import Popen

class Main(Wox):

  def loadServerSettings(tag):
    with open('ssh-servers.json') as servers_file:
      servers = json.load(servers_file)
      return servers[tag]

  def query(self, userInput):
    # ToDo :: Load servers from file for auto-complete
    return [{
      'Title': 'Enter server tag',
      'SubTitle': 'Connect to: ' + userInput,
      'IcoPath': 'Images/pic.png',
      'JsonRPCAction': {
        'method': 'action',
        'parameters': [userInput],
        'dontHideAfterAction': False
      }
    }]

  def action(self, tag, commandType = 'ssh'):
    if commandType == 'ssh':
      with open('ssh-servers.json') as servers_file:
        server = Main.loadServerSettings(tag)

        if server:
          host = server['host']
          port = server['port']
          username = server['username']
          password = server['password']
          certificate = server['certificate']
          description = server['description']

          # Assemble command string
          command = f"echo Connecting to: {description} && ssh "
          if certificate:
            command += f"-i {certificate} "

          command += f"{username}@{host} -p {port}"

#           Popen(["cmd", '/K', command ])
          Popen(["wt", "new-tab", "-p", '"{0caa0dad-35be-5f56-a8ff-afceeeaa6101}"', 'cmd', '/K', f"{command}" ])
          return

        print('No server found')

if __name__ == '__main__':
  Main()
