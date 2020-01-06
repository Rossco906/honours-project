#list of deliveries
class Trip: 

    def __init__(self, deliveries):
        self.deliveries = [deliveries]

    def addDelivery(self, delivery):
        self.deliveries.append(delivery)

    def __str__(self):
        return(str(self.deliveries))
    