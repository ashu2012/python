def calc(cent):
	fahr= 9.0/5.0 * cent+32
	return fahr

def get_input():
	inputArg= input("enter centigarde temperature:")
	return inputArg

def printing(fahr):
	print(str(fahr))


def main():
	inputArg =get_input()
	printing(calc(inputArg))
 

if __name__ == "__main__": main()
