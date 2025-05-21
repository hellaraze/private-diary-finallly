from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Entry, Category, Tag
from .forms import EntryForm
from django.db.models import Q # <--- ДОБАВЬ ЭТОТ ИМПОРТ

@login_required
def entry_list(request):
    # Получаем поисковый запрос из GET-параметра 'q'
    search_query = request.GET.get('q', None) # Если 'q' нет, search_query будет None

    # Начальный queryset - записи текущего пользователя
    entries = Entry.objects.filter(author=request.user)

    # Если поисковый запрос есть, фильтруем queryset
    if search_query:
        entries = entries.filter(
            Q(title__icontains=search_query) | # Ищем в заголовке (без учета регистра)
            Q(content__icontains=search_query)  # ИЛИ в содержимом (без учета регистра)
        ).distinct() # distinct() чтобы не было дубликатов, если слово есть и в заголовке, и в тексте

    # Сортируем результат (либо полный список, либо отфильтрованный)
    entries = entries.order_by('-created')

    # Остальные данные для контекста
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'entries': entries,
        'categories': categories,
        'tags': tags,
        'search_query': search_query # Передаем поисковый запрос в шаблон
    }
    return render(request, 'diary/entry_list.html', context)

# Остальные твои функции (entry_detail, entry_create, entry_edit, entry_delete) остаются БЕЗ ИЗМЕНЕНИЙ
# Я их здесь не повторяю для краткости, но они должны остаться в файле такими, какими были.

@login_required
def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk, author=request.user)
    return render(request, 'diary/entry_detail.html', {'entry': entry})

@login_required
def entry_create(request):
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.save()
            form.save_m2m()
            return redirect('entry_list')
    else:
        form = EntryForm()
    return render(request, 'diary/entry_form.html', {'form': form})

@login_required
def entry_edit(request, pk):
    entry = get_object_or_404(Entry, pk=pk, author=request.user)
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry_detail', pk=pk)
    else:
        form = EntryForm(instance=entry)
    return render(request, 'diary/entry_form.html', {'form': form})

@login_required
def entry_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk, author=request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('entry_list')
    return render(request, 'diary/entry_confirm_delete.html', {'entry': entry})