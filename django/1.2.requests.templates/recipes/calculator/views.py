from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def get_recipes(request, name: str):

    servings: int = int(request.GET.get("servings", 1))
    recipe: dict = {}

    for ingredient in DATA.get(name).keys():
        recipe[ingredient] = DATA.get(name).get(ingredient) * servings

    context = {
        'recipe': recipe
    }

    return render(request, 'calculator/index.html', context)
