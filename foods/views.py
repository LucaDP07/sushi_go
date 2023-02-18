from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Food


def all_foods(request):
    """ A view to show all foods, including sorting and search queries """

    foods = Food.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria yet!")
                return redirect(reverse('foods'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        foods = foods.filter(queries)

    context = {
        'foods': foods,
        'search_term': query,
    }

    return render(request, 'foods/foods.html', context)

def food_detail(request, food_id):
    """ A view to show individual food details """

    food = get_object_or_404(Food, pk=food_id)

    context = {
        'food': food,
    }

    return render(request, 'foods/food_detail.html', context)