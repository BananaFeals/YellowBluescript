# Im Gonna Clean It
print("YellowBluescript 0.1v\nBy BananaFeals originally written in python\nsay help? for questions\n")

printword =  "print:"
addword = "math.add"
minusword = "math.sub"
stybs = "stybs"

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
		print("\nuse print:, to make words print math.add/sub to math more 	functions are coming later\nby i got bored at the middle of school inc so i 		made a programming language")
# Math stuff	
	elif addword in inputword:
		add_1 = int(input('number 1: '))
		add_2 = int(input('number 2: '))

		print(add_1 + add_2)
	elif minusword in inputword:
		minus_1 = int(input('number 1: '))
		minus_2 = int(input('number 2: '))
		
		print(minus_1 - minus_2)
		
# Stybs Stop the Yellow Blue Script		
	elif stybs in inputword:
		print("\nStopping Terminal\n")
		bool = False

# Unkown Scripts		
	elif inputword:
		print("[Unknown]")