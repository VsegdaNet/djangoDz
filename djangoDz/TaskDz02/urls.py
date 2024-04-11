
from django.urls import path
from TaskDz02.views import orders_by_client_and_date

app_name = 'TaskDz01'

urlpatterns = [
    path('<int:id_client>', orders_by_client_and_date, name='client'),
]
