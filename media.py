import webbrowser


class Movie():
    '''This class provides a way to store movie information'''

    # This function constructs the class with variables
    # for instantiated objects of the class
    def __init__(
        self, movie_title, movie_storyline, poster_image,
            trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # This function is a class function and available to
    # instantiated objects of the class
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
