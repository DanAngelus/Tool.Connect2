from wox import Wox
from subprocess import Popen
from ConfigManager import ConfigManager

class Connect2(Wox):

  configManager = ConfigManager()

  def generateItem(self, server):
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
    return list(map(lambda server: self.generateItem(server), self.configManager.searchServerSettings(userInput)))

  def action(self, tag, commandType = 'ssh'):
    if commandType == 'ssh':
      server = self.configManager.loadServerSettings(tag)
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
          command += f"-i {self.configManager.getKeysLocation()}/{certificate} "

        command += f"{username}@{host} -p {port}"

        Popen(["wt", "-f", "-p", '"{0caa0dad-35be-5f56-a8ff-afceeeaa6101}"', 'cmd', '/K', f"{command}" ])
        return

if __name__ == '__main__':
  Connect2()
