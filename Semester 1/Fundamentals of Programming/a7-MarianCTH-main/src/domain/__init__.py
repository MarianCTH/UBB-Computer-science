
class Repository():
    def __init__(self):
        pass

    def __load_file(self):
        try:
            file = open(self.__file_name, "rb")
            self.__data = pickle.load(file)
        except EOFError:
            self.__data = {}

        file.close()

    def __save_file(self):
        file = open(self.__file_name, "wb")
        pickle.dump(self.__data, file)
        file.close()
