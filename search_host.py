class HostsIter:
    def __init__(self) -> None:
        self.__data = list()

    @property
    def data(self) -> list:
        return self.__data

    @staticmethod
    def __validate_adding_data(some_data):
        if not isinstance(some_data, str):
            raise ValueError('Должна передаваться строка')

    def add_new_host(self, new_host: str) -> None:
        self.__validate_adding_data(new_host)
        self.data.append(new_host)

    def __iter__(self) -> object:
        self.index = 0
        return self

    def __next__(self) -> str:
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
        else:
            raise StopIteration()
        return result

    def clear(self):
        self.__data = list()
