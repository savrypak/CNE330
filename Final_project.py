## here the program that i chose to run on python turtle galaxy 
### welcome to final project

print("Hello, World!")
print("How are you doing?")

### Turtle show now
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

print(list(range(5, 60, 2)))
tess.up()                    
for size in range(5, 60, 2):  
    tess.stamp()              
    tess.forward(size)         
    tess.right(24)              

wn.exitonclick()

