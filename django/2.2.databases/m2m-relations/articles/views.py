from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    ordering = '-published_at'
    template = 'articles/news.html'
    context = {'object_list': Article.objects.all().order_by(ordering)}

    return render(request, template, context)
