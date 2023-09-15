import sys




def main():
    #make variables for the options
   
    option1= "-o"
    option2= "-t"
    option3= "-h"
    optOneWord=""
    optTwoWord=""
    option1Given=False
    option2Given=False
    option3Given=False
    #Check for cl args
    if len(sys.argv) >1:
        
        #make a new array, one which skips the first argument of argv
        args = sys.argv[1:]
        #loop through arguments
        for i in range(len(args)):
            arg=args[i]
            if arg == option1:
                optOneWord=args[i+1]
                i+=1
                option1Given=True
            elif arg == option2:
                optTwoWord=args[i+1]
                i+=1
                option2Given=True
            elif arg == option3:
                option3Given=True
    
   

    print("Standard Input:")
    for line in sys.stdin:
        
        print(line)

    print("Command line arguments:")
    if option1Given== True:
        print("option 1: " + optOneWord)
    if option2Given== True:
        print("option 2: " + optTwoWord)
    if option3Given== True:
        print("option 3")

if __name__ == "__main__":
    main()




