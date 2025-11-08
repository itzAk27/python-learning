class parent:
    def __init__(self, fname):
        self.fname = fname

    def full_name(self):
        return "Khan" + ' ' + self.fname

class child(parent):
    def __init__(self, fname, lname):
        super().__init__(fname)
        self.lname = lname

    def full_name(self):
        return self.fname + '.' + self.lname


class grandChild(child):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

    def full_name(self):
        return "Ok"


obj = grandChild("Akhtar", "Khan")
print(help(obj))
print(obj.full_name())