

class Viewer:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) in range(6, 17):
            self._username = username
        else:
            raise Exception

    def reviews(self):
        return [r for r in Review.all if r.viewer is self]

    def reviewed_movies(self):
        return [r.movie for r in Review.all if r.viewer is self]

    def has_reviewed_movie(self, movie):
        return movie in self.reviewed_movies()

from classes.review import Review


