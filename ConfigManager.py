import json


class ConfigManager():
    with open('settings.json') as settings:
        settings = json.load(settings)

    def load_server_settings(self, tag):
        with open(self.settings['serversConfigLocation']) as servers_file:
            servers = json.load(servers_file)
            return next(s for s in servers if s['tag'] == tag)

    def search_server_settings(self, tag):
        with open(self.settings['serversConfigLocation']) as servers_file:
            servers = json.load(servers_file)
            if not tag:
                return servers
            return list(filter(lambda s: s['tag'].startswith(tag), servers))

    def get_keys_location(self):
        return self.settings['sshKeysLocation']
