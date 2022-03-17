from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>hello Django!</h1>
        <p>Mes groupes preferes sont:</p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
    """)

def about(request):
    return HttpResponse('<h1>A propos</h1><p>Nous aimons merch</p>')

def listings(request):
    listings = Listing.objects.all()
    return HttpResponse(f"""
        <h1>Liste des titres!</h1>
        <p>Ma liste:</p>
        <ul>
            <li>{listings[0].title}</li>
            <li>{listings[1].title}</li>
            <li>{listings[2].title}</li>
            <li>{listings[3].title}</li>
            <li>{listings[4].title}</li>
            <li>{listings[5].title}</li>
            <li>{listings[6].title}</li>
        </ul>
    """)

def contact(request):
    return HttpResponse('<h1>Nous contacter</h1><p>Page de contact<p>')