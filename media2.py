import webbrowser
import fresh_tomatoes

# This is the parent class in case we wanted to add a new section
# like TV shows or something.
# class Video() is the parent class
# class Movie() is the child class which inherits
class Video():
    def __init__(self, length, rating):
        print ("Duration and Rating Score Constructor")
        self.length = length
        self.rating = rating

VALID_RATINGS = ["G", "PG", "PG-13", "R"]
# Added 'Video' as the partent so 'Movie' could inheret.
class Movie(Video):  
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, length, rating):
        print("Chiled contstructor movie")
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        Video.__init__(self, length, rating)

    def show_trailer():
        webbrowser.open(self.trailer_youtube_url)
        
    def show_poster():
        webbrowser.open(self.poster_image_url)
        
