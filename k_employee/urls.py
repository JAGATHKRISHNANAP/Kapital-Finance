from django.urls import path
from k_employee.views import *
urlpatterns = [
    path('custreg/',loadcustRegpage,name="custfrm"),
    path('custregAct/',custregAction, name="custregAct"),
    path('emphome/',emphomePage,name="emphome"),
    path('home/',homePage, name="home"),
    path('empprofile/',loadEmpProfile,name="eprofile"),
    # path('loginAct/',loginaction,name="loginAct")

    # path('customerdel/',custdelAction,name="customerdel")
    ]