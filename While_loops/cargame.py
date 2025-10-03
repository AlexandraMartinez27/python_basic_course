command = ""
started = False

while True:
    
    command = input (">").lower()
    if command == 'start' : 
        if started:
            print ("Car is already started")
        else:
            started = True    
            print ("cart started")
    elif command == "stop":
        if not started:
            print ("Car is already stopped")
        else: 
            started = False
            print ("car stopped")
    elif command == "help":
        print("start - to start the car\nstop - to stop the car\nquit - to exit the game")
    elif command == "quit":
        break
    else:
        print("i dont understand that")