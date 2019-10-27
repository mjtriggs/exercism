class Clock(object):
    def __init__(self, hour, minute):

        # Convert hours into minutes and assign
        total_mins = hour * 60 + minute
        self.mins = total_mins % 60
        self.hour = (total_mins // 60) % 24

    def __repr__(self):
        return "{}:{}".format(str(self.hour).zfill(2), str(self.mins).zfill(2))

    def __eq__(self, other):
        if (self.hour == other.hour) & (self.mins == other.mins):
            return True
        else:
            return False

    def __add__(self, minutes):
        total_mins = self.hour * 60 + self.mins + minutes
        self.mins = total_mins % 60
        self.hour = (total_mins // 60) % 24
        return self

    def __sub__(self, minutes):
        total_mins = self.hour * 60 + self.mins - minutes
        self.mins = total_mins % 60
        self.hour = (total_mins // 60) % 24
        return self 