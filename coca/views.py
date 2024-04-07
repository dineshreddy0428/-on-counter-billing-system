from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def gen_pdf(request):
    if request.method =='POST':
        TV=request.POST['TV']
        JBL=request.POST['JBL']
        AIR=request.POST['AIR']
        PRO11=request.POST['PRO11']
        Fanta=request.POST['Fanta']
        Iphone14=request.POST['Iphone14']
        Limca=request.POST['Limca']
        shake=request.POST['shake']
        dt=request.POST['dt']
        if int(TV)<0 or int(JBL)<0 or int(AIR)<0 or int(PRO11)<0 or int(Fanta)<0 or int(Iphone14)<0 or int(Limca)<0 or int(shake)<0:
            return HttpResponse("<h1>items cannot be negative</h1>")
        TV_rt=50000
        JBL_rt=30000
        AIR_rt=100000
        PRO11_rt=20000
        Fanta_rt=100
        Iphone14_rt=40000
        Limca_rt=100
        shake_rt=2000
        total=(int(TV)*TV_rt+int(JBL)*JBL_rt+int(AIR)*AIR_rt+int(PRO11)*PRO11_rt+int(Fanta)*Fanta_rt+int(Iphone14)*Iphone14_rt+int(Limca)*Limca_rt+int(shake)*shake_rt)
        return render(request,'pdf.html',{'TV':TV,'JBL':JBL,'AIR':AIR,'PRO11':PRO11,'Fanta':Fanta,'Iphone14':Iphone14,'Limca':Limca,'shake':shake,'dt':dt,'total':total})
    return render(request,'index.html')
