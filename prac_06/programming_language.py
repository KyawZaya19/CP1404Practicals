"""
Programming language class
"""


class ProgrammingLanguage:
    """ Consist of the information about a programming language"""
    def __init__(self, name, typing, reflection, year):
        """Initialise given programming language data """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """ Determine if the typing is dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        """ Return the string representation of the programming language information """
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
