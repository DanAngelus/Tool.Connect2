import json

class ConfigManager():
    with open('settings.json') as settings:
        settings = json.load(settings)

    def loadServerSettings(self, tag):
        with open(self.settings['serversConfigLocation']) as servers_file:
            servers = json.load(servers_file)
            return next(s for s in servers if s['tag'] == tag)

    def searchServerSettings(self, tag):
        with open(self.settings['serversConfigLocation']) as servers_file:
            servers = json.load(servers_file)
            if not tag:
                return servers
            return list(filter(lambda s: s['tag'].startswith(tag), servers))

    def getKeysLocation(self):
        return self.settings['sshKeysLocation']
