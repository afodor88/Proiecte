"""Title:  [easy] challenge #2
Text:  Hello, coders! An important part of programming is being able to apply your programs,
so your challenge for today is to create a calculator application that has use in your life.
It might be an interest calculator, or it might be something that you can use in the classroom.
For example, if you were in physics class, you might want to make a F = M * A calc. 
EXTRA CREDIT: make the calculator have multiple functions! Not only should it be able to calculate F = M * A, but also A = F/M, and M = F/A!"""



userchoice = raw_input('What do you want to calculate?\nmass, acceleration or force')

def calculator():
    if userchoice == 'mass':
        acceleration = int(raw_input('What will be the acceleration?'))
        force = int(raw_input('And what it will be the force?'))
        return float(force) / float(acceleration)

    elif userchoice == 'force':
        acceleration = int(raw_input('What will be the acceleration?'))
        mass = int(raw_input('And what it will be the mass?'))
        return float(mass) * float(acceleration)

    elif userchoice == 'acceleration':
        force = int(raw_input('And what it will be the force?'))
        mass = int(raw_input('And what it will be the mass?'))
        return float(force)/float(mass)

    else:
        return "You didn't choose any of the available options"


print calculator()

        
        


    

