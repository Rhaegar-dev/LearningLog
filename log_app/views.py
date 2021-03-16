from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse 

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    return render(request, 'index.html')


def topics(request):
    tps = Topic.objects.order_by('date_added')
    context = {'topics': tps}
    return render(request, 'topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries':entries}
    return render(request, 'topic.html', context)

# to est est view obrabot4ik query i v ntvvm vyzyvaetsa object form lalala
#vyzov form iz view ski vyzov formi i peredacha object v nee object Form in dj 
# ne odno i tozh s form on web
def new_topic(request):
    
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
    
    context = {'form': form}
    return render(request, 'new_topic.html', context)

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        form = EntryForm
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            #commit false нужен чтобы создать нью обжект но не помещать пока в базу данных
            new_entry = form.save(commit=False)
            new_entry.topic = topic 
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'new_entry.html', context)

def edit_entry(request, entry_id):
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # instance приказывает джанге создать форму заранее заполненную информацией из существующего объекта
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'edit_entry.html', context)

# lj,bnm уже это радактирование записей две страницы всего ммм давить мнияяааа шшшш чуть чуть
# адски сложно тяжело ужасно кошмар смерть