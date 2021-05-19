class Bulb:
    def __init__(self,lightState):
        print(__name__)
        self.lights=lightState
    def lightState(self):
        if self.lights:
            return "Lights are ON"
        else:
            return "Lights are OFF"