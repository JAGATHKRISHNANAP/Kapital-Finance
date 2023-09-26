from django.shortcuts import render,redirect
from k_employee.models import *
from k_admin.models import *
from .models import *
# # Create your views here.
def telehomePage(request):
    return render(request,"telehome.html")

def custcallPage(request):

    telefb_list=telefb.objects.all()
    cus_list=customer.objects.all().exclude(id__in=telefb_list.values('cust'))
    print(cus_list)
    # {"details": custdetails}
    return render(request,"calldetails.html",{"customer":cus_list,"addedfb":telefb_list})
# def submitAction(request):

def loadcustMDEL(request,cust_id):
    custdetails=customer.objects.get(id=cust_id)
    return render(request,"custMDEL.html",{"cust":custdetails})

def loadteleFD(request):
    if request.method == "POST":
        tele_feedback=request.POST["feedback"]
        custid=request.POST["custid"]
        teleid=request.session["userid"]
        cusobj=customer.objects.get(id=custid)
        empobj=empreg.objects.get(id=teleid)
        cust = telefb(feedback=tele_feedback,cust=cusobj,emp=empobj)
        cust.save()

        if cust:
            msg = "success"
        else:
            msg = "failed"


        return redirect("calldetails")


def loadteleEditFD(request):
    if request.method == "POST":
        tele_feedback=request.POST["feedback"]
        feed_id=request.POST["feedid"]

        feedobj = telefb.objects.get(id=feed_id)
        feedobj.feedback=tele_feedback
        feedobj.save()

        if feedobj:
            msg = "success"
        else:
            msg = "failed"

        # return render(request,"calldetails.html",{"m": msg})
        return redirect("calldetails")

def loadteleProfile(request):
    empid=request.session["userid"]
    empdetails=empreg.objects.get(id=empid)

    return render(request,"teleprofile.html",{"details":empdetails})