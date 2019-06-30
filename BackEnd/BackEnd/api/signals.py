from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import HDPE_Grade_Run, HDPE_Trains, HDPE_Grade_Number, Contribution_Areas, HDPE_Demand_Pattern, HDPE_Demand_Stock
from .models import HDPE_TPH, HDPE_Contribution, HDPE_Minimum_Sales, HDPE_Maximum_Sales, HDPE_GM_Demand, HDPE_Restart_Parameters 
from .models import HDPE_Execution_Parameters, NCU_Parameters, NCU_Parameters_Stock, HDPE_Transition, HDPE_Output_Summary, HDPE_Grade_Activation
from .models import HDPE_Last_Running_Grades, HDPE_Last_Main_Grade, HDPE_Last_Transition_Grade, HDPE_Last_Maintenance, HDPE_Last_Under_Restart
from .models import HDPE_Output_Grade, HDPE_Output_Transition, HDPE_Output_NonPrime
from BackEnd.sequencemodel.hdpesequence import HDPE_Sequence_Model

import numpy
import random
import datetime as datetime


# generate all HDPE_Grade_Activation post save HDPE_Grade_Run with default true value

@receiver(post_save, sender=HDPE_Grade_Run)
def create_hdpe_grade_activation(sender, instance, **kwargs):

   allgrades = HDPE_Grade_Number.objects.all().order_by('id')

   for i in range (0, len(allgrades)):
       HDPE_Grade_Activation.objects.create(Active_Status = True, hdpe_Grade_Number = allgrades[i], hdpe_Grade_Run = instance)



# generate HDPE_Demand_Stock post save HDPE_Grade_Run corresponding to each grade based on previous months input

@receiver(post_save, sender=HDPE_Grade_Run)
def create_hdpe_demand_stock(sender, instance, **kwargs):

   allgrades = HDPE_Grade_Number.objects.all().order_by('id')

   for i in range (0, len(allgrades)):
       HDPE_Demand_Stock.objects.create(Demand = random.randint(600,6000), Opening_Inventory = random.randint(600,6000), Closing_Inventory = random.randint(600,6000), hdpe_Grade_Number = allgrades[i], hdpe_Grade_Run = instance)



# generate HDPE_Demand_Pattern post save HDPE_Grade_Run corresponding to each grade for all the days in the run

@receiver(post_save, sender=HDPE_Grade_Run)
def create_hdpe_demand_pattern(sender, instance, **kwargs):

   allgrades = HDPE_Grade_Number.objects.all().order_by('id')

   for i in range (0, len(allgrades)):
       for j in range (0, instance.Plan_Days):
           HDPE_Demand_Pattern.objects.create(Day = j+1, Demand_Percentage = random.randint(0.0, 5.0), hdpe_Grade_Number = allgrades[i], hdpe_Grade_Run = instance)



# generate HDPE_TPH post save HDPE_Grade_Run for each train and grade

@receiver(post_save, sender=HDPE_Grade_Run)
def create_hdpe_tph(sender, instance, **kwargs):

   allgrades = HDPE_Grade_Number.objects.all().order_by('id')
   alltrains = HDPE_Trains.objects.all().order_by('id')

   for i in range (0, len(allgrades)):

       Train_TPH = random.randint(18, 22)
       Minimum_Batch_Size = random.randint(300, 800)
       C2_Percentage = random.randint(0.0, 5.0)
       C3_Percentage = random.randint(0.0, 5.0)

       for j in range (0, len(alltrains)):
           HDPE_TPH.objects.create(Train_TPH = Train_TPH, Minimum_Batch_Size = Minimum_Batch_Size, C2_Percentage = C2_Percentage, C3_Percentage = C3_Percentage, hdpe_Trains = alltrains[j], hdpe_Grade_Number = allgrades[i], hdpe_Grade_Run = instance)




# generate HDPE_Contribution for each contribution area and each grade

@receiver(post_save, sender=HDPE_Grade_Run)
def create_hdpe_contribution(sender, instance, **kwargs):

   allgrades = HDPE_Grade_Number.objects.all().order_by('id')
   allcontributionareas = Contribution_Areas.objects.all().order_by('id')

   for i in range (0, len(allcontributionareas)):

       for j in range (0, len(allgrades)):
           HDPE_Contribution.objects.create(Contribution_Amount = random.randint(15000, 25000), contribution_Areas = allcontributionareas[i], hdpe_Grade_Number = allgrades[j], hdpe_Grade_Run = instance)



# generate HDPE_Minimum_Sales for each contribution area and each grade

@receiver(post_save, sender=HDPE_Grade_Run)
def create_hdpe_minimum_sales(sender, instance, **kwargs):

   allgrades = HDPE_Grade_Number.objects.all().order_by('id')
   allcontributionareas = Contribution_Areas.objects.all().order_by('id')

   for i in range (0, len(allcontributionareas)):

       for j in range (0, len(allgrades)):
           HDPE_Minimum_Sales.objects.create(Minimum_Sales_Amount = random.randint(15000, 25000), contribution_Areas = allcontributionareas[i], hdpe_Grade_Number = allgrades[j], hdpe_Grade_Run = instance)



