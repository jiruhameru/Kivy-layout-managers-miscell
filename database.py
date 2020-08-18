import datetime

class Database:
    def __init__(self, filename):
        self.filename = filename
        self.speakers = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.speakers = {}

        for line in self.file:
            id_speaker, name = line.strip().split(";")
            self.speakers[id_speaker] = (name)

        self.file.close()


