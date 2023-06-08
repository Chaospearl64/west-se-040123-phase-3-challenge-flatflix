class Review:
    all = []

    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        self.all.append(self)

    @property
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self, value):
        if isinstance(value, Movie):
            self._movie = value
        else:
            raise Exception 

    @property
    def viewer(self):
        return self._viewer

    @viewer.setter
    def viewer(self, value):
        if isinstance(value, Viewer):
            self._viewer = value
        else:
            raise Exception 

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if isinstance(value, int) and 1 <= value <= 5:
            self._rating = value
        else:
            raise Exception

            
from classes.viewer import Viewer
from classes.movie import Movie