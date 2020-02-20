from os import path
from models import anime

home_path = path.expanduser("~")
print(home_path)
config_path = path.join(home_path, ".config", "schwi")
print(config_path)
anime.Anime("This is a Test")
