from tkinter import *
from tkinter import messagebox
import threading
from time import sleep
import random

width = 800
height = 500
list = []
obs = 2
time_played=0
player_pos = {"x": 100, "y": 400}
player = None
jump_no = 0
obs_pos = {"x": 600, "y": 310}
random_obstacle =None


threadLock = threading.Lock()
threads = []




#wall1
def create_obstacle_1(x,y):
    obstacle=[]

    x1=x
    x2=x+30

    obstacle.append(canvas.create_rectangle(x1,y+50,x2,y+100,fill='gray64')) #1.
    obstacle.append(canvas.create_rectangle(x1, y, x2, y + 50, fill='gray64'))  # 2.
    obstacle.append(canvas.create_rectangle(x1,y-50,x2,y,fill='gray64')) #3.

    return obstacle

def create_wall_2(x,y):
    wall=[]

    x1 = x + 30
    x2 = x + 60

    wall.append(canvas.create_rectangle(x1, y + 50, x2, y + 100, fill='gray64')) #4.
    wall.append(canvas.create_rectangle(x1, y, x2, y + 50, fill='gray64')) #5.
    wall.append(canvas.create_rectangle(x1, y - 50, x2, y, fill='gray64')) #6.

    return wall

def create_wall_3(x,y):
    wall=[]
    x2=x+60
    x3=x+90
    wall.append(canvas.create_rectangle(x2, y + 50, x3, y + 100, fill='gray64')) #7.
    wall.append(canvas.create_rectangle(x2, y, x3, y + 50, fill='gray64')) #8.
    wall.append(canvas.create_rectangle(x+60, y - 50, x3, y, fill='gray64')) #9.

    return wall

def create_wall_4(x,y):
    wall=[]
    x3=x+90
    x4=x+120
    wall.append(canvas.create_rectangle(x3, y + 50, x4, y + 100, fill='gray64')) #10.
    wall.append(canvas.create_rectangle(x3, y, x4, y + 50, fill='gray64')) #11.
    wall.append(canvas.create_rectangle(x3, y - 50, x4, y, fill='gray64')) #12.

    return wall

def create_obstacle_2(x, y):
    obstacle = []

    obstacle.append(create_obstacle_1(x,y))
    obstacle.append(create_wall_2(x,y))
    obstacle.append(create_wall_3(x,y))
    obstacle.append(create_wall_4(x,y))

    return obstacle

def create_obstacle_3(x,y):

    obstacle=[]

    obstacle.append(canvas.create_rectangle(x, y + 50, x + 30, y + 100, fill='gray64'))  # 1.
    obstacle.append(canvas.create_rectangle(x, y, x + 30, y + 50, fill='gray64'))  # 2.

    obstacle.append(create_wall_2(x,y)) #4,5,6
    obstacle.append(create_wall_3(x,y)) #7,8,9

    obstacle.append(canvas.create_rectangle(x + 90, y + 50, x + 120, y + 100, fill='gray64')) #10.
    obstacle.append(canvas.create_rectangle(x + 90, y, x + 120, y + 50, fill='gray64')) #11.

    return obstacle


def create_obstacle_4(x, y):
    obstacle = []

    obstacle.append(canvas.create_rectangle(x, y + 50, x + 30, y + 100, fill='gray64')) #1.
    obstacle.append(canvas.create_rectangle(x, y, x + 30, y + 50, fill='gray64')) #2.

    obstacle.append(create_wall_2(x,y)) #4,5,6
    obstacle.append(create_wall_3(x,y)) #7,8,9


    obstacle.append(canvas.create_rectangle(x+90, y + 50, x + 120, y + 100, fill='gray64'))
    obstacle.append(canvas.create_rectangle(x+90, y, x + 120, y + 50, fill='gray64'))

    obstacle.append(canvas.create_rectangle(x-30,y+50,x,y+100,fill='gray64'))
    obstacle.append(canvas.create_rectangle(x+120,y+50,x+150,y+100,fill='gray64'))

    obstacle.append(canvas.create_rectangle(x+45,y-100,x+75,y-50,fill='gray64'))

    return obstacle


def create_obstacle_5(x, y):
    obstacle = []

    obstacle.append(create_obstacle_1(x,y)) #1,2,3

    obstacle.append(canvas.create_rectangle(x+30, y + 50, x + 60, y + 100, fill='gray64')) #4.
    obstacle.append(canvas.create_rectangle(x+30, y, x+60 , y + 50, fill='gray64')) #5.

    obstacle.append(canvas.create_rectangle(x+60, y + 50, x + 90, y + 100, fill='gray64')) #7.

    return obstacle

def create_obstacle_6(x, y):
    obstacle = []

    obstacle.append(canvas.create_rectangle(x, y + 50, x + 30, y + 100, fill='gray64')) #1.
    obstacle.append(canvas.create_rectangle(x+30, y + 50, x + 60, y + 100, fill='gray64')) #4.
    obstacle.append(canvas.create_rectangle(x+30, y, x+60 , y + 50, fill='gray64')) #5.
    obstacle.append(create_wall_3(x,y))


    return obstacle



#izokrenute
#1.i druga prepreka iste kao i obicne

