def get_input():
    userInput = input("Enter the temperature in Celsius: ->")
    return userInput

def calc_temp(celsius):
    fahr= celsius * 9/5.0 + 32
    return fahr

if __name__== "__main__":
    import doctest
    doctest.testmod()
    userInput=get_input()
    fahrConverted=calc_temp(userInput)
    print "The user's Celsius input is "+ str(userInput)+" and its Fahrenheit equivalent "+str(fahrConverted)




