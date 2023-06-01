from django.shortcuts import render
from service.models import offerOrder
# Create your views here.

def contact(request):
    if request.method == 'POST':
        need = request.POST['need']
        package = request.POST['package']
        name = request.POST['name']
        mail = request.POST['mail']
        sms = request.POST['sms']
        
        new_list = offerOrder(need = need, package = package, name = name, mail= mail, sms=sms)
        new_list.save()
    return render(request, 'contact/contact.html') 