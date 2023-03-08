from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Food, Category
from .forms import FoodForm


def all_foods(request):
    """ A view to show all foods, including sorting and search queries """

    foods = Food.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            foods = foods.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter your search criteria!")
                return redirect(reverse('foods'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            foods = foods.filter(queries)

    context = {
        'foods': foods,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'foods/foods.html', context)


def food_detail(request, food_id):
    """ A view to show individual food details """

    food = get_object_or_404(Food, pk=food_id)

    context = {
        'food': food,
    }

    return render(request, 'foods/food_detail.html', context)


def add_food(request):
    """ Add food to the menu """
    form = FoodForm()
    template = 'foods/add_food.html'
    context = {
        'form': form,
    }

    return render(request, template, context)