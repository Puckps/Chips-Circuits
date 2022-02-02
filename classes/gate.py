class Gate():
    ''' Gate object contained in node. '''
    def __init__(self, coordinate, id):
        self.coordinate = coordinate
        self.id = id

    def get_coords(self):
        ''' Return coordinate of gate. '''
        return self.coordinate

    def get_id(self):
        ''' Return gate-id. '''
        return self.id