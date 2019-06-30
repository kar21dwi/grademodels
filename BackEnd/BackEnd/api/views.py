from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
#from .serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import HttpResponse
import json
import ast
import random
from datetime import datetime

from .models import HDPE_Grade_Run, HDPE_Trains, HDPE_Grade_Number, Contribution_Areas, HDPE_Demand_Pattern, HDPE_Demand_Stock
from .models import HDPE_TPH, HDPE_Contribution, HDPE_Minimum_Sales, HDPE_Maximum_Sales, HDPE_GM_Demand, HDPE_Restart_Parameters 
from .models import HDPE_Execution_Parameters, NCU_Parameters, NCU_Parameters_Stock, HDPE_Transition, HDPE_Output_Summary, HDPE_Grade_Activation
from .models import HDPE_Last_Running_Grades, HDPE_Last_Main_Grade, HDPE_Last_Transition_Grade, HDPE_Last_Maintenance, HDPE_Last_Under_Restart

# update current confirmation status of hdpe_grade_run

@csrf_exempt
def updateGradeRun(request):
      
      parent_obj = HDPE_Grade_Run.objects.all().order_by('-id')[0] 
      HDPE_Grade_Run.objects.filter(pk=parent_obj.id).update(Confirmation = True)  
  

      return JsonResponse('Done', safe = False, status=status.HTTP_201_CREATED)
