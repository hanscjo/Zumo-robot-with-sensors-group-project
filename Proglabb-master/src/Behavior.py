

class Behavior():


    def __init__(self, sensobs, priority, done):
        self.sensobs = sensobs
        self.priority = priority
        self.recomendation = None
        self.done = done
        self.movement = ['F', 0.1]
        self.boot()

    def getSensobs(self):
        return self.sensobs

    def considerActivation(self):
        return False

    def considerDeactivation(self):
        return False

    def updateRecomendation(self):
        return None

    def getRecomendation(self):
        return self.recomendation

    def getMovement(self):
        return self.movement

    def getDone(self):
        return self.done

    def boot(self):
        return None

