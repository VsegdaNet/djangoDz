
from django.urls import path
from TaskDz01.views import HomeView, AboutView, log_visit


app_name = 'TaskDz01'

urlpatterns = [
    path('', HomeView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),
    path('visit/', log_visit, name="visit"),
]
