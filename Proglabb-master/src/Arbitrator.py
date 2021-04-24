class abitrator():

    def __init__(self, bbcon):
        self.bbcon = bbcon

    def choose_action(self):
        max = [None, - float('inf')]
        print("Gets to chose action. Length:",len(self.bbcon.active_behaviors))
        for state in self.bbcon.active_behaviors:
            #print(state.__name__, state.getRecomendation(),"Recomendation")
            if state.getRecomendation() > max[1]:
                max = [state, state.getRecomendation()]
        #print("Done recomending action")
        print("Recomended action from: ", max[0].__name__,". Recomondation:", max[0].getRecomendation())
        return max[0], max[0].getDone()

