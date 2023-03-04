from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('foods'))

    order_form = OrderForm()
    template = 'order/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)