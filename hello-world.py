# import random

# print(random.randrange(1, 10))

# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''

# for x in a:
# 	print(x)

# print(len(a))

# Check if "free" is present in the following text:

# txt = "The best things in life are free!"
# print("free" in txt)
# print("free" not in txt)

# b = "Hello, World!"
# print(b[2:5])

# txt = "hello, and welcome to my world."
# print(txt.capitalize())	

# x = 10
# print(x % 3)

# x = 5

# x **= 4

# print(x)

# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# print(thislist[-1])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:10])

# thislist = ["apple", "banana", "cherry"]
# if "apples" in thislist:
# 	print("Yes")

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist[1:3])

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]

# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i+=1

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[0])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

# x = ["apple", "banana", "cherry"]
# [green, yellow, *red] = x
# print(green)

# x = ["apple", "banana", "cherry"]
# print(x.index("bananaa"))

# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# thisset = {"apple", "banana", "cherry", "apple"}

# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]

# thisset.update(mylist)

# print(thisset)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict['brand'])
# print(thisdict.get('brand'))
# print(thisdict.keys())

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

#x = car.keys()

# print(x) #before the change

#car["color"] = "white"

# print(x) #after the change

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["color"] = "red"

# print(x) #after the change


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change

# car["color"] = "red"

# print(x) #after the change


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

# for x in thisdict:
# 	print(thisdict[x])

# for x, y in thisdict.items():
#   print(x, y)


# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# print(myfamily)


# x = ('key1', 'key2', 'key3')
# y = 0

# thisdict = dict.fromkeys(x, y)

# print(thisdict)


# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")


# i = 1
# while i < 6:
#   print(i)
#   i += 1


# for x in range(2, 30, 3):
#   print(x)


# def my_function():
#     print("Hello from a function")

# my_function()


# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil")


# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")


# def my_function(child3, child2, child1):
#   print("The youngest child is " + child2)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")

# x = lambda a : a + 10
# print(x(5))

# x = lambda b : b + str(10)
# print(x('asasas'))

# x = lambda c, a : c + a

# print(x(2, 4))


# class Person():
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def myFunc(self):
# 		return f"Hello nama saya {self.name} {str(self.age)}"

# p1 = Person("Jhon", 36)

# class Student(Person):
# 	def __init__(self, fname, lname):
# 		Person.__init__(self, fname, lname)

# s1 = Student("Mike", 15)

# print(s1.myFunc())


# class Person():
# 	def __init__(self):
# 		self.name = "Dadang"

# 	def getName(self):
# 		return "dddd"

# p = Person()

# print(p.name)

# p.name = "Agus"

# print(p.getName())


# arr = [5, 10, 25]
# x = min(arr)
# y = max(5, 10, 25)

# print(x, y)

# import json

# x = '{"name": "Agus", "age": 17}'

# print(json.loads(x))

# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# print(json.dumps(x))

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None)) 


# import camelcase

# c = camelcase.CamelCase()

# txt = "hello world"

# print(c.hump(txt)) 

# class Ex(BaseException):
# 	def __init__(self, message):
# 		BaseException.__init__()
# 		self.message = message
# 	def getMessage(self):
# 		return self.message

# try:
# 	raise Ex('Error Ocure')
# except Ex as e:
# 	print(e.getMessage())
# except:
# 	print('error')
# else:
# 	print("Nothing went wrong") 


# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")


# def makePretty(func = None):
#     if func:
#         func()
#     return print("Def makePretty")


# @makePretty
# def ordinary():
#     print("Def Ordinary")
# print("asasas")


# class Abc():
#     tablename = 'Abc'

#     def __init__(self):
#         self.tablename = 'Bcd'

#     def getTableName(self):
#         return self.tablename

#     def getTableName2(self):
#         return Abc.tablename

# v = Abc()
# print(v.getTableName())
# print(v.getTableName2())

# data = {"nama": "Agus Setiadi", "Almat": "Mbogor"}

# print(data["nama"])

class Hero():
  def __init__(self):
    self._name = 'name'
    self.nama = 'nama'

  @property
  def name(self):
    return self._name

class Heroku(Hero):
  def __init__(self):
    super().__init__()

  def test(self):
    return super().name

her = Heroku()
print(her.test())

# print(_('asas'))