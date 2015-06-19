from django.shortcuts import render
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView, TemplateView)
from django.db.models import Max, F
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from main.models import Intern, Late


""" class that creates a form for creating an instance of Intern"""
class InternCreate(CreateView):
    model = Intern
    fields = ['name']
    template_name = 'main/intern_form.html'
    success_url = reverse_lazy('main:intern_list')


""" class that shows the details of a specific instance of Intern, 
    and the Late instances associated with it (arrivals)"""

class InternDetailView(DetailView):
    model = Intern

    def arrivals(self):
        return Late.objects.filter(name_id=self.kwargs['pk'])


"class that lists all the created instances of Intern"

class InternListView(ListView):
    model = Intern


"class that deletes a specific instance of Intern"

class InternDelete(DeleteView):
    model = Intern
    success_url = reverse_lazy('main:intern_list')


""" class that creates a form for creating an instance of Late"""

class LateCreate(CreateView):
    model = Late
    fields = ['name']
    template_name = 'main/late_form.html'

    # """ prevents the form from saving before setting
    # the payment to be double the last/max payment of the
    # same intern"""
    # def form_valid(self, form):
    #     amount = form.save(commit=False)
    #     i = Intern.objects.get(name_id=self.id)
    #     pay = i.late_set.all().aggregate(payment=Max('payment'))
    #     amount.payment = pay.payment *2
    #     amount.save()
    #     return HttpResponseRedirect(amount.get_absolute_url())


"""class that shows details of a specific Late instance"""

class LateDetailView(DetailView):
    model = Late

