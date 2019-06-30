from BackEnd.api.models import HDPE_Output_Grade, HDPE_Output_Transition, HDPE_Output_NonPrime, HDPE_Output_Summary
from BackEnd.api.models import HDPE_Grade_Number, HDPE_Trains, HDPE_Transition

import numpy
import random

class HDPE_Sequence_Model():

    def hdpe_output_grade(instance):

        output = []
        temp1 = []
        temp2 = []
        trains = HDPE_Trains.objects.all()
        grades = HDPE_Grade_Number.objects.all()
        
        for i in range (0, len(trains)):
            for j in range (0, len(grades)):
                for day in range (0, 30):
                    temp1.append(random.randint(0, 500))
                temp2.append(temp1)    
            output.append(temp2)

        return output    

    def hdpe_output_transition(instance):

        output = []
        temp1 = []
        temp2 = []
        trains = HDPE_Trains.objects.all()
        transitions = HDPE_Transition.objects.all()
        
        for i in range (0, len(trains)):
            for j in range (0, len(transitions)):
                for day in range (0, 30):
                    temp1.append(random.randint(0, 100))
                temp2.append(temp1)    
            output.append(temp2)

        return output

    def hdpe_output_nonprime(instance):

        output = []
        temp1 = []
        
        for i in range (0, 5):
            for day in range (0, 30):
                temp1.append(random.randint(0, 100))
            output.append(temp1)

        return output               
        


