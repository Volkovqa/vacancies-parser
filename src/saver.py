from abc import ABC, abstractmethod
import json
import os


class Saver(ABC):
    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def delete(self):
        pass


class FileManagerMixin:

    @staticmethod
    def _connect(filename) -> None:

        if not os.path.exists(os.path.dirname(filename)):
            os.mkdir(os.path.dirname(filename))

        if not os.path.exists(filename):
            with open(filename, "w") as file:
                file.write(json.dumps([]))

    @staticmethod
    def _open_file(filename) -> list:

        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)


class JSONSaver(Saver, FileManagerMixin):

    def __init__(self, file_path):
        self.data_file = file_path

    @property
    def data_file(self):
        return self.__data_file

    @data_file.setter
    def data_file(self, value):
        self.__data_file = value
        self._connect(self.__data_file)

    def insert(self, data) -> None:
        file_data = self._open_file(self.__data_file)
        file_data.append(data)

        with open(self.__data_file, "w", encoding="utf-8") as file:
            json.dump(file_data, file, indent=4, ensure_ascii=False)

    def select(self, query=None) -> list:
        file_data = self._open_file(self.__data_file)

        if not query:
            return file_data

        result = []
        for entry in file_data:
            if all(entry.get(key) == value for key, value in query.items()):
                result.append(entry)

        return result

    def delete(self, query=None) -> None:
        file_data = self._open_file(self.__data_file)

        if not query:
            return

        result = []
        for entry in file_data:
            if not all(entry.get(key) == value for key, value in query.items()):
                result.append(entry)

        with open(self.__data_file, "w", encoding="utf-8") as file:
            json.dump(result, file, indent=4, ensure_ascii=False)

    def clear_data(self):
        with open(self.__data_file, "w") as file:
            file.write(json.dumps([]))