def create_obstacle_7(x,y): #treca izokrenuta
    obstacle=[]

    obstacle.append(canvas.create_rectangle(x, y, x+30, y+50, fill='gray64'))  # 2.
    obstacle.append(canvas.create_rectangle(x, y-50, x+30, y, fill='gray64'))  # 3.
    obstacle.append(create_wall_2(x,y))
    obstacle.append(create_wall_3(x,y))
    obstacle.append(canvas.create_rectangle(x+90, y, x+120, y + 50, fill='gray64'))  # 11.
    obstacle.append(canvas.create_rectangle(x+90, y - 50, x+120, y, fill='gray64'))  # 12.


    return obstacle


def create_obstacle_8(x,y): #4.izokrenuta
    obstacle=[]

    obstacle.append(canvas.create_rectangle(x+45,y+50,x+75,y+100,fill='gray64'))
    obstacle.append(canvas.create_rectangle(x,y-50,x+30,y,fill='gray64')) #3.
    obstacle.append(canvas.create_rectangle(x+30, y, x+60, y + 50, fill='gray64')) #5.
    obstacle.append(canvas.create_rectangle(x+30, y - 50, x+60, y, fill='gray64')) #6.
    obstacle.append(canvas.create_rectangle(x+60, y, x+90, y + 50, fill='gray64')) #8.
    obstacle.append(canvas.create_rectangle(x+60, y - 50, x+90, y, fill='gray64')) #9.
    obstacle.append(canvas.create_rectangle(x+90, y - 50, x+120, y, fill='gray64'))  # 12.
    obstacle.append(canvas.create_rectangle(x,y-100,x+30,y-50,fill='gray64'))
    obstacle.append(canvas.create_rectangle(x+30, y - 100, x+60, y-50, fill='gray64'))
    obstacle.append(canvas.create_rectangle(x+60, y - 100, x+90, y-50, fill='gray64'))
    obstacle.append(canvas.create_rectangle(x+90, y - 100, x+120, y-50, fill='gray64'))
    obstacle.append(canvas.create_rectangle(x-30, y - 100, x, y-50, fill='gray64'))
    obstacle.append(canvas.create_rectangle(x+120, y - 100, x+150, y-50, fill='gray64'))

    return obstacle

def create_obstacle_9(x,y): #5.izokrenuta
    obstacle=[]

    obstacle.append(create_obstacle_1(x,y)) #1,2,3
    obstacle.append(canvas.create_rectangle(x+30, y, x+60, y + 50, fill='gray64'))  # 5.
    obstacle.append(canvas.create_rectangle(x+30, y - 50, x+60, y, fill='gray64'))  # 6.
    obstacle.append(canvas.create_rectangle(x+60, y - 50, x+90, y, fill='gray64')) #9.

    return obstacle

def create_obstacle_10(x,y): #6.izokrenuta
    obstacle=[]

    obstacle.append(canvas.create_rectangle(x,y-50,x+30,y,fill='gray64')) #3.
    obstacle.append(canvas.create_rectangle(x + 30, y, x + 60, y + 50, fill='gray64'))  # 5.
    obstacle.append(canvas.create_rectangle(x + 30, y - 50, x + 60, y, fill='gray64'))  # 6.
    obstacle.append(create_wall_3(x,y))

    return obstacle

def crash(obstacle):
    global player
    if player:

        px1, px2, py1, py2 = canvas.coords(player)
        ox1, ox2, oy1, oy2 = canvas.coords(obstacle)
        # print(canvas.coords(player))
        # print(canvas.coords(obstacle))

        if px2==ox1 or py1==oy2 or py2==oy1:
            return True
        else:
            return False
    else:
        return False

# def obstacle_movemet(x, y):
#     global random_obstacle
#     global obs
#     global time_played
#     global obs_pos
#     # i = random.randint(1, 12)
#     # obs = 3
#     i = obs
#
#     while x > 10:
#         if i == 1:
#             random_obstacle=create_obstacle_1(x, y)
#         elif i == 2:
#             random_obstacle=create_obstacle_2(x, y)
#         elif i == 3:
#             random_obstacle=create_obstacle_3(x, y)
#         elif i == 4:
#             random_obstacle=create_obstacle_4(x, y)
#         elif i == 5:
#             random_obstacle=create_obstacle_5(x, y)
#         elif i == 6:
#             random_obstacle=create_obstacle_6(x, y)
#         elif i == 7:
#             random_obstacle=create_obstacle_1(x, y-350)
#         elif i == 8:
#             random_obstacle=create_obstacle_2(x, y-350)
#         elif i == 9:
#             random_obstacle=create_obstacle_7(x, y-350)
#         elif i == 10:
#             random_obstacle=create_obstacle_8(x, y-350)
#         elif i == 11:
#             random_obstacle=create_obstacle_9(x, y-350)
#         else:
#             random_obstacle=create_obstacle_10(x, y-350)
#
#         game_window.update()
#         x -= 10
#         obs_pos["x"] = x
#         sleep(0.05)
#         time_played += 0.05
#         for o in random_obstacle:
#             if str(type(o)) == "<class 'list'>":
#                 for o1 in o:
#                     if crash(o1):
#                         print("END")
#                     canvas.delete(o1)
#             else:
#                 if crash(o):
#                     print("END")
#             canvas.delete(o)
#
#         # player_movemet(None, player_pos["x"], player_pos["y"])
#     # else:
#     #     for o in random_obstacle:
#     #         if str(type(o)) == "<class 'list'>":
#     #             for o1 in o:
#     #                 canvas.delete(o1)
#     #         else:
#     #             canvas.delete(o)
#     #     obs_pos["x"] = 600
#     #     obs_pos["y"] = 310
#     #     player_movemet(None, player_pos["x"], player_pos["y"])








