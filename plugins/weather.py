import plugintypes
import sys

sys.path.append('./plugins')

from py3owm import OpenWeatherMap

class WeatherPlugin(plugintypes.TelegramPlugin):
    """
    Weather
    """

    patterns = [
        "^!weather (.*)"
    ]

    usage = [
        "!weather <zip code>|<city>"
    ]

    def activate(self):
        if not self.has_option("api key"):
            self.write_option("api key", "")
        
        api_key = self.read_option("api key")
        self.owm = OpenWeatherMap(api_key, "imperial")


    def run(self, msg, matches):
        return self.owm.weather(zip="91941")
