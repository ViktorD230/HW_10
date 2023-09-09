from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .forms import AuthorForm, QuoteForm
from .models import Author, Tag, Quote

# Create your views here.
def main(request, page=1):
    quotes = Quote.objects.all()
    authors = Author.objects.all()
    tags = Tag.objects.all()
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quoteapp/index.html', {'quotes': quotes_on_page, 'authors': authors, 'tags': tags})


def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/author.html', {'form': form})

    return render(request, 'quoteapp/author.html', {'form': AuthorForm()})


def quote(request):
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        
        if form.is_valid():
            new_quote = form.save(commit=False)  # Создаем объект цитаты, но пока не сохраняем
            tags_input = form.cleaned_data['tags']  # Введенные пользователем теги

            tags_list = [tag.strip() for tag in tags_input.split(',')]  # Разделяем теги по запятой

            # Сохраняем цитату
            new_quote.author = form.cleaned_data['author']
            new_quote.save()

            # Добавляем теги, создавая их при необходимости
            for tag_name in tags_list:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                new_quote.tags.add(tag)
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/quote.html', {"authors": authors, 'form': form})

    return render(request, 'quoteapp/quote.html', {"authors": authors, 'form': QuoteForm()})

def author_about(request, fullname):
    author = get_object_or_404(Author, fullname=fullname)
    return render(request, 'quoteapp/author_about.html', {'author': author})
