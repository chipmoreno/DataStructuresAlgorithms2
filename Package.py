
# Defining Package class

class Package:
    def __init__(self, ID, address, city, state, zipcode, Deadline_time, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.Deadline_time = Deadline_time
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None

#Formats and returns package attributes

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zipcode,
                                                       self.Deadline_time, self.weight, self.delivery_time,
                                                       self.status)

# Update Status method update package status based on given delivery time

    def UpdateStatus(self, convert_timedelta):
        if self.delivery_time is not None and self.delivery_time < convert_timedelta:
            self.status = "DELIVERED"
        elif self.departure_time is not None and self.departure_time > convert_timedelta:
            self.status = "CURRENTLY ON ROUTE"
        else:
            self.status = "@ HUB"