import json
from models import utilities


class Anime():
    def __init__(self, name):
        # Determine the next ID to use
        # TODO: Refactor this into a general function
        global_config = {}
        with open(utilities.get_global_config_path()) as json_file:
            global_config = json.load(json_file)
            self.id = global_config["Next Anime ID"]  # The internal ID
            global_config["Next Anime ID"] += 1
        with open(utilities.get_global_config_path(), 'w') as json_file:
            json.dump(global_config, json_file, indent=4)
        self.name = name  # The base Japanese name
        self.year = None  # The inital release year
        self.status = "Plan to Watch"  # The status of this entry
        self.score = None  # Our score for this entry
        self.progress = None  # Our progress for this entry
        self.episode_count = None  # The total number of episodes
        self.start_date = None  # When did we start watching?
        self.end_date = None  # When did we stop watching?
        self.rewatch_count = 0  # How many times have we rewatched this?
        self.notes = ""  # Custom notes
        self.externals = {}  # Information about external services
        self.alternate_names = []  # Do we have other names for this?
        self.custom_categories = []  # Our custom categories
        self.genres = []  # This entry's genres
        self.tags = []  # This entry's tags
        self.Save()

    def Save(self):
        self_dict = {}
        self_dict["Name"] = self.name
        self_dict["Release Year"] = self.year
        self_dict["Status"] = self.status
        self_dict["Score"] = self.score
        self_dict["Progress"] = self.progress
        self_dict["Episode Count"] = self.episode_count
        self_dict["Start Date"] = self.start_date
        self_dict["End Date"] = self.end_date
        self_dict["Rewatch Count"] = self.rewatch_count
        self_dict["Notes"] = self.notes
        self_dict["External Services"] = self.externals
        self_dict["Alternate Names"] = self.alternate_names
        self_dict["Custom"] = self.custom_categories
        self_dict["Genres"] = self.genres
        self_dict["Tags"] = self.tags
        with open(utilities.get_anime_path(self.id), 'w') as json_file:
            json.dump(self_dict, json_file, indent=4)
