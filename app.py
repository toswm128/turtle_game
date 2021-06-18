import turtle as t

t.setup(800,800) 
t.up()
t.ht()

playerSpeed = 5
score = 0
isGameOver = False

t.goto(0,30)
t.write(f"score :", False, "center",("",20))

player = t.Turtle()
player.shape("turtle")
player.up()

while (isGameOver != True):
    player.forward(playerSpeed)

input()