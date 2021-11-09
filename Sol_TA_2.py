import turtle

dict_square={"Shape":"square","Size":100,"Angle":90,"Color":"red"}

for i in range(4):
    turtle.pencolor(dict_square["Color"])
    turtle.shape(dict_square["Shape"])
    turtle.forward(dict_square["Size"])
    turtle.left(dict_square["Angle"])
