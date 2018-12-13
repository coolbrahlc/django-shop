from django.shortcuts import render
from .forms import SubscriberForm

def landing(request):

    vari = ' texting '

    form = SubscriberForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():        # !!!!!!!!!!!!!!!!!!! Консольный вывод
        print(request.POST)  # print(form)                  # !!!!!!!!!!!!!!!!!!!
        data = form.cleaned_data                            # !!!!!!!!!!!!!!!!!!!
        print(data['name'])

        new_form = form.save()

    return render(request, 'landing/landing.html', locals())