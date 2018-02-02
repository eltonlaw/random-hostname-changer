import random
import json
import subprocess
from itertools import permutations
# pylint:disable=no-member

class NameGenerator:
    def __init__(self):
        # SystemRandom object is closer to truly random
        self.sr = random.SystemRandom()

    def random_names(self):
        with open("stupid_names.json", "r") as f:
            names = json.load(f)
        return sr.choice(names)

    def random_anagram(self, original="MARK-C02TT2W0G8WN"):
        original = "MARK-C02TT2W0G8WN"
        shuffled = list(original)
        self.sr.shuffle(shuffled)
        return ''.join(shuffled)

    def random_sentence_structure(self, structure=None):
        structure = ["adjective", "noun"]

        if not structure:
            available = ["verb", "noun", "adjective"]
            structure = sr.choice(list(permutations(available)))

        try:
            name = "-".join([sr.choice(words[piece]) for piece in structure])
        except AttributeError:
            with open("sentence_fragments.json", "r") as f:
                self.words = json.load(f)
                self.random_sentence_structure()
        return name

ng = NameGenerator()
new_name = ng.random_sentence_structure()
subprocess.run("sudo scutil --set ComputerName {}".format(new_name))
subprocess.run("sudo scutil --set LocalHostName {}".format(new_name))
subprocess.run("sudo scutil --set HostName {}".format(new_name))
subprocess.run("dscacheutil -flushcache")
