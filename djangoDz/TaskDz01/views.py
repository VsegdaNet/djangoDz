from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages import get_messages

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['html'] = """
        <h1>Добро пожаловать на мой первый Django-сайт!</h1>
        <p>Это моя первая страница на Django. Здесь вы найдете информацию о моем сайте и обо мне.</p>
        """
        return context

class AboutView(LoginRequiredMixin, TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['html'] = """
        <h1>Обо мне</h1>
        <p>Привет! Меня зовут [Ваше имя] и я создал этот сайт для того, чтобы поделиться своими знаниями о Django и Python.</p>
        """
        return context

def log_visit(request):
    messages.info(request, 'Вы посетили страницу.')
    return HttpResponse('')