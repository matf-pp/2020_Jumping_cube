import thread

from tkinter import *

from time import sleep

width = 800
height = 500
player_pos = {"x": 100, "y": 450}
player = None
jump_no = 0

def create_player(x, y):

    global player
    player = canvas.create_rectangle(x + 10, y + 10, x - 10, y - 10, fill="bisque2", outline="black")
    player_pos["x"]=x
    player_pos["y"]=y
    game_window.update()


def player_movemet(move, x, y):
    global player
    global jump_no

    if move:
        # while y >= 1:
        y -= 1
        if y < 240:
            canvas.delete(player)
            sleep(0.05)
            player_movemet(None, x, 250)

        create_player(x, y)
        jump_no = 1
        sleep(0.009)
        canvas.delete(player)

    else:
        # while y >= 1:
        y += 1
        if y > 400:
            y = 400
            jump_no=0


        create_player(x, y)

        sleep(0.009)
        canvas.delete(player)






def movement(event=None):
    move = event.char
    global jump_no
    print(move)
    if player:
        canvas.delete(player)
    if jump_no == 0:
        player_movemet(move,player_pos["x"], player_pos["y"])
    game_window.update()


def main():
    global canvas, game_window
    game_window = Tk()
    game_window.title('jumping cube')
    canvas = Canvas(game_window, width=width, height=height, background='white')
    canvas.pack()
    # canvas.create_rectangle(5, 5, width - 5, height - 5, fill='red')
    # canvas.create_rectangle(50, 50, 50, 50, fill="blue")
    # obsticle_movemet(600, 400)
    # player_movemet(100,350)
    # obstacle_movemet(600, 400)
    game_window.update()
    game_window.bind('w', movement)
    player_movemet(None, player_pos["x"],player_pos["y"])


    game_window.mainloop()