class myThread (threading.Thread):
    # def __init__(self, threadID, name, counter):
    #       threading.Thread.__init__(self)
    #       self.threadID = r
    #       self.name = name
    #       self.counter = counter
    def kill(self):
        self.killed = True

    def run(self):

        global random_obstacle
        global obs
        global time_played
        global obs_pos
        # i = random.randint(1, 12)
        # obs = 3
        while True:

            i = obs
            x = obs_pos["x"]
            y = obs_pos["y"]
            print("111111111111111111111111111111111")
            print(x,y)
            print("111111111111111111111111111111111")
            while x > 20:
                if i == 1:
                    random_obstacle = create_obstacle_1(x, y)
                elif i == 2:
                    random_obstacle = create_obstacle_2(x, y)
                elif i == 3:
                    random_obstacle = create_obstacle_3(x, y)
                elif i == 4:
                    random_obstacle = create_obstacle_4(x, y)
                elif i == 5:
                    random_obstacle = create_obstacle_5(x, y)
                elif i == 6:
                    random_obstacle = create_obstacle_6(x, y)
                elif i == 7:
                    random_obstacle = create_obstacle_1(x, y - 350)
                elif i == 8:
                    random_obstacle = create_obstacle_2(x, y - 350)
                elif i == 9:
                    random_obstacle = create_obstacle_7(x, y - 350)
                elif i == 10:
                    random_obstacle = create_obstacle_8(x, y - 350)
                elif i == 11:
                    random_obstacle = create_obstacle_9(x, y - 350)
                else:
                    random_obstacle = create_obstacle_10(x, y - 350)

                game_window.update()
                x -= 10
                obs_pos["x"] = x
                sleep(0.05)
                time_played += 0.05
                for o in random_obstacle:
                    if str(type(o))=="<class 'list'>":
                         for o1 in o:
                            canvas.delete(o1)
                    else:
                        canvas.delete(o)
                random_obstacle=None
                print('------------------------------------------')
                print(x)
                print('------------------------------------------')
            obs_pos["x"] = 600
            sleep(3)
            obs = random.randint(1, 7)



def cleanup():
    global thread
    print('you lost')
    sleep(.5)
    score = int(time_played)*10
    message = messagebox.showinfo("Game over", "Your score is " + str(score))
    if message:
        thread.kill()
        exit()



def create_player(x, y):

    global player
    if player:
        canvas.delete(player)
    player = canvas.create_rectangle(x + 10, y + 10, x - 10, y - 10, fill="red", outline="black")
    player_pos["x"] = x
    player_pos["y"] = y
    game_window.update()

def player_movemet(move, x, y):
    global player
    global jump_no
    global time_played
    global random_obstacle
    global thread
    speed = 0.009
    if move:
        while y >= 1:

            y -= 1
            if y < 180:
                canvas.delete(player)
                sleep(0.05)
                time_played += 0.05
                player_movemet(None, x, 190)

            create_player(x, y)
            jump_no = 1
            sleep(speed)
            time_played += speed
            if random_obstacle:
                for o in random_obstacle:
                    if str(type(o)) == "<class 'list'>":
                        for o1 in o:
                            if crash(o1):
                                cleanup()
                    else:
                        if crash(o):
                            cleanup()
            # canvas.delete(player)

    else:
        while y >= 1:
            y += 1
            if y > 400:
                y = 400
                jump_no=0


            create_player(x, y)

            sleep(speed)
            time_played += speed
            # canvas.delete(player)




def movement(event=None):
    move = event.char
    global jump_no
    global time_played
    global player_pos
    global random_obstacle
    print(move)
    print(int(time_played))
    # thread1 = myThread(1,"ssss", 1)
    # thread1.start()

    if player:
        canvas.delete(player)

    if jump_no == 0:
        player_movemet(move, player_pos["x"], player_pos["y"])
    # player_movemet(None, player_pos["x"], player_pos["y"])
    # time_played += 0.02

    game_window.update()


def main():
    global canvas, game_window,time_played, thread
    time_played=5
    game_window = Tk()
    game_window.title('jumping cube')
    canvas = Canvas(game_window, width=width, height=height, background='white')
    canvas.pack()
    thread = myThread()
    thread.start()
    game_window.bind('w', movement)
    create_player(player_pos["x"], player_pos["y"])
    # obstacle_movemet(obs_pos["x"], obs_pos["y"])
    # player_movemet(None, player_pos["x"], player_pos["y"])
    game_window.update()
    game_window.mainloop()

main()