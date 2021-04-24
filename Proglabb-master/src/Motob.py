import motors

class motob():

    def __init__(self):
        self.motor = motors.Motors()
        self.value = [0,0]
        self.dur = None

    def setValue(self,val,dur = None):
        if len(val) != 2:
            print("Val tar in to verdier")
        for value in val:
            if value > 1 or value < -1:
                print("Motor mellom [-1,1]")
                return
        self.value = val

    def setDur(self,dur):
        if dur <= 0:
            self.dur = None
        else:
            self.dur = dur

    def recomend(self, rec): #[(L,R,F,B,S), (deg, deg, speed, speed, 0]
        print("Gets recomendation:",rec)
        degTime = 0.4/90
        if rec[0] == "L" or rec[0] == "R":
            acc = [-0.5, 0.5]
            if rec[0] == "R":
                acc = [ -x for x in acc]
            self.setValue(acc)
            self.setDur(degTime*rec[1])
        elif rec[0] == "F"or rec[0] == "B":
            acc = [rec[1],rec[1]]
            if rec[0] == "B":
                acc = [ -x for x in acc]
            self.setValue(acc)
            self.setDur(0)
        elif rec[0] == "S":
            self.value = [0,0]
            self.dur = None


    def update(self):
        print("Uppdated value:",self.value, "duration:",self.dur)
        if self.value == [0,0]:
            self.motor.stop()
        else:
            self.motor.set_value(self.value, self.dur)

    def drive(self,val=None):
        if val != None:
            self.setValue(val)
        self.update()

    def stop(self):
        self.motor.stop()
