from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import EmailEntry
from .tasks import send_scheduled_mail
from django.urls import reverse_lazy
from .forms import SendMailForm

from datetime import datetime


class CreateMail(LoginRequiredMixin, CreateView):
    model = EmailEntry
    success_url = reverse_lazy('mail_app:send_mail')
    form_class = SendMailForm
    template_name = 'mail_app/send_mail.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        mail = form.save()
        send_time = mail.sent_datetime
        send_scheduled_mail.apply_async((mail.id,), eta=send_time)
        return super().form_valid(form)
