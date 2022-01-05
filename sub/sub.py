import hashlib
import os
import json


class Japan():
    def __init__(self):
        self.president = "kisida-san"
        self.world_population_ranking = 11
        self.major_cities = ["Tokyo", "Yokohama", "Saitama", "Chiba"]
        self.secure_hash = self._get_secure_hash()

    def _get_secure_hash(self):
        return hashlib.sha256(os.urandom(32)).hexdigest()

    def get_president(self):
        return self.president

    def get_information(self):
        dictionary = {
            "president": self.president,
            "world_population_ranking": self.world_population_ranking,
            "major_cities": self.major_cities,
            "secure_hash": self.secure_hash
        }
        return json.dumps(dictionary)
