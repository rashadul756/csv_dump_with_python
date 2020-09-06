from abc import ABCMeta, abstractmethod

class MainClass():

    __metaclass__ = ABCMeta

    def __init__(self, data):
        self.data = data


    def query_placeholders(self, columns):
        return ', '.join(['%s'] * len(columns))


    def query_columns(self, columns):
        return ', '.join(columns)


    @abstractmethod
    def columns(self): raise NotImplementedError


    @abstractmethod
    def values(self, id): raise NotImplementedError


    @abstractmethod
    def query(self): raise NotImplementedError

    