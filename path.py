import gate
class Path():
    def __init__ (self, net):
        self.net = net              # van waar naar waar (begin, eind) 
        self.path = []              # in welke stapjes (lijst van de coordinatens) 

    def make_path(self):
        start_gate = self.net[0]
        end_gate = self.net[1]
        start_coordinate = gate.coordinate(start_gate)