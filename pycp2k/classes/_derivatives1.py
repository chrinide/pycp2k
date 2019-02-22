from pycp2k.inputsection import InputSection
from ._each220 import _each220


class _derivatives1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Ndigits = None
        self.EACH = _each220()
        self._name = "DERIVATIVES"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Ndigits': 'NDIGITS'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']
