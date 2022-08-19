from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index (request):

    # we defined our own temporary dataset
    meetups = [

        {
        'title': 'A First Meetup',
        'location': 'New York',
        'slug': 'a-first-meetup'
        },
        {
        'title': 'A Second Meetup',
        'location': 'Chicago',
        'slug': 'a-second-meetup'
        },
        {
        'title': 'A Third Meetup',
        'location': 'Dubai', 'slug': 'a-third-meetup'
        },
        {
        'title': 'A Fourth Meetup',
        'location': 'Paris',
        'slug': 'a-fourth-meetup'
        }

    ]
    return render(request, 'meetups/index.html', {
        'show_meetups' : True,
        # we define a key to the database we made in a list
        # the key is meetups_key in our case
        'meetups_key': meetups
    })

def greetings(request):
    return HttpResponse('namaste')


def meetup_details(request, meetup_slug):
    print(meetup_slug)
    selected_meetup = {
        'title': 'A First Meetup',
        'description': 'This is the first meetup !'
        }
    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
    })
