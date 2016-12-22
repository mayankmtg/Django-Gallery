from django.http import HttpResponse
from django.template import loader
from .models import Segment

def index(request):

	all_segments = Segment.objects.all()
	template = loader.get_template('paintings/index.html')
	
	#now we need a dictionary to pass tha data since 
	#the django interface of teh loader works only with the dictionary

	#generally the dictionary is called the context
	context = {
		'all_segments' : all_segments,
	}

	return HttpResponse(template.render(context, request))

def nextseg(request, segment_id):
	return HttpResponse("<h2>This is Segment Number: " + str(segment_id) + "</h2>")
