from django.shortcuts import render
from TaskDz02.models import Order

# Create your views here.
def orders_by_client_and_date(request, id_client):
    orders = Order.objects.filter(buyer_user=id_client)

    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

    if date_from and date_to:
        orders = orders.filter(order_date__range=(date_from, date_to))

    orders = orders.order_by('order_date')

    context = {
        'orders': orders
    }

    return render(request, 'client.html', context)


def info_client(request):
    pass

def info_order(request):
    pass

def info_product(request):
    pass