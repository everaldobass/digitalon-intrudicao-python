# Class Televisão
class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
         self.canal += 1

    def diminue_canal(self):
        self.canal -= 1

televisao = Televisao()
print("TV ligada {}".format(televisao.ligada))
televisao.power()
print("TV ligada {}".format(televisao.ligada))
televisao.power()
print("TV ligada {}".format(televisao.ligada))

# Volume canal
print("Canal: {}".format(televisao.canal))
televisao.aumenta_canal()
televisao.aumenta_canal()
televisao.aumenta_canal()
print("Canal: {}".format(televisao.canal))
# Diminue o volume do canal
televisao.diminue_canal()
print("Canal: {}".format(televisao.canal))

