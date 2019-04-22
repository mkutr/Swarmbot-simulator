from swarm_bot_simulator.model.bot_components import Bot


class Config:
    def __init__(self, app_config):
        self.bot_n = len(app_config["bots"])
        self.communication_settings = CommunicationSettings(app_config["communication_settings"])
        self.bot_settings = BotSettings(app_config["bot_settings"])
        self.view_settings = ViewSettings(app_config["view_settings"])
        self.start_bots = [Bot(b, self.communication_settings, self.bot_settings) for b in app_config["bots"]]

class CommunicationSettings:
    def __init__(self, communication_settings):
        self.broker = communication_settings["broker"]
        self.port = communication_settings["port"]
        self.method = communication_settings["method_is_direct"]


class BotSettings:
    def __init__(self, bot_settings):
        self.view_is_omni = bot_settings["view_mode_is_omni"]
        self.separation_distance = bot_settings["separation_distance"]
        self.max_speed = bot_settings["max_speed"]
        self.max_force = bot_settings["max_force"]

class ViewSettings:
    def __init__(self, view_settings):
        self.launch = view_settings["launch"]