# generate HDPE_Maximum_Sales for each contribution area and each grade

@receiver(post_save, sender=HDPE_Grade_Run)
def create_hdpe_maximum_sales(sender, instance, **kwargs):

   allgrades = HDPE_Grade_Number.objects.all().order_by('id')
   allcontributionareas = Contribution_Areas.objects.all().order_by('id')

   for i in range (0, len(allcontributionareas)):

       for j in range (0, len(allgrades)):
           HDPE_Maximum_Sales.objects.create(Maximum_Sales_Amount = random.randint(15000, 25000), contribution_Areas = allcontributionareas[i], hdpe_Grade_Number = allgrades[j], hdpe_Grade_Run = instance)



# generate HDPE_GM_Demand for each contribution area and each grade

@receiver(post_save, sender=HDPE_Grade_Run)
def create_hdpe_GM_demand(sender, instance, **kwargs):

   allgrades = HDPE_Grade_Number.objects.all().order_by('id')
   allcontributionareas = Contribution_Areas.objects.all().order_by('id')

   for i in range (0, len(allcontributionareas)):

       for j in range (0, len(allgrades)):
           HDPE_GM_Demand.objects.create(GM_Demand = random.randint(0, 1000), contribution_Areas = allcontributionareas[i], hdpe_Grade_Number = allgrades[j], hdpe_Grade_Run = instance)



# generate HDPE_Restart_Parameters for each grade if that grade is a restart grade

@receiver(post_save, sender=HDPE_Grade_Run)
def create_hdpe_restart_parameters(sender, instance, **kwargs):

   allrestartgrades = HDPE_Grade_Number.objects.filter(Restart_Grade = True)

   for i in range (0, len(allrestartgrades)):

       HDPE_Restart_Parameters.objects.create(Hours_Prime_Production = random.randint(10, 20), Avg_TPH = random.randint(10, 20), NP_Amount = random.randint(10, 20), OG_Amount = random.randint(10, 20), LG_Amount = random.randint(10, 20), hdpe_Grade_Number = allrestartgrades[i], hdpe_Grade_Run = instance)



# generate HDPE_Execution_Parameters for each trains based on previous month values

@receiver(post_save, sender=HDPE_Grade_Run)
def create_hdpe_execution_parameters(sender, instance, **kwargs):

   alltrains = HDPE_Trains.objects.all().order_by('id')

   for i in range (0, len(alltrains)):
       
       HDPE_Execution_Parameters.objects.create(Start_Date_Time = '2019-6-20 10:10:10' , Duration = random.randint(10, 20),
       Maintenance_Start_Day = random.randint(10, 20),
       Maintenance_Start_Hour = random.randint(10, 20),
       Maintenance_Duration = random.randint(10, 20),
       Initial_Maintenance_Duration = random.randint(10, 20),
       Allowable_Days = random.randint(10, 20),
       Allowable_Hours = random.randint(10, 20),
       Difference_Days = random.randint(10, 20),
       Difference_Hours = random.randint(10, 20),
       hdpe_Trains = alltrains[i], hdpe_Grade_Run = instance)



# generate NCU_Parameters for each day corresponding to the current run

@receiver(post_save, sender=HDPE_Grade_Run)
def create_ncu_parameters(sender, instance, **kwargs):

    for i in range (0, instance.Plan_Days):

        NCU_Parameters.objects.create(Day = i+1, NCU_Load = random.randint(200, 300), Ethylene_Yield = random.randint(10, 20),
        Propylene_Yield = random.randint(10, 20), hdpe_Grade_Run = instance)

####################generate NCU_Parameters_Stock#####################

@receiver(post_save, sender=HDPE_Grade_Run)
def create_ncu_parameters_stock(sender, instance, **kwargs):

    Ethylene_Opening_Stock = random.randint(1000, 2000)
    Ethylene_Closing_Stock = random.randint(1000, 2000)
    Propylene_Opening_Stock = random.randint(1000, 2000)
    Propylene_Closing_Stock = random.randint(1000, 2000)

    NCU_Parameters_Stock.objects.create(Ethylene_Opening_Stock = Ethylene_Opening_Stock, Ethylene_Closing_Stock = Ethylene_Closing_Stock,
    Propylene_Opening_Stock = Propylene_Opening_Stock, Propylene_Closing_Stock = Propylene_Closing_Stock, hdpe_Grade_Run = instance)


# generate HDPE_Transition based on previous months values

@receiver(post_save, sender=HDPE_Grade_Run)
def create_hdpe_transition(sender, instance, **kwargs):

    parent = HDPE_Grade_Run.objects.all().order_by('-id')[1]
    transitions = HDPE_Transition.objects.filter(hdpe_Grade_Run = parent)

    for i in range (0, len(transitions)):
        HDPE_Transition.objects.create(Transition_TPH = transitions[i].Transition_TPH , Transition_Hour = transitions[i].Transition_Hour,
        Transition_NP = transitions[i].Transition_NP, Transition_OG = transitions[i].Transition_OG,
        Transition_LG = transitions[i].Transition_LG, hdpe_Grade_Number_From = transitions[i].hdpe_Grade_Number_From,
        hdpe_Grade_Number_To = transitions[i].hdpe_Grade_Number_To, hdpe_Grade_Run = instance)


