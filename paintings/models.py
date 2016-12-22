from django.db import models

class Segment(models.Model):
	artist_name = models.CharField(max_length=50) #name of the painter
	artist_type = models.CharField(max_length=25) #type of paintings done by the painter
	artist_image= models.CharField(max_length=1000) #image link to the segment of the artist which user can explore

	def __str__(self):
		return self.artist_name

class Artwork(models.Model):
	painting_artist = models.ForeignKey(Segment, on_delete= models.CASCADE)
	painting_name = models.CharField(max_length=100)
	painting_date = models.CharField(max_length=25)
	painting_cost = models.CharField(max_length=10)
	painting_image=models.CharField(max_length=1000)

	def __str__(self):
		return self.painting_name

	
