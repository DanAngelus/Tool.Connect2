from wox import Wox
import os

class Main(Wox):

  def query(self, userInput):
    return [{
      'Title': 'Enter server name',
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
      os.system('wt -p "{0caa0dad-35be-5f56-a8ff-afceeeaa6101}" cmd /K "%ALIASES% && %CMD_TOOLS%/ssh/' + serverName + '.bat"')

if __name__ == '__main__':
  Main()
