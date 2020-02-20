from os import path

def get_db_path():
    return path.join(path.expanduser("~"), ".config", "schwi")

def get_global_config_path():
    return path.join(get_db_path(), "db", "global.json")

def get_anime_path(id):
    return path.join(get_db_path(), "db", "anime", str(id) + ".json")