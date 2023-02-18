from django.shortcuts import render
from .models import Food

# Create your views here.

def all_foods(request):
    """ A view to show all foods, including sorting and search queries """

    foods = Food.objects.all()

    context = {
        'foods': foods,
    }

    return render(request, 'foods/foods.html', context)