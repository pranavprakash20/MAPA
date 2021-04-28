from edith import *

class Mapa:

    def __init__(self):
        show_welcome_message()

    def mapa(self, command):
        method = get_skill(command)
        try:
            getattr(sys.modules[__name__], method)()
        except AttributeError:
            print("Uh Ohh, I didn't get that. Please try `mapa help` for help")


obj = Mapa()
obj.mapa("tell me a joke")