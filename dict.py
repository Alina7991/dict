class MyDict:
    def __init__(self):
        self._data = []

    def __setitem__(self, key, value):
        for pair in self._data:
            if pair[0] == key:
                pair[1] = value
                return
        self._data.append([key, value])

    def __getitem__(self, key):
        for pair in self._data:
            if pair[0] == key:
                return pair[1]
        return None

    def __delitem__(self, key):
        for i, pair in enumerate(self._data):
            if pair[0] == key:
                del self._data[i]
                return

    def keys(self):
        return [pair[0] for pair in self._data]

    def values(self):
        return [pair[1] for pair in self._data]

    def items(self):
        return [(pair[0], pair[1]) for pair in self._data]

    def __str__(self):
        return str({key: value for key, value in self.items()})

    def __contains__(self, key):
        return any(pair[0] == key for pair in self._data)

