class Gate():
    def __init__(self, coordinate, id):
        self.coordinate = coordinate
        self.id = id

    def get_coords(self):
        return self.coordinate

    def get_id(self):
        return self.id