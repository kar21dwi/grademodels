from django.db import models

# Create your models here.

class HDPE_Grade_Run(models.Model):
    Model_Type = models.IntegerField()
    Exponential_Factor = models.FloatField()
    Decay_Factor = models.FloatField()
    Plan_Days = models.IntegerField()
    Sliding_Window = models.IntegerField()
    Series_Run = models.IntegerField()
    Parallel_Run = models.IntegerField()
    Date_Time = models.DateTimeField()
    Confirmation = models.BooleanField(default=False)
    Run_Name = models.TextField(null=True, blank=True)
    Run_Month = models.TextField(null=True, blank=True)
    Run_Year = models.TextField(null=True, blank=True)

    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_Grade_Run"
       

#Next_Hour_Selection Class
class HDPE_Trains(models.Model):
    Name = models.TextField()
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_Trains"

#Model_Output_Parameter_Running
class HDPE_Grade_Number(models.Model):
    Grade_Name = models.TextField()
    Restart_Grade = models.BooleanField()
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_Grade_Number"

#Tank Class
class Contribution_Areas(models.Model):
    Area_Name = models.TextField()

    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Contribution_Areas"


class HDPE_Grade_Activation(models.Model):
    Active_Status = models.BooleanField()
    hdpe_Grade_Number = models.ForeignKey(HDPE_Grade_Number,on_delete =models.CASCADE)
    hdpe_Grade_Run = models.ForeignKey(HDPE_Grade_Run,on_delete =models.CASCADE)  

    objects = models.Manager() 
    class Meta:
       verbose_name_plural = "HDPE_Grade_Activation" 


class HDPE_Demand_Pattern(models.Model):
    Day = models.IntegerField()
    Demand_Percentage = models.FloatField()
    hdpe_Grade_Number = models.ForeignKey(HDPE_Grade_Number,on_delete =models.CASCADE)
    hdpe_Grade_Run = models.ForeignKey(HDPE_Grade_Run,on_delete =models.CASCADE)

    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_Demand_Pattern"   


class HDPE_Demand_Stock(models.Model):
    Demand = models.FloatField()
    Opening_Inventory = models.FloatField()
    Closing_Inventory = models.FloatField()
    hdpe_Grade_Number = models.ForeignKey(HDPE_Grade_Number,on_delete =models.CASCADE)
    hdpe_Grade_Run = models.ForeignKey(HDPE_Grade_Run,on_delete =models.CASCADE)

    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_Demand_Stock"        


class HDPE_TPH(models.Model):
    Train_TPH = models.FloatField()
    Minimum_Batch_Size = models.FloatField()
    C2_Percentage = models.FloatField()
    C3_Percentage = models.FloatField()
    hdpe_Trains = models.ForeignKey(HDPE_Trains,on_delete =models.CASCADE)
    hdpe_Grade_Number = models.ForeignKey(HDPE_Grade_Number,on_delete =models.CASCADE)
    hdpe_Grade_Run = models.ForeignKey(HDPE_Grade_Run,on_delete =models.CASCADE)

    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_TPH" 


class HDPE_Contribution(models.Model):
    Contribution_Amount = models.FloatField()
    contribution_Areas = models.ForeignKey(Contribution_Areas,on_delete =models.CASCADE)
    hdpe_Grade_Number = models.ForeignKey(HDPE_Grade_Number,on_delete =models.CASCADE)
    hdpe_Grade_Run = models.ForeignKey(HDPE_Grade_Run,on_delete =models.CASCADE)
   
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_Contribution" 


class HDPE_Minimum_Sales(models.Model):
    Minimum_Sales_Amount = models.FloatField()
    contribution_Areas = models.ForeignKey(Contribution_Areas,on_delete =models.CASCADE)
    hdpe_Grade_Number = models.ForeignKey(HDPE_Grade_Number,on_delete =models.CASCADE)
    hdpe_Grade_Run = models.ForeignKey(HDPE_Grade_Run,on_delete =models.CASCADE)

    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_Minimum_Sales"   


class HDPE_Maximum_Sales(models.Model):
    Maximum_Sales_Amount = models.FloatField()
    contribution_Areas = models.ForeignKey(Contribution_Areas,on_delete =models.CASCADE)
    hdpe_Grade_Number = models.ForeignKey(HDPE_Grade_Number,on_delete =models.CASCADE)
    hdpe_Grade_Run = models.ForeignKey(HDPE_Grade_Run,on_delete =models.CASCADE)

    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_Maximum_Sales"   


class HDPE_GM_Demand(models.Model):
    GM_Demand = models.FloatField()
    hdpe_Grade_Number = models.ForeignKey(HDPE_Grade_Number,on_delete =models.CASCADE)
    hdpe_Grade_Run = models.ForeignKey(HDPE_Grade_Run,on_delete =models.CASCADE)
    contribution_Areas = models.ForeignKey(Contribution_Areas,on_delete =models.CASCADE)
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_GM_Demand" 


class HDPE_Restart_Parameters(models.Model):
    Hours_Prime_Production = models.FloatField()
    Avg_TPH = models.FloatField()
    NP_Amount = models.FloatField()
    OG_Amount = models.FloatField()
    LG_Amount = models.FloatField()
    hdpe_Grade_Number = models.ForeignKey(HDPE_Grade_Number,on_delete =models.CASCADE)
    hdpe_Grade_Run = models.ForeignKey(HDPE_Grade_Run,on_delete =models.CASCADE)

    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_Restart_Parameters"     


class HDPE_Execution_Parameters(models.Model):
    Start_Date_Time = models.DateTimeField(blank = True, null = True)
    Duration = models.IntegerField()
    Maintenance_Start_Day = models.IntegerField()
    Maintenance_Start_Hour = models.IntegerField()
    Maintenance_Duration = models.IntegerField()
    Initial_Maintenance_Duration = models.IntegerField()
    Allowable_Days = models.IntegerField()
    Allowable_Hours = models.IntegerField()
    Difference_Days = models.IntegerField()
    Difference_Hours = models.IntegerField()
    hdpe_Trains = models.ForeignKey(HDPE_Trains,on_delete =models.CASCADE)
    hdpe_Grade_Run = models.ForeignKey(HDPE_Grade_Run,on_delete =models.CASCADE)

    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_Execution_Parameters"    


class NCU_Parameters(models.Model):
    NCU_Load = models.FloatField()
    Ethylene_Yield = models.FloatField()
    Propylene_Yield = models.FloatField()
    Day = models.IntegerField()
    hdpe_Grade_Run = models.ForeignKey(HDPE_Grade_Run,on_delete =models.CASCADE)

    objects = models.Manager()
    class Meta:
       verbose_name_plural = "NCU_Parameters"     


class NCU_Parameters_Stock(models.Model):
    Ethylene_Opening_Stock = models.FloatField()
    Ethylene_Closing_Stock = models.FloatField()
    Propylene_Opening_Stock = models.FloatField()
    Propylene_Closing_Stock = models.FloatField()
    hdpe_Grade_Run = models.ForeignKey(HDPE_Grade_Run,on_delete =models.CASCADE)

    objects = models.Manager()
    class Meta:
       verbose_name_plural = "NCU_Parameters_Stock"     


class HDPE_Transition(models.Model):
    Transition_TPH = models.FloatField()
    Transition_Hour = models.IntegerField()
    Transition_NP = models.FloatField()
    Transition_OG = models.FloatField()
    Transition_LG = models.FloatField()
    hdpe_Grade_Number_From = models.ForeignKey(HDPE_Grade_Number,on_delete =models.CASCADE, null=True, related_name='hdpe_Grade_Number_From')
    hdpe_Grade_Number_To = models.ForeignKey(HDPE_Grade_Number,on_delete =models.CASCADE, null=True, related_name='hdpe_Grade_Number_To')
    hdpe_Grade_Run = models.ForeignKey(HDPE_Grade_Run,on_delete =models.CASCADE)

    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_Transition" 

#------------------Output Models---------------------#

class HDPE_Output_Summary(models.Model):
    hdpe_Grade_Run = models.OneToOneField(HDPE_Grade_Run,on_delete =models.CASCADE)
   
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_Output_Summary"    


class HDPE_Output_Grade(models.Model):

    Day = models.IntegerField()
    Production_Amount = models.FloatField()
    hdpe_Trains = models.ForeignKey(HDPE_Trains, on_delete =models.CASCADE)
    hdpe_Grade_Number = models.ForeignKey(HDPE_Grade_Number, on_delete =models.CASCADE)
    hdpe_Output_Summary = models.ForeignKey(HDPE_Output_Summary, on_delete =models.CASCADE)
   
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_Output_Grade"  


class HDPE_Output_Transition(models.Model):
    
    Day = models.IntegerField()
    Transition_Amount = models.FloatField()
    hdpe_Trains = models.ForeignKey(HDPE_Trains, on_delete =models.CASCADE)
    hdpe_Transition = models.ForeignKey(HDPE_Transition, on_delete =models.CASCADE)
    hdpe_Output_Summary = models.ForeignKey(HDPE_Output_Summary, on_delete =models.CASCADE)
   
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_Output_Transition"  


class HDPE_Output_NonPrime(models.Model):
   
    Day = models.IntegerField()
    NP_Production = models.FloatField()
    OG_Production = models.FloatField()
    LG_Production = models.FloatField()
    Ethylene_Consumed = models.FloatField()
    Propylene_Consumed = models.FloatField()
    hdpe_Output_Summary = models.ForeignKey(HDPE_Output_Summary, on_delete =models.CASCADE)
   
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_Output_NonPrime"                

#------------------Output Models---------------------#

class HDPE_Last_Running_Grades(models.Model):
    hdpe_Grade_Run = models.OneToOneField(HDPE_Grade_Run,on_delete =models.CASCADE)
    hdpe_Output_Summary = models.OneToOneField(HDPE_Output_Summary,on_delete =models.CASCADE)
   
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_Last_Running_Grades"  


class HDPE_Last_Main_Grade(models.Model):

    Grade_Hours_Completed = models.FloatField()
    Series_Parallel_Hours_Completed = models.FloatField()
    Family_Hours_Completed = models.FloatField()
    hdpe_Trains = models.ForeignKey(HDPE_Trains, on_delete =models.CASCADE)
    hdpe_Grade_Number = models.ForeignKey(HDPE_Grade_Number, on_delete =models.CASCADE) 
    hdpe_Last_Running_Grades = models.ForeignKey(HDPE_Last_Running_Grades,on_delete =models.CASCADE)
   
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_Last_Main_Grade" 


class HDPE_Last_Transition_Grade(models.Model):
    Transition_Hours_Completed = models.FloatField(null=True, blank=True)
    hdpe_Trains = models.ForeignKey(HDPE_Trains, on_delete =models.CASCADE, null=True, blank=True)
    hdpe_Transition = models.ForeignKey(HDPE_Transition, on_delete =models.CASCADE, null=True, blank=True) 
    hdpe_Last_Running_Grades = models.ForeignKey(HDPE_Last_Running_Grades,on_delete =models.CASCADE)
   
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_Last_Transition_Grade"


class HDPE_Last_Maintenance(models.Model):
    Maintenance_Hours_Left = models.FloatField(null=True, blank=True)
    hdpe_Trains = models.ForeignKey(HDPE_Trains, on_delete =models.CASCADE, null=True, blank=True)
    hdpe_Last_Running_Grades = models.ForeignKey(HDPE_Last_Running_Grades,on_delete =models.CASCADE)
   
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_Last_Maintenance"  


class HDPE_Last_Under_Restart(models.Model):
    Remaining_Hours_Max_TPH = models.FloatField(null=True, blank=True)
    hdpe_Trains = models.ForeignKey(HDPE_Trains, on_delete =models.CASCADE, null=True, blank=True)
    hdpe_Grade_Number = models.ForeignKey(HDPE_Grade_Number, on_delete =models.CASCADE, null=True, blank=True)
    hdpe_Last_Running_Grades = models.ForeignKey(HDPE_Last_Running_Grades,on_delete =models.CASCADE)
   
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "HDPE_Last_Under_Restart"                                                                                                                                               