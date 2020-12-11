from django.shortcuts import render
from learning_logs.models import Topic
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    """ The home page for learning logs """
    return render(request, 'learning_logs/index.html')

# @login_required
def topic(request, topic_id):
    """ Show a tpoic and all its entrirs """
    topic = Topic.objects.get(id=topic_id)
    # if topic.owner != request.user:
    #     raise Http404

    entries = topic.entry_set.order_by('date_added')
    context = {
        'topic' : topic,
        'entries' : entries
    }
    return render(request, 'learning_logs/topic.html', context)
