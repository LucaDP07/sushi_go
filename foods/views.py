from django.shortcuts import render, get_object_or_404
from .models import Food


def all_foods(request):
    """ A view to show all foods, including sorting and search queries """

    foods = Food.objects.all()

    context = {
        'foods': foods,
    }

    return render(request, 'foods/foods.html', context)

def food_detail(request, food_id):
    """ A view to show individual food details """

    food = get_object_or_404(Food, pk=food_id)

    context = {
        'food': food,
    }

    return render(request, 'foods/food_detail.html', context)