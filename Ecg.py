#ECG class

class Ecg:
    def __init__(self, id, leads):
        self.id = id
        self.leads = leads

    def to_string(self):
        print("ID: ", self.id)
        print("Number of leads: ", self.leads)
