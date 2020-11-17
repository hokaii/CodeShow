class Character:
    def __init__(self):
        self.name = ""
        self.who = ""
        self.what = ""
        self.IS = True
        self.desc = ""
        self.reverseSelf = Character()

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getReverseSelf(self):
        return self.reverseSelf

    def setReverseSelf(self, reverseSelf):
        self.reverseSelf = reverseSelf

    def getWho(self):
        return self.who

    def setWho(self, who):
        self.who = who

    def getDesc(self):
        return self.desc

    def getWhat(self):
        return self.what

    def setWhat(self, what):
        self.what = what

    def isIs(self):
        return self.IS

    def setIs(self, IS):
        self.IS = IS

    def Character(self, who, what, IS):
        super()
        self.who = who
        self.what = what
        self.IS = IS

    #def Character(self):
    #    super()


class Statement:
    def __init__(self):
        self.charSet = []

    def getCharSet(self):
        return self.charSet

    def setCharSet(self, charSet):
        self.charSet = charSet

    def addCharacter(self, addch):
        for ch in self.charSet:
            if ch.getDesc().eq(addch.getDesc()):
                raise RuntimeError("同一个子句中存在两个相反的变量 p和非p")
        self.charSet.append(addch)

    def __eq__(self, other):
        if other == self:
            return True
        if other
