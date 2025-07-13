class ProgrammingLanguage:
    def __init__(self,name, typing, reflection, year):
        """initialize programming language"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """return string representation of programming language"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """return true if programming language is dynamic"""
        return self.typing == "Dynamic"