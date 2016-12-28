from django.shortcuts import render, get_object_or_404
from .models import Segment, Artwork

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
	segment = get_object_or_404(Segment, id=segment_id)
	context = {
		'segment' : segment,
	}
	return render(request, 'paintings/segments.html', context)


def like(request, segment_id):
	segment = get_object_or_404(Segment, id=segment_id)
	context = {
		'segment' : segment,
	}
	try:
		selected_artwork = segment.artwork_set.get(id=request.POST['artwork'])
	except(KeyError, Artwork.DoesNotExist):
		return render(request, 'paintings/segments.html', {
			'segment' : segment,
			'error_message' : "No item was selected"
		})
	else:
		if(selected_artwork.painting_liked == True):
			selected_artwork.painting_liked = False
		else:
			selected_artwork.painting_liked = True
		selected_artwork.save() 
		return render(request, 'paintings/segments.html', context)
