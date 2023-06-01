from django.shortcuts import render
from . models import offerOrder
# Create your views here.




def service(request):
    return render(request, 'service/service.html', {})
def web(request):
    if request.method == 'POST':
        bneed = request.POST['need']
        bpackage = request.POST['package']
        bname = request.POST['name']
        bmail = request.POST['mail']
        bsms = request.POST['sms']
        
        new_list = offerOrder(need = bneed, package = bpackage, name = bname, mail= bmail, sms=bsms)
        new_list.save()
    return render(request, 'service/web.html')
def app(request):
    if request.method == 'POST':
        need = request.POST['need']
        package = request.POST['package']
        name = request.POST['name']
        mail = request.POST['mail']
        sms = request.POST['sms']
        
        new_list = offerOrder(need = need, package = package, name = name, mail= mail, sms=sms)
        new_list.save()
    return render(request, 'service/app.html')
def seo(request):
    if request.method == 'POST':
        need = request.POST['need']
        package = request.POST['package']
        name = request.POST['name']
        mail = request.POST['mail']
        sms = request.POST['sms']
        
        new_list = offerOrder(need = need, package = package, name = name, mail= mail, sms=sms)
        new_list.save()
    return render(request, 'service/seo.html')

