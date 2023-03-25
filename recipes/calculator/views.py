from django.shortcuts import render
from django.http import HttpResponse


def omlet(request):
    srv = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'яйца, шт': 2 * srv,
            'молоко, л': 0.1 * srv,
            'соль, ч.л.': 0.5 * srv,
        },
        'servings' : srv,
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    srv = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'макароны, г': 0.3 * srv,
            'сыр, г': 0.05 * srv,
        },
    }
    return render(request, 'calculator/index.html', context)


def buter(request):
    srv = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'хлеб, ломтик': 1 * srv,
            'колбаса, ломтик': 1 * srv,
            'сыр, ломтик': 1 * srv,
            'помидор, ломтик': 1 * srv,
        },
    }
    return render(request, 'calculator/index.html', context)

