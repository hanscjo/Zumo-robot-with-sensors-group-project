from Behavior import Behavior

class standardBehavior(Behavior):

    __name__ = "Standard"

    def boot(self):
        self.recomendation = 1
        self.movement = ["F",0.2]

    def getRecomendation(self):
        self.recomendation = 2
        return self.recomendation




