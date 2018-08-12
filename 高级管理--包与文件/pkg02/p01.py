class Animel():
    def __init__(self, name="Noname", age=18):
        self.name = name
        self.age = age
        
    def say(self):
        print("My name is {0}".format(self.name))
        print("I years old {0}".format(self.age))
        
class Person(Animel):
    def __init__(self):
        pass
    
    def attr(self,name,age):
        super().__init__(name, age)
        print("我的名字是{0}".format(self.name))
        print("我今年{0}岁了".format(self.age))

def say():
    print("上面有两个类哦！")

print("看看我会不会输出！")