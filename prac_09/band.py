class Band:

    def __init__(self, name=""):
        """initialize band name with musician as empty list"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """string representation of band"""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """add musician to band"""
        self.musicians.append(musician)

    def play(self):
        """string representation of musicians playing their instruments"""
        return '\n'.join(musician.play() for musician in self.musicians)
