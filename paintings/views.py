from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>This is the Paintings Section</h1>")

def nextseg(request, segment_id):
	return HttpResponse("<h2>This is Segment Number: " + str(segment_id) + "</h2>")
	