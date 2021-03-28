
import json

with open('settings.json') as settings:
  serversConfigLocation = json.load(settings)['serversConfigLocation']

class ConfigManager():

  def loadServerSettings(tag):
    with open(serversConfigLocation) as servers_file:
      servers = json.load(servers_file)
      return next(s for s in servers if s['tag'] == tag)

  def searchServerSettings(tag):
    with open(serversConfigLocation) as servers_file:
      servers = json.load(servers_file)
      if not tag:
        return servers
      return list(filter(lambda s: s['tag'].startswith(tag), servers))
