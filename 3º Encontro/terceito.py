class Sum:

	def add(self, x):
		return x + 1

s = Sum()

print(s.add(1823123))

##############################################################################

class Person: #blueprint
	def __init__(self, name, age, height, hair_colour, sport):
		self.name = name
		self.age = age
		self.height = height
		self.hair_colour = hair_colour
		self.sport = sport


	def walk(self):
		print(self.name + "is walking")

	def plays(self):
		print(self.sport + 'is my favourite sport')

	def speak(self):
		print("Hey, my name is "+ self.name + ". I am  " + str(self.age) + ' years old. My height is' + str(self.height) + ' and my hair colour is' + self.hair_colour)

baldo = Person("Eduardo Baldini", 17, 1.89, 'green', 'basketball')
felpo = Person("Felipe Sánchez", 16, 1.89, 'yellow', 'afl')
carlos = Person("Carlos", 1231, 1.934, "brown", 'football')

print(baldo.hair_colour)
baldo.walk()
baldo.speak()
print(carlos.height)
baldo.sport()

##############################################################################

class Pet:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def show(self):
		print(f"I am {self.name} and I'm {self.age} years old")

class Cat(Pet):
	
	def speak(self):
		print("meow")

class Dog(Pet):
	
	def speak(self):
		print("bark")

p = Pet("aksdasd", 15)
p.show()
c = Cat("snowy", 221312)
c.show()
c.speak()
d = Dog("rex", 3)
d.show()
d.speak()

###################################################################################

class Student:
	def __init__(self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade

	def get_grade(self):
		return self.grade

class Course:
	def __init__(self, name, max_student):
		self.name = name
		self.max_student = max_student
		self.students = []

	def add_student(self, student):
		if len(self.students) < self.max_student:
			self.students.append(student)
			print("woked fine!")
		print("did not work")

	def get_avarege_grade(self):
		value = 0
		for student in self.students:
			value += student.get_grade()

		return value / len(self.students)

s1 = Student("baldo", 17, 84)
s2 = Student('felpo', 16, 91)
s3 = Student('lobo', 17, 31)


course1 = Course("Math", 2)
course2 = Course("Spanish", 2)


course1.add_student(s1)
course1.add_student(s2)
course1.add_student(s3)

course2.add_student(s1)
course2.add_student(s2)
course2.add_student(s3)

print(course2.students[1].age)
print(course2.students[1].grade)
print(course2.get_avarege_grade())