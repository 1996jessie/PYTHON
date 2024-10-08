'''
Created on 2024. 8. 8.

@author: user
'''
class Lion :
    def __init__(self):
        print("Lion")
    def cry(self):
        print("사자 으르렁~")
    def bite(self):
        print("사자 bite~")
        
class Tiger :
    def __init__(self):
        print("Tiger")
    def cry(self):
        print("호랑이 어흥~")
    def jump(self):
        print("호랑이 jump~")
        
class Liger(Tiger, Lion):
    def __init__(self):
        print("Liger")
    def play(self):
        print('라이거와 놀기')
        
l = Liger()
l.bite()
l.cry()
l.jump()
l.play()