# generate HDPE_Last_Running_Grades based on previous months HDPE_Output_Summary

@receiver(post_save, sender=HDPE_Grade_Run)
def create_hdpe_last_running_grades(sender, instance, **kwargs):

    parent = HDPE_Grade_Run.objects.all().order_by('-id')[1]
    print (parent)    
    hdpe_Output_Summary = HDPE_Output_Summary.objects.filter(hdpe_Grade_Run = parent).get()
    print (hdpe_Output_Summary)

    HDPE_Last_Running_Grades.objects.create(hdpe_Output_Summary = hdpe_Output_Summary, hdpe_Grade_Run = instance)


###############generate HDPE_Last_Main_Grade#################

@receiver(post_save, sender=HDPE_Last_Running_Grades)
def create_hdpe_last_main_grade(sender, instance, **kwargs):

    trains = HDPE_Trains.objects.all()
    grades = HDPE_Grade_Number.objects.all()

    Grade_Hours_Completed = random.randint(10,20)
    Series_Parallel_Hours_Completed = random.randint(10,20)
    Family_Hours_Completed = random.randint(10,20)

    for i in range (0, len(trains)):
        HDPE_Last_Main_Grade.objects.create(Grade_Hours_Completed = Grade_Hours_Completed, 
        Series_Parallel_Hours_Completed = Series_Parallel_Hours_Completed, Family_Hours_Completed = Family_Hours_Completed,
        hdpe_Trains = trains[i], hdpe_Grade_Number = grades[i], hdpe_Last_Running_Grades = instance)

   
###############generate HDPE_Last_Transition_Grade#################

@receiver(post_save, sender=HDPE_Last_Running_Grades)
def create_hdpe_last_transition_grade(sender, instance, **kwargs):

    HDPE_Last_Transition_Grade.objects.create(Transition_Hours_Completed = None, hdpe_Trains = None,
    hdpe_Transition = None, hdpe_Last_Running_Grades = instance)

###############generate HDPE_Last_Maintenance#################

@receiver(post_save, sender=HDPE_Last_Running_Grades)
def create_hdpe_last_maintenance(sender, instance, **kwargs):

    HDPE_Last_Maintenance.objects.create(Maintenance_Hours_Left = None, hdpe_Trains = None,
    hdpe_Last_Running_Grades = instance)

###############generate HDPE_Last_Under_Restart#################

@receiver(post_save, sender=HDPE_Last_Running_Grades)
def create_hdpe_last_under_restart(sender, instance, **kwargs):

    HDPE_Last_Under_Restart.objects.create(Remaining_Hours_Max_TPH = None, hdpe_Trains = None,
    hdpe_Grade_Number = None, hdpe_Last_Running_Grades = instance)


# generate HDPE_Output_Summary by running the model

@receiver(post_save, sender=HDPE_Grade_Run)
def create_hdpe_output_summary(sender, instance, **kwargs):

    HDPE_Output_Summary.objects.create(hdpe_Grade_Run = instance)


###############generate HDPE_Output_Grade#################

@receiver(post_save, sender=HDPE_Output_Summary)
def create_hdpe_output_grade(sender, instance, **kwargs):

    output = HDPE_Sequence_Model.hdpe_output_grade(instance)
    trains = HDPE_Trains.objects.all()
    grades = HDPE_Grade_Number.objects.all()
    
    for i in range (0, len(trains)):
        for j in range (0, len(grades)):
            for day in range (0, 30):
                HDPE_Output_Grade.objects.create(Day = day+1, Production_Amount = output[i][j][day],
                hdpe_Trains = trains[i], hdpe_Grade_Number = grades[j], hdpe_Output_Summary = instance)
            

    

###############generate HDPE_Output_Transition#################

@receiver(post_save, sender=HDPE_Output_Summary)
def create_hdpe_output_transition(sender, instance, **kwargs):

    output = HDPE_Sequence_Model.hdpe_output_transition(instance)
    trains = HDPE_Trains.objects.all()
    transitions = HDPE_Transition.objects.all()
    
    for i in range (0, len(trains)):
        for j in range (0, len(transitions)):
            for day in range (0, 30):
                HDPE_Output_Transition.objects.create(Day = day+1, Transition_Amount = output[i][j][day],
                hdpe_Trains = trains[i], hdpe_Transition = transitions[j], hdpe_Output_Summary = instance)

###############generate HDPE_Output_NonPrime#################

@receiver(post_save, sender=HDPE_Output_Summary)
def create_hdpe_output_nonprime(sender, instance, **kwargs):

    output = HDPE_Sequence_Model.hdpe_output_nonprime(instance)
  
    for i in range (0, 30):
        HDPE_Output_NonPrime.objects.create(Day = i+1, NP_Production = output[0][i], OG_Production = output[1][i],
        LG_Production = output[2][i], Ethylene_Consumed = output[3][i], Propylene_Consumed = output[4][i], hdpe_Output_Summary = instance)









