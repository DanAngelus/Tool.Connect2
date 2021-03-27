from wox import Wox
import os
import json
from subprocess import Popen

class Main(Wox):

  def loadSettings():
    with open('ssh-servers.json') as servers_file:
      servers = json.load(servers_file)
      return servers

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

  def action(self, serverName, commandType = 'ssh'):
    if commandType == 'ssh':
      with open('ssh-servers.json') as servers_file:
        servers = json.load(servers_file)
        server = servers[serverName]

        if server:
          host = server['host']
          port = server['port']
          username = server['username']
          password = server['password']
          certificate = server['certificate']
          description = server['description']

#           command = 'wt new-tab -p "{0caa0dad-35be-5f56-a8ff-afceeeaa6101}" cmd /K "ssh'
#           if certificate:
#             command += ' -i ' + certificate
#
#           command += ' ' + username + '@' + host + ' -p ' + port + '"'

          # Assemble command string
          command = '"ssh'
          if certificate:
            command += ' -i ' + certificate

          command += ' ' + username + '@' + host + ' -p ' + port + '"'

          Popen(['wt', 'new-tab', '-p', '"{0caa0dad-35be-5f56-a8ff-afceeeaa6101}"', 'cmd', '/K', command])
          return

        print('No server found')

if __name__ == '__main__':
  Main()
