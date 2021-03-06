from generatorObjects.node import Depot
from generatorObjects.battery import Battery
class Action:
    def __init__(self, node, prevAction, nextAction):
        self.node = node
        self.prevAction = prevAction
        self.nextAction = nextAction 
    
    def __repr__(self):
        return str(self)

    def __str__(self):
        return (f"Node : {str(self.node)}")

class Delivery(Action):
    def __init__(self, node, package, prevAction = None, nextAction = None):
        super().__init__(node, prevAction, nextAction)
        self.package = package 

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (super().__str__() + f" Package: {self.package}")

class ChangeBattery(Action):
    def __init__(self, node, batteryDropped, batterySelected = None, prevAction=None, nextAction=None):
        if batterySelected == None: 
            batterySelected = Battery.createNew()
        self.batteryDropped = batteryDropped
        self.batterySelected = batterySelected
        super().__init__(node, prevAction, nextAction)
    
class AtDepot(Action):
    def __init__(self, node = Depot() , prevAction=None, nextAction=None):
        super().__init__(node, prevAction, nextAction)