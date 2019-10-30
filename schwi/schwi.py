from os import path

home_path = path.expanduser("~")
print(home_path)
config_path = path.join(home_path, ".config", "schwi")
print(config_path)