Author: Nickolas Johnson - njohnso3@uoregon.edu

APPLICATION

This application determines control open and close times for a brevet. A brevet is a timed, long distance road cycling event. To control the speed that riders are riding the
course, there are 'controls' (similar to checkpoints) that have certain times that they open or close depending on a universal minimum and maximum speed allowed during certain
intervals of a race. The intervals are listed below, along with their minimum and maximum speeds allowed within the given interval, all in Km/Hr:

	0 - 200: Max speed: 34, Min speed: 15
	200 - 400: Max speed: 32, Min speed: 15
	400 - 600: Max speed: 30, Min speed: 15
	600 - 1000: Max speed: 28, Min speed: 11.428
	1000 - 1300: Max speed: 26, Min speed: 13.333

ALGORITHM

The algorithm for this is fairly simple and contains a few special edge cases. In order to account for different minimum and maximum speeds in each distance span, I created
a couple of dictionaries containing information for each distance span. Then I looped through each distance span individually and had two cases to check. For case 1, if the
control point is within the distance span, then I find the amount of time it takes to get to the control point from the beginning(calculating with min/max speed depending on if 
I am in open time or close time function). Or case 2 where it is not within the distance span. Here I get the length of the distance span divided by min/max speed, multiplied
by 60. This will give me the minutes that it takes to cover the distance span at min/max speed. These two cases are run through for each distance span and eventually you add all
the minutes up to get the total minute displacement from the start time and return this value.


USING START

First you need to download Docker. You then can clone this repository and type "Docker build -t myimagename ." Note the '.' at the end of the commang. To run the the 
image in a container, type "docker run -p5000:5000 myimage". Your application is now running. View your web app by going to http://localhost:5000 in a browser.
If you're running an apple computer, then you may want to run with -p5001:5000 as port 5000 is usually used for other programs. Then you can provide the given inputs 
specified in the webpage and it should give you open and close times.  


SUBMIT/DISPLAY

These two buttons at the bottom of the site will insert/fetch the data provided within the rows. The submit button, when pressed, will take the degin date, brevet distance, 
and each value within the rows: mile length, kilometer length, location, open time, and close time. Once grabbed it will insert it into the mongodb database.
After this it will clear all values in the website to their default state. The Display button will grab the most recent insertion into the database and will change
all values within the site to the values grabbed from insertion ("Submit"). 


API IMPLEMENTATION

Resources Include: api/brevet & api/brevets

Each resource had individual operations for multiple common HTTP requests. Brevet contained GET, PUT, and DELETE while Brevets contained GET and POST.
