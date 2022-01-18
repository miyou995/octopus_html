from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.views.generic.base import RedirectView
from .models import Quote, Service, Contact, Client
from .forms  import ContactForm
from django.core.mail import EmailMessage
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.filter(priority__range=[1,6])
        context["quotes"] = Quote.objects.all()
        return context
    
#  STATIC
class ServiceDetailView(DetailView):
    model = Service
    template_name = "service-detail.html"

class ServicesListView(ListView):
    model = Service
    context_object_name = "services"

    template_name = "services.html"


class AboutView(TemplateView):
    template_name = "about.html"

  

class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('message')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print('je usi cand le dofrm')
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipients = ['hello@octopus-consulting.com']
            body = 'Nom: {} \n email: {} \n Phone:{} \n Sujet: {} \n Message: {}' .format(name, email, phone, subject, message)
            mail = EmailMessage('Cet email est envoyer depuis le site internet', body, 'octopus.emailing@gmail.com', recipients) 
            Contact.objects.create(name= name ,email= email ,phone= phone ,subject= subject ,message = message )
            try:
                mail.send()
                return HttpResponse('Merci ! votre message a été envoyer avec succée')
            except:
                return HttpResponse('Oups ! une erreur est survenue, veuiller vérifier vos informations SVP.')
        else :
            return HttpResponse('Oups ! veuiller vérifier vos informations SVP.')


