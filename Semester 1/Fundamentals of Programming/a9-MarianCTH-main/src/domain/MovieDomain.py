class Movie:
    def __init__(self, movie_id, title, description, genre):
        self.__movie_id = movie_id
        self.__title = title
        self.__description = description
        self.__genre = genre

    def __str__(self):
       return f"[ID: {self.__movie_id}] {self.__title}, Genre: {self.__genre}, Description: {self.__description}"

    def GetID(self):
        return self.__movie_id
    def GetTitle(self):
        return self.__title
    def GetDescription(self):
        return self.__description
    def GetGenre(self):
        return self.__genre

    def SetID(self, new_movie_id):
        self.__movie_id = new_movie_id
    def SetTitle(self, new_title):
        self.__title = new_title

