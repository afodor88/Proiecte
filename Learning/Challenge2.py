"""Title:  [easy] challenge #2
Text:  Hello, coders! An important part of programming is being able to apply your programs,
so your challenge for today is to create a calculator application that has use in your life.
It might be an interest calculator, or it might be something that you can use in the classroom.
For example, if you were in physics class, you might want to make a F = M * A calc. 
EXTRA CREDIT: make the calculator have multiple functions! Not only should it be able to calculate F = M * A, but also A = F/M, and M = F/A!"""
   
mass = raw_input('This calculator measures the force. Please input the mass of the object')  
acceleration = raw_input('Now please input the acceleration')
mass = int(mass)
acceleration = int(acceleration)
force = mass * acceleration

print 'The Force calculated for a object of mass ' + str(mass) + ' and acceleration ' + str(acceleration) + ' is ' + str(force) + '.'    