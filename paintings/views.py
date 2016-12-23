from django.http import Http404
from django.shortcuts import render
from .models import Segment

def index(request):

	all_segments = Segment.objects.all()
	#now we need a dictionary to pass tha data since 
	#the django interface of teh loader works only with the dictionary

	#generally the dictionary is called the context
	context = {
		'all_segments' : all_segments,
	}

	return render(request, 'paintings/index.html', context)

def nextseg(request, segment_id):
	try:
		segment = Segment.objects.get(id=segment_id)
		artworks= segment.artwork_set.all()
		context = {
			'segment' : segment,
			'artworks': artworks,
		}
	except Segment.DoesNotExist:
		raise Http404("Segment does not exists")
	return render(request, 'paintings/segments.html', context)
