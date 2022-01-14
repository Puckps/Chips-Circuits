from gate import Gate

class Node():
    def __init__(self, coordinate, id):
        self.coordinate = coordinate          # x, y 
        self.id = id
        self.is_gate = False                  # true als node is a gate

    def set_gate(self):
        self.is_gate = True

    def create_gate(self):
        self._gate = Gate(self.coordinate, self.id)

    def get_gate(self):
        return self._gate
