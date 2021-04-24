#Import sensors
from camera import Camera
from ultrasonic import Ultrasonic
from zumo_button import ZumoButton
from reflectance_sensors import ReflectanceSensors

#Import packages
from time import sleep

#Import other classes
from Motob import motob
from Arbitrator import abitrator
from StandardBehavior import standardBehavior
from ObstacleBehaviours import StopAtSight, Turn90AtSight, RunAtSight
from GroundBehaviours import turnAtSight as turnOverBlack
from ImageBehavior import imageBehavior

class BBCON():


    def __init__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = []
        self.motobs = motob()
        self.abitrator = abitrator(self)


    def addBehavior(self):
        #TODO Should append all the nessecary behaviors
        self.behaviors.append(standardBehavior([None], 1, False)) #Moves forward
        self.behaviors.append(RunAtSight([self.sensobs[1]], 10000, False)) #Avoids wall
        self.behaviors.append(turnOverBlack([self.sensobs[3]], 2000, False)) #Discovers black dot
        for behavior in self.behaviors:
            print("Added behavior:",behavior.__name__)
            self.activateBehavior(behavior)
        #TODO Add a behavior for taking pictures
        self.behaviors.append(imageBehavior([self.sensobs[0]], 10, False))

    def addSenob(self):
        #TODO Should append all the nessecary sensory objects
        self.sensobs.append(Camera())
        self.sensobs.append(Ultrasonic())
        self.sensobs.append(ZumoButton())
        self.sensobs.append(ReflectanceSensors())
        #Added all sensors

    def activateBehavior(self, behavior):
        if self.behaviors.__contains__(behavior) and not self.active_behaviors.__contains__(behavior):
            self.active_behaviors.append(behavior)

    def deactivate_behavior(self, behavior):
        if self.active_behaviors.__contains__(behavior):
            self.active_behaviors.remove(behavior)

    #TODO Evrything else...
    def runOneTimestep(self):
        print("Starts")
        button = ZumoButton()
        button.wait_for_press()
        self.addSenob()
        self.addBehavior()
        pictureTime = 0
        while True:
            #print("Runns itteration")
            #Reads from active sensors
            activeSensors = []
            #Adds imageBehaviour
            if pictureTime > 3:
                self.active_behaviors.append(self.behaviors[3])

            for behavior in self.active_behaviors:
                sensorList = behavior.getSensobs()
                for sensor in sensorList:
                    if not activeSensors.__contains__(sensor):
                        activeSensors.append(sensor)
            #print("Adds to active sensors")
            for sensor in activeSensors:
                #print("Adds sensor")
                if (sensor != None):
                    sensor.update()
            #print("Update all behaviors")
            #Update all behaviors
            for behavior in self.active_behaviors:
                behavior.updateRecomendation()
            #print("About to chose action")
            #Requesting the motor recomendation and halt request flag
            behavior, requestFlag = self.abitrator.choose_action()
            #print("Action:", behavior.getMovement())
            if requestFlag:
                break
            #Update the motobs so that the motors are activated/deactivated
            self.motobs.recomend(behavior.getMovement())
            #print("Recomended movement")
            self.motobs.update()
            #print("Uppdated motors")

            if self.active_behaviors.__contains__(self.behaviors[3]):
                self.active_behaviors.remove(self.behaviors[3])
                pictureTime = 0

            #Wait. Defines how long the code should wait
            sleep(0.05)
            pictureTime = pictureTime + 1
            #Resets sensors
            for sensor in activeSensors:
                if sensor != None:
                    sensor.reset()


if __name__ == "__main__":
    bbcon = BBCON()
    bbcon.runOneTimestep()