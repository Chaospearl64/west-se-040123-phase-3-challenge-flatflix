


class Movie:
    all = []

    def __init__(self, title):
        self.title = title 
        self.all.append(self)
        

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._title = value
            
        else:
            raise Exception

    def reviews(self):
        return [r for r in Review.all if r.movie is self]

    def reviewers(self):
        return [r.viewer for r  in self.reviews()]

    def average_rating(self):
       ratings = [r.rating for r in self.reviews()]
       return sum(ratings)/ len(ratings)
      

    @classmethod
    def highest_rated(cls):
        highest_rating = 0
        highest_rated_movie = None
        for movie in cls.all:
            average_rating = movie.average_rating()
            if average_rating > highest_rating:
                highest_rating = average_rating
                highest_rated_movie = movie
        return highest_rated_movie

from classes.review import Review

