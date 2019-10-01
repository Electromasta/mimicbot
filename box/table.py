class table:
    name = "Default"
    rows = []
    def __init__(self, name):
        self.name = name
        self.rows = []
    def addRow(self, r):
        self.rows.append(r)
    def get(self, i):
        for row in self.rows:
            if i in range(row.begin, row.end):
                return row
        return None

class row:
    name = "Default"
    begin = 0
    end = 10
    desc = "This is a descriptive text"
    def __init__(self, name, begin, end, desc):
        #print(name + ": " + str(begin) + ", " + str(end+1))
        self.name = name
        self.begin = begin
        self.end = end+1
        self.desc = desc

        
def testTable():
    t = table("Test Table")
    t.addRow(row("Reefclaw", 1, 45))
    t.addRow(row("Dire Reefclaw", 46, 70))
    t.addRow(row("Reefclaw Lich", 71, 90))
    t.addRow(row("Reefclaw Dragon", 91, 99))
    t.addRow(row("Reefclaw Deity", 100, 100))
    return t
