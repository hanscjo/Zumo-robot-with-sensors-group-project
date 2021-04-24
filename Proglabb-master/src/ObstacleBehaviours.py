from Behavior import*

class UltraSonic(Behavior):

    __name__ = "Ultrasonic"

    def boot(self): #(self, sensobs):
        self.uSonic= self.sensobs[0]

    def sensorPull(self):
        return self.uSonic.get_value()

#-----------------------------------------------------------------------------------------------------------------------

class StopAtSight(UltraSonic):

    def updateRecomendation(self):
        distance = (self.sensorPull()/2)* 0.034
        if distance <= 20 and distance > 0:
            self.recomendation = (1/(distance))*self.priority   #Kaller stopp med hoyere pri nearmere vegg
            self.movement = ["S",0]
        else:
            self.recomendation = 0
            self.movement = ["F",0.5]

#-----------------------------------------------------------------------------------------------------------------------

class Turn90AtSight(UltraSonic):

    def updateRecomendation(self):
        distance = (self.sensorPull()/2)* 0.034
        if distance <= 20 and distance > 0:
            self.recomendation = (1/(distance))*self.priority   #Kaller stopp med hoyere pri naermere vegg
            self.movement = ["F",90]
        else:
            self.recomendation = 0
            self.movement = ["F",0.5]

#-----------------------------------------------------------------------------------------------------------------------

class RunAtSight(UltraSonic):

    def updateRecomendation(self):
        distance = (self.sensorPull())
        print("Distance:", self.uSonic.get_value())
        if distance <= 20 and distance > 0:
            self.recomendation = distance*self.priority   #Kaller stopp med hoyere pri naermere vegg
            self.movement = ["L",180]
        else:
            self.recomendation = 0
            self.movement = ["F",0.2]

#-------------------------------------------------------------
