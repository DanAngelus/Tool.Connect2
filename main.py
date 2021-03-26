#encoding=utf8
from wox import Wox,WoxAPI
import os

#Your class must inherit from Wox base class https://github.com/qianlifeng/Wox/blob/master/PythonHome/wox.py
#The wox class here did some works to simplify the communication between Wox and python plugin.
class Main(Wox):

  def request(self,url):
    #If user set the proxy, you should handle it.
    if self.proxy and self.proxy.get("enabled") and self.proxy.get("server"):
      proxies = {
        "http":"http://{}:{}".format(self.proxy.get("server"),self.proxy.get("port")),
        "https":"http://{}:{}".format(self.proxy.get("server"),self.proxy.get("port"))}
      return requests.get(url,proxies = proxies)
    else:
      return requests.get(url)

  # A function named query is necessary, we will automatically invoke this function when user query this plugin
  def query(self,key):

    os.system('wt -p "{0caa0dad-35be-5f56-a8ff-afceeeaa6101}" cmd /K "%ALIASES%"')

    return 'Complete'

  def openUrl(self,url):
    webbrowser.open(url)
    WoxAPI.change_query(url)

  #Following statement is necessary
  if __name__ == "__main__":
    Main()
