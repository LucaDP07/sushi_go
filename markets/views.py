from django.shortcuts import render, get_list_or_404
from .models import Market


def markets_all(request):
    """
    Get all markets and return template.
    """
    markets = get_list_or_404(Market)

    context = {
        'markets': markets,
    }

    return render(request, 'markets/markets.html', context)
