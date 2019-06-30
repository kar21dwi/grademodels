from django.contrib import admin

from .models import HDPE_Grade_Run, HDPE_Trains, HDPE_Grade_Number, Contribution_Areas, HDPE_Demand_Pattern, HDPE_Demand_Stock
from .models import HDPE_TPH, HDPE_Contribution, HDPE_Minimum_Sales, HDPE_Maximum_Sales, HDPE_GM_Demand, HDPE_Restart_Parameters 
from .models import HDPE_Execution_Parameters, NCU_Parameters, NCU_Parameters_Stock, HDPE_Transition, HDPE_Output_Summary, HDPE_Grade_Activation
from .models import HDPE_Last_Running_Grades, HDPE_Last_Main_Grade, HDPE_Last_Transition_Grade, HDPE_Last_Maintenance, HDPE_Last_Under_Restart
from .models import HDPE_Output_Grade, HDPE_Output_Transition, HDPE_Output_NonPrime
# Register your models here.

admin.site.register(HDPE_Grade_Run)
admin.site.register(HDPE_Trains)
admin.site.register(HDPE_Grade_Number)
admin.site.register(Contribution_Areas)
admin.site.register(HDPE_Grade_Activation)
admin.site.register(HDPE_Demand_Pattern)
admin.site.register(HDPE_Demand_Stock)
admin.site.register(HDPE_TPH)
admin.site.register(HDPE_Contribution)
admin.site.register(HDPE_Minimum_Sales)
admin.site.register(HDPE_Maximum_Sales)
admin.site.register(HDPE_GM_Demand)
admin.site.register(HDPE_Restart_Parameters)
admin.site.register(HDPE_Execution_Parameters)
admin.site.register(NCU_Parameters)
admin.site.register(NCU_Parameters_Stock)
admin.site.register(HDPE_Transition)
admin.site.register(HDPE_Output_Summary)
admin.site.register(HDPE_Output_Grade)
admin.site.register(HDPE_Output_Transition)
admin.site.register(HDPE_Output_NonPrime)
admin.site.register(HDPE_Last_Running_Grades)
admin.site.register(HDPE_Last_Main_Grade)
admin.site.register(HDPE_Last_Transition_Grade)
admin.site.register(HDPE_Last_Maintenance)
admin.site.register(HDPE_Last_Under_Restart)


