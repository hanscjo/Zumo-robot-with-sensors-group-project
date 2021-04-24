from Behavior import*

class GroundCheck(Behavior):

    __name__ = "Ground check"

    def boot(self):
        self.uSonic= self.sensobs[0]
        self.value = None

    def sensorPull(self):
        return self.uSonic.get_value()

#----------------------------------------------------------

#Turns the robot when it drives over something black
class turnAtSight(GroundCheck):

    def updateRecomendation(self):
        color = min(self.sensorPull()) #Value between 0 and 1
        print("Reads from ground:", color)
        if color < 0.01:
            self.recomendation = self.priority*1
            self.movement = ["L", 180] #Turn 180 dgr
        else:
            self.recomendation = 0


#-----------------------------------------------------------


#-----------------------------------------------------------

class dontFallOfEdge(GroundCheck):

    def updateRecomendation(self):
        sensorList = self.sensorPull()
        colorL = sensorList[0]
        colorR = sensorList[5]
        if colorL < self.threshHold and colorR < self.threshHold:
            self.recomendation = self.priority
            self.movement = ["R",180]
        elif colorL < self.threshHold:
            self.recomendation = self.priority
            self.movement = ["R",90]
        elif colorR < self.threshHold:
            self.recomendation = self.priority
            self.movement = ["L",90]

#-----------------------------------------------------------

class followTheLine(GroundCheck):

    def lineInMid(self,SL):
        if SL[2] < self.threshHold or SL[3] < self.threshHold:
            return True
        return False

    def lineOnLeft(self,SL):
        if SL[0] < self.threshHold:
            return True
        return False

    def lineOnRight(self, SL):
        if SL[5] < self.threshHold:
            return True
        return False

    def updateRecomendations(self):
        SL = self.sensorPull()
        self.recomendation = self.priority
        if self.lineInMid(SL):
            self.movement = ["F",0.3]
        elif self.lineOnLeft(SL):
            self.movement = ["R", 30]
        elif self.lineOnRight(SL):
            self.movement = ["L", 30]
        else:
            self.recomendation = 0
