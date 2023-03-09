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
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            food = form.save()
            messages.success(request, 'Menu successfully updated!')
            return redirect(reverse('food_detail', args=[food.id]))
        else:
            messages.error(request, 'Failed to update menu. Please ensure the form is valid.')
    else:
        form = FoodForm()
        
    template = 'foods/add_food.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_food(request, food_id):
    """ Edit food in the store """
    food = get_object_or_404(Food, pk=food_id)
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update Successful!')
            return redirect(reverse('food_detail', args=[food.id]))
        else:
            messages.error(request, 'Updated Failed. Please ensure the form is valid.')
    else:
        form = FoodForm(instance=product)
        messages.info(request, f'You are editing {food.name}')

    template = 'foods/edit_food.html'
    context = {
        'form': form,
        'food': food,
    }

    return render(request, template, context)


def delete_food(request, food_id):
    """ Delete food from the store """
    food = get_object_or_404(Food, pk=food_id)
    food.delete()
    messages.success(request, 'Food deleted!')
    return redirect(reverse('foods'))