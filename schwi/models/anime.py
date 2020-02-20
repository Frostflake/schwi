import json

class Anime():
    def __init__(self, name):
        self.id = 0 # The internal ID
        self.name = name # The base Japanese name
        self.year = None # The inital release year
        self.status = "Plan to Watch" # The status of this entry
        self.score = None # Our score for this entry
        self.progress = None # Our progress for this entry
        self.episode_count = None # The total number of episodes
        self.start_date = None # When did we start watching?
        self.end_date = None # When did we stop watching?
        self.rewatch_count = 0 # How many times have we rewatched this?
        self.notes = "" # Custom notes
        self.externals = {} # Information about external services
        self.alternate_names = [] # Do we have other names for this?
        self.custom_categories = [] # Our custom categories
        self.genres = [] # This entry's genres
        self.tags = [] # This entry's tags

    def Json():
        return ""
