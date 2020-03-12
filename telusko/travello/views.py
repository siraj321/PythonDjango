from django.shortcuts import render

# Create your views here.
from travello.models import Destination


def index(request):

    """dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.price = 701
    dest1.img = 'destination_1.jpg'
    dest1.desc = 'The city that Never Sleeps.'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Mumbai2'
    dest2.price = 702
    dest2.img = 'destination_2.jpg'
    dest2.desc = 'The city that Never Sleeps.2'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Mumbai3'
    dest3.price = 703
    dest3.img = 'destination_3.jpg'
    dest3.desc = 'The city that Never Sleeps.3'
    dest3.offer = False

    dests = [dest1, dest2, dest3]"""

    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests':dests})