from django.shortcuts import render, get_object_or_404
 
from .models import Post, Group
 
# Create your views here.
 
 
def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    title = 'Это главная страница проекта Yatube'
    text = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title,
        'text': text,
    }
    return render(request, 'posts/index.html', context)

 
def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title = 'Записи сообщества Лев Толстой – зеркало русской революции.'
    text = 'Лев Толстой – зеркало русской революции.'
    context = {
        'group': group,
        'posts': posts,
        'title': title,
        'text': text,
    }
    return render(request, 'posts/group_list.html', context)