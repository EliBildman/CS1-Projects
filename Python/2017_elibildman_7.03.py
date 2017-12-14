class Time(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        added = Time(0, 0, 0)
        added.second = self.second + other.second
        if added.second >= 60:
            added.minute += 1
            added.second -= 60
        added.minute = self.minute + other.minute
        if added.minute >= 60:
            added.hour += 1
            added.minute -= 60
        added.hour = self.hour + other.hour
        if added.hour >= 24:
            added.hour -= 24
        return added


class Kangaroo(object):
    def __init__(self, name):
        self.name = name
        self.pouch_contents = []

    def put_in_pouch(self, thing):
        self.pouch_contents.append(thing)

    def __str__(self):
        return str(self.pouch_contents)


thing = Kangaroo("joe")
thing.put_in_pouch("yammos")
print(thing)
