from django.urls import path
from k_telicaller.views import *
# from k_employee.views import *
urlpatterns = [
    # path('custdl/', custRegForm, name="custregfrm"),
    path('telehome/',telehomePage,name="telehome"),
    path('custMDEL/<int:cust_id>/',loadcustMDEL,name="custMDEL"),
    path('callpage/',custcallPage,name="calldetails"),
    path('telefeedAct/',loadteleFD,name="telefeedAct"),
    path('telefeedEditAct/',loadteleEditFD,name="telefeedEditAct"),
    path('teleprofile/',loadteleProfile,name="tprofile"),


    ]