from edith import *


class Mapa:

    def __init__(self):
        self.edith = Edith()
        self.edith.show_welcome_message()

    def mapa(self, command):
        method = self.edith.get_skill(command)
        try:
            getattr(sys.modules[__name__], method)()
        except Exception:
            print("Uh Ohh, I didn't get that. Please try `mapa help` for help")


obj = Mapa()
obj.mapa("tell me a joke")