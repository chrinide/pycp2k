from pycp2k.inputsection import InputSection


class _gv094(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale_x = None
        self.Cutoff_radius = None
        self.Gamma = None
        self._name = "GV09"
        self._keywords = {'Cutoff_radius': 'CUTOFF_RADIUS', 'Scale_x': 'SCALE_X', 'Gamma': 'GAMMA'}
        self._attributes = ['Section_parameters']

