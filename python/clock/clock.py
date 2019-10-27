class Clock(object):
    def __init__(self, hour, minute):

        # Convert hours into minutes and assign
        total_mins = hour * 60 + minute
        self.mins = total_mins % 60
        self.hour = (total_mins // 60) % 24 # // takes the floor of a division sum

    def __repr__(self):
        return "{}:{}".format(str(self.hour).zfill(2), str(self.mins).zfill(2))

    def __eq__(self, other):
        # Equality is defined as one time being the same as another
        # So we just need to check hours and mins are equal
        if (self.hour == other.hour) & (self.mins == other.mins):
            return True
        else:
            return False

    def __add__(self, minutes):
        # Use the same logic as the initial ask but add on minutes
        # Return 'self' so that the class instance updates
        total_mins = self.hour * 60 + self.mins + minutes
        self.mins = total_mins % 60
        self.hour = (total_mins // 60) % 24
        return self

    def __sub__(self, minutes):
        # As above
        total_mins = self.hour * 60 + self.mins - minutes
        self.mins = total_mins % 60
        self.hour = (total_mins // 60) % 24
        return self 