from Behavior import Behavior
import math
from PIL import Image

class imageBehavior(Behavior):


    __name__ = "Image"

    def boot(self):
        self.imageSensor = self.sensobs[0]

    #Find point of image with most of a collor
    def findColor(self):
        #return ["L",4] #Should return which way to turn and by how much
        img = self.imageSensor.get_value() #Returns a PIL element
        print("ImageBehaviour type:", type(img))
        img.save("picture.png", "png")
        #TODO Find some color and turn toward that

        red = [150, 50, 50]
        green = [50, 150, 50]
        blue = [50, 50, 150]
        white = [200, 200, 200]
        black = [50, 50, 50]
        selected_color = red  #Kan sette random, eller hva enn vi ønsker
        img_width = 128       #Referanse til kamera sin bildebredde i tilfelle vi endrer
        img_height = 96       #Referanse til kamera sin bildehøyde
        max_deg = 36          #Dette antar at vinkelen for en piksel helt til venstre/høyre er 90 grader. Dette er sannsynligvis feil, og vi må teste
        found_color = False
        x_value = 0           #Er egentlig bare interessert i x-verdien, men w/e
        y_value = 0


        for y in range(0, img_height):  #For-løkken itererer gjennom hvert eneste piksel til den finner en med sterk nok farge

            if not found_color and y != img_height-1:
                for x in range(0, img_width):

                        rgb_values = img.getpixel((x,y))

                        if selected_color == red:
                            if (rgb_values[0] >= red[0] and rgb_values[1] < red[1] and rgb_values[2] < red[2]):
                                found_color = True
                                x_value = x
                                y_value = y

                        elif selected_color == green:
                            if (rgb_values[0] < green[0] and rgb_values[1] >= green[1] and rgb_values[2] < green[2]):
                                found_color = True
                                x_value = x
                                y_value = y

                        elif selected_color == blue:
                            if (rgb_values[0] < blue[0] and rgb_values[1] < blue[1] and rgb_values[2] >= blue[2]):
                                found_color = True
                                x_value = x
                                y_value = y

                        elif selected_color == white:
                            if (rgb_values[0] > white[0] and rgb_values[1] > white[1] and rgb_values[2] > white[2]):
                                found_color = True
                                x_value = x
                                y_value = y

                        elif selected_color == black:
                            if (rgb_values[0] < black[0] and rgb_values[1] < black[1] and rgb_values[2] < black[2]):
                                found_color = True
                                x_value = x
                                y_value = y

        if not found_color:
            print("Fant ingen farge!")
            return["F", 0.5]

        else:  #Beregner ut retning og grader roboten skal snu seg, i forhold til max-bredde og hvor den oppdagede fargen ligger
            half_of_width = math.floor(img_width/2)

            print("Fant valgt farge på x:", x_value, "y:", y_value)

            if x_value == half_of_width:   #Fargen ble oppdaget rett frem
                return["R", 0]

            elif x_value < half_of_width:  #Fargen ble oppdaget til venstre
                degree = ((half_of_width - x_value) / half_of_width) * max_deg
                return["L", int(degree)]

            elif x_value > half_of_width:  #Fargen ble oppdaget til høyere
                degree = ((x_value - half_of_width) / half_of_width) * max_deg
                return["R", int(degree)]




    def setMovement(self, movement):
        self.movement = movement

    def updateRecomendation(self):
        colorPlace = self.findColor()
        self.setMovement(colorPlace)
        if colorPlace == ["F", 0.5]:
            self.recomendation = 0
        else:
            self.recomendation = 1000