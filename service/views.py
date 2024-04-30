from service.models import Client, Message, Mailing, Attempt
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ClientListView(ListView):
    model = Client
    fields = ['email', 'first_name', 'last_name', 'comment']
    template_name = 'service/client_list.html'
    extra_context = {'title': 'Клиенты'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ClientDetailView(DetailView):
    model = Client
    fields = ['email','first_name', 'last_name', 'comment']
    template_name = 'service/client_detail.html'
    success_url = reverse_lazy('service:client_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_item = self.get_object()
        context['title'] = client_item.first_name
        return context


class ClientCreateView(CreateView):
    model = Client
    fields = ['email', 'first_name', 'last_name', 'comment']
    template_name = 'service/client_from.html'
    success_url = reverse_lazy('service:client_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание клиента'
        return context


class ClientUpdateView(UpdateView):
    model = Client
    fields = ['email','first_name', 'last_name', 'comment']
    template_name = 'service/client_from.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_item = self.get_object()
        context['title'] = client_item.first_name
        return context


class ClientDeleteView(DeleteView):
    model = Client
    fields = ['email', 'first_name', 'last_name', 'comment']
    template_name = 'service/client_confirm_delete.html'
    success_url = reverse_lazy('service:client_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_item = self.get_object()
        context['title'] = client_item.first_name
        return context


class MessageListView(ListView):
    model = Message
    fields = ['subject', 'text', 'picture']
    template_name = 'service/message_list.html'
    extra_context = {'title': 'Сообщения'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MessageDetailView(DetailView):
    model = Message
    fields = ['subject', 'text', 'picture']
    template_name = 'service/message_detail.html'
    success_url = reverse_lazy('service:message_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        message_item = self.get_object()
        context['title'] = message_item.subject
        return context


class MessageCreateView(CreateView):
    model = Message
    fields = ['subject', 'text', 'picture']
    template_name = 'service/message_from.html'
    success_url = reverse_lazy('service:message_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание сообщения'
        return context


class MessageUpdateView(UpdateView):
    model = Message
    fields = ['subject', 'text', 'picture']
    template_name = 'service/message_from.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        message_item = self.get_object()
        context['title'] = message_item.subject
        return context


class MessageDeleteView(DeleteView):
    model = Message
    fields = ['subject', 'text', 'picture']
    template_name = 'service/message_confirm_delete.html'
    success_url = reverse_lazy('service:message_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        message_item = self.get_object()
        context['title'] = message_item.subject
        return context


class MailingView(ListView):
    model = Mailing
    fields = ['time_sending', 'time_end', 'periodicity', 'status', 'clients']
    template_name = 'service/mailing_list.html'
    extra_context = {'title': 'Рассылка'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MailingDetailView(DetailView):
    model = Mailing
    fields = ['time_sending', 'time_end', 'periodicity','status', 'clients']
    template_name = 'service/mailing_detail.html'
    success_url = reverse_lazy('service:mailing_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mailing_item = self.get_object()
        context['title'] = mailing_item.time_sending
        return context


class MailingCreateView(CreateView):
    model = Mailing
    fields = ['time_sending', 'time_end', 'periodicity','status', 'clients']
    template_name = 'service/mailing_from.html'
    success_url = reverse_lazy('service:mailing_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание рассылки'
        return context


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ['time_sending', 'time_end', 'periodicity','status', 'clients']
    template_name = 'service/mailing_from.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mailing_item = self.get_object()
        context['title'] = mailing_item.time_sending
        return context


class MailingDeleteView(DeleteView):
    model = Mailing
    fields = ['time_sending', 'time_end', 'periodicity','status', 'clients']
    template_name = 'service/mailing_confirm_delete.html'
    success_url = reverse_lazy('service:mailing_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mailing_item = self.get_object()
        context['title'] = mailing_item.time_sending
        return context


class AttemptView(ListView):
    model = Attempt
    fields = ['status']
    template_name = 'service/attempt_list.html'
    extra_context = {'title': 'Попытки'}


