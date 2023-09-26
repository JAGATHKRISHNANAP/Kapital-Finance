from django.shortcuts import render
from k_employee.models import *
from k_admin.models import *
# Create your views here.
def loadcustRegpage(request):
    return render(request,"customer.html")
def emphomePage(request):
    return render(request,"emphome.html")
def homePage(request):
    return render(request,"home.html")
# def emplogin(request):
#     return render(request,"")

def custregAction(request):
    if request.method=="POST":

        msg=""
        cu_name = request.POST["name"]
        cu_age = request.POST["age"]
        cu_address = request.POST["address"]
        cu_mob=request.POST["mob"]
        cu_email = request.POST["email"]
        cu_bank = request.POST["bank"]
        cu_branch = request.POST["branch"]
        cu_ifsc = request.POST["ifsc"]
        cu_acc = request.POST["acc_no"]
        cu_duration = request.POST["loanduration"]
        cu_approveddate = request.POST["loanapprove"]
        cu_loanamount = request.POST["loanamount"]
        cu_cloan=request.POST["currentamont"]
        cu_emi = request.POST["emi"]
        cust=customer(name=cu_name, age=cu_age, adress=cu_address,mob=cu_mob,email=cu_email,bank=cu_bank,branch=cu_branch,ifsc=cu_ifsc,acc_no=cu_acc,loanduration=cu_duration,loanapprove=cu_approveddate,loanamount=cu_loanamount,emi=cu_emi)
        cust.save()
        if cust:
            msg = "success"
        else:
            msg = "failed"
        return render(request,"customer.html", {"m": msg})

def loadEmpProfile(request):
    empid=request.session["userid"]
    empdetails=empreg.objects.get(id=empid)

    return render(request,"empprofile.html",{"details":empdetails})

