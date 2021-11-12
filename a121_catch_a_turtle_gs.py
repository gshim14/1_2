# a121_catch_a_turtle.py
# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb
#-----game configuration----

spotColor = "pink"
spotShape = "circle"
spotSize = 5
points = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000 
timer_up = False
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Please enter your name:")
#-----initialize turtle-----

spot = trtl.Turtle()
counter_one = trtl.Turtle()
counter =  trtl.Turtle()
spot.shape(spotShape)
spot.turtlesize(spotSize)
spot.fillcolor(spotColor)
spot.speed(0)
spot.penup()

#-----game functions--------
def spot_clicked(x,y):
  counter_one.clear()
  global points
  size = rand.randint(1, 5)
  change_position(size)
  counter_one.color("dark blue")
  counter_one.hideturtle()
  counter_one.penup()
  counter_one.speed(0)
  counter_one.goto(300, 300)
  points += 1
  counter_one.write("points: " + str(points), font=font_setup)
  
def change_position(size):
  if timer_up == False:
    new_xpos = rand.randint(-400,400)
    new_ypos = rand.randint(-300, 300)
    colors = ["violet" , "light green", "light yellow", "pink"]
    colorcycle = rand.randint(0,3)
    spot.stamp()
    spot.hideturtle()
    spot.fillcolor(colors[colorcycle])
    spot.turtlesize(size)
    spot.goto(new_xpos,new_ypos)
    spot.showturtle()
  else:
    spot.hideturtle()
    manage_leaderboard()


def countdown():
  global timer, timer_up
  counter.hideturtle()
  counter.speed(0)
  counter.color("dark blue")
  counter.penup()
  counter.goto(-400, 300)
  counter.pendown()
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
  

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global points
  global spot
  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or points > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, points)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, points)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, points)

#-----events----------------
def start_game():
  wn = trtl.Screen()
  wn.ontimer(countdown, counter_interval)
  if timer_up == False:
    spot.onclick(spot_clicked)
  else:
    spot.clear()
  wn.bgcolor("light blue")
  wn.mainloop()

start_game()