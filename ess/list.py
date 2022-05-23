# list

bicycles = ['trek','cannondable','redline','specialized']
print(bicycles)
print(bicycles[-1])

bicycles[0] = 'fh'
bicycles.append('bj')
print(bicycles)

bicycles.insert(2,'yadii')

print(bicycles)

motorcycles = ['honda','yamaha','suzuki']
#del motorcycles[1]
print(motorcycles)

#print(motorcycles.pop())
#print(motorcycles)

#print(motorcycles.pop(0))
#print(motorcycles)

motorcycles.remove('yamaha')
print(motorcycles)

cars = ['bmw','audi','toyota','subaru']
#cars.sort()
#print(cars)

#cars.sort(reverse=True)
#print(cars)

print(cars)
print(sorted(cars))
print(cars)

cars.reverse()
print(cars)

print(len(cars))
