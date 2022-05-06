import threading
class Foo (threading.Thread):
    def __init__(self,x):
        self.__x = x
        threading.Thread.__init__(self)
    def run (self):
          print(str(self.__x))

for x in range(20):
    Foo(x).start()