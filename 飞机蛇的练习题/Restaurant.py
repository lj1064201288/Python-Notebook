class Restaurant():

    def __init__(self, name, cuisine):

        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_serced = 0

    def describe_restaurant(self):
        print("这个餐馆的名字是:", self.restaurant_name)
        print("这个餐馆是一个" + self.cuisine_type + "餐馆.")

    def open_restaurant(self):
        print("该餐馆正在营业!")

    def set_number_served(self, num):
        self.num = num
        print(id(self.num))
        print("这个餐馆最多能容纳" + str(self.num) + "人！")

    def increment_number_serced(self, value):

        self.value = value
        self.number_serced += self.value
        if restaurant.num <= restaurant.number_serced:
            print("餐馆已满!请明天再来!")
        else:
            print("有" + str(restaurant.number_serced) + "人来过这家餐厅!")


