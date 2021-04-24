
class Sensob():

    def __init__(self, sensorlist):

        self.sensobValues = {}

        for sensor in sensorlist:
            self.sensobValues[sensor] = 0



    def update(self):

        for sensor in self.sensobValues:
            self.sensobValues[sensor].update()              #Dersom vi skal oppdatere gjennom Sensob klassen
            self.sensobValues[sensor] = sensor.get_value()  #Spørs hva som er mest naturlig
