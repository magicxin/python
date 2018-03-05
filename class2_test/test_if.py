import random
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

age = 18
if age >= 10 and age <=20:
    print("age is teen")

if age < 10 or age > 14:
    print("not teen")

if 'audi' in cars:
    print("I hava an audi")

if 'benz' not in cars:
    print("I do not hava benz")

name = 'dabing'
if name == 'dabing':
    print('我是小宝宝')
elif name == 'magic':
    print('我是大宝宝')
else:
    print('unstoppable')

colors = ['red','yellow','green']
color = colors[random.randint(0,2)]

if color == 'green':
    print("玩家获得五分")

str = []
if str:
    print("空也可以显示")
else:
    print("字符串为空")