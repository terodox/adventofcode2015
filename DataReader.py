class DataReader:
    @staticmethod
    def read_data(day):
        with open("Day{0:02d}.txt".format(day)) as data:
            return data.readlines()


class AdventDay:
    def __init__(self, day):
        self._day = day

    def read_data(self):
        return DataReader.read_data(self._day)
