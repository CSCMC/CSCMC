def funcao():

    a = 3
    b = 2
    
    print(a*b)

    var = "variavel sendo uma string"
    print(var)

funcao()

###loops


def first_function():
	a = 10
	while(a == 10):
		print("este eh um while loop")

first_function()

#else if = elif


def second_function():
	a = 10
	if(a == 11):
		print("testando")
	elif(a == 12):
		print("testando2")
	elif(a==13):
		print('testando3')
	else:
		print("did not find the value of a")

	
second_function()


for x in range(2, 8, 12):
  print(x)



adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
	for y in fruits:
		print(x, y)