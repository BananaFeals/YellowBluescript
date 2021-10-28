from random import randint
# Im Gonna Clean It
print("YellowBluescript 0.1v\nBy BananaFeals written in python\nsay help? for questions\n")

printword =  "print:"
addword = "math.add"
minusword = "math.sub"
random = "math.random"

bool = True

while bool:
	inputword = input()

	if printword in inputword:
		
		inputword = inputword.replace(printword, "")

		print("\nPrinted:")
		print(inputword+"\n")
	
		print("[Finished]")
# help	
	elif inputword == "help?":
		print("\nuse print:, to make words print math.add/sub to math more functions are coming later")
# Math stuff	
	elif addword in inputword:
		add_1 = int(input('number 1: '))
		add_2 = int(input('number 2: '))

		print(add_1 + add_2)
	elif minusword in inputword:
		minus_1 = int(input('number 1: '))
		minus_2 = int(input('number 2: '))
		
		print(minus_1 - minus_2)
	elif random in inputword:
		random_1 = int(input('number 1:'))
		random_2 = int(input('number 2:'))
		
		print(randint(random_1, random_2))
		
# Stybs Stop the Yellow Blue Script		
	elif inputword == "stybs":
		print("\nStopping Terminal\nYellowBlue Foundation©")
		bool = False

# Unkown Scripts		
	elif inputword:
		print("[Unknown]")