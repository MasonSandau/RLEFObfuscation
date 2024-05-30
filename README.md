# RLEFObfuscation
Random linear execution flow obfuscation PoC

# Idea and write up

This obfuscation method is ideal for low level obfuscation (I'm hoping to port this ti assembly or c++ to do more security testing)

Bascially the idea is that when you dissasemble a program in ida it builds a execution flow graph, I was hoping with this that it would be very difficult to determine how things are executed via the graph representation by returning to functions and random times but still allowing for execution to flow in a linear fashion. So the program builds a list of functions and then executes them in a "random" order, then checking if its time to execute that specfic funciton. If it is time to execute it will run it then pop it from the list, but then if it isn't it simply skips it and selects a new random function to execute and repeats till the list is empy which would mean its done executing. 

# Uses

The main uses I see in this is having a authentication portion, main function portion, and other helper functions. This would allow for it to seem as if the execution order may execute the main function without autherization but still forcing autherization first. 

Checks inside of each function for authentication would be necessary for safty purposes. 

# Limitations and vulnerablities

Execution time is greatly increased as the randomizaion of it means that it is an unknown time it takes to execute all functions in order. 

Vulnerablities mainly lie in the execution order list, if an attacker can rewrite the list that means it could easily skip authentication and control the flow via that list. 
