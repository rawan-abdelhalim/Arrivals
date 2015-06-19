from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import Max


class Intern (models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:intern_detail', kwargs={'pk': self.pk})

    def get_payment(self):
        return self.late_set.all().aggregate(payment=Max('payment'))['payment']



class Late (models.Model):
    name = models.ForeignKey('Intern')
    arrived = models.DateTimeField(auto_now_add=True)
    payment = models.IntegerField(default=10)

    def __unicode__(self):
        return "Arrived on %s. Payment = %s" % (self.arrived, self.payment)

    def get_absolute_url(self):
        return reverse('main:late_detail', kwargs={'pk': self.pk})


