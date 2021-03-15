from django.shortcuts import render
from .models import Topic
# Create your views here.

def index(request):
    return render(request, 'index.html')

# вывести список тем вывести
def topics(request):
    tps = Topic.objects.order_by('date_added')
    context = {'topics': tps}
    return render(request, 'topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries':entries}
    return render(request, 'topic.html', context)

