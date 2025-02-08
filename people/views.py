import requests
from django.shortcuts import render
from django.http import HttpResponse

def get_actor(request, actor_id):
    API_KEY = 'your_api_key_here'
    actor_name = 'Tom Hanks'
    url = f'https://api.themoviedb.org/3/person/{actor_id}?api_key={API_KEY}'
    
    response = requests.get(url)
    if response.status_code == 200:
        actor_data = response.json()
        return render(request, 'actor_detail.html', {'actor': actor_data})
    else:
        return HttpResponse("Actor not found.", status=404)
