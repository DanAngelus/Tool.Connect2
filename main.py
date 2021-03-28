from wox import Wox
import json
from subprocess import Popen

class Main(Wox):

  def loadServerSettings(tag):
    with open('ssh-servers.json') as servers_file:
      servers = json.load(servers_file)
#       filtered_servers = list(filter(lambda s: s['tag'] == tag, servers))
#       if filtered_servers:
#         return filtered_servers[0]
#       return {}
      for s in servers:
        if s['tag'] == tag:
          return s
      return {
        "tag": "none",
        "type": "ssh",
        "description": f"Trying to find: {tag}",
        "host": "dammit.son",
        "port": "22",
        "username": "tier2",
        "password": '',
        "certificate": "nocert"
      }
      # return list(filter(lambda s: s['tag'] == tag, servers))

  def searchServerSettings(tag):
    with open('ssh-servers.json') as servers_file:
      servers = json.load(servers_file)
      if not tag:
        return servers
      return list(filter(lambda s: s['tag'].startswith(tag), servers))

  def generateItem(server):
    return {
      'Title': server['tag'],
      'SubTitle': f"🔌 {server['description']}",
      'IcoPath': 'Images/pic.png',
      'JsonRPCAction': {
        'method': 'action',
        'parameters': [server['tag']],
        'dontHideAfterAction': False
      }
    }

  def query(self, userInput):
    if not userInput:
      return [{
        'Title': 'Server tag',
        'SubTitle': 'Start typing a server tag...',
        'IcoPath': 'Images/pic.png',
        'JsonRPCAction': {
          'method': 'action',
          'parameters': [userInput],
          'dontHideAfterAction': False
        }
      }]
    return list(map(lambda server: Main.generateItem(server), Main.searchServerSettings(userInput)))

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
          command = f"echo Connecting to: && echo {description} && echo "
          if password:
            command += f"Use password :: {password}"
          else:
            command += "... "

          command += "&& ssh "

          if certificate:
            command += f"-i {certificate} "


          command += f"{username}@{host} -p {port}"

          # ToDo :: Open into existing window
          # https://docs.microsoft.com/en-us/windows/terminal/command-line-arguments?tabs=linux
          Popen(["wt", "new-tab", "-p", '"{0caa0dad-35be-5f56-a8ff-afceeeaa6101}"', 'cmd', '/K', f"{command}" ])
          return

if __name__ == '__main__':
  Main()
