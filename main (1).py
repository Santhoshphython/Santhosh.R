#Define the base class player 
class player:
  def play(self):
    print("the player is playing cricket. ")

#Define the drived class Batsman 
class Batsman(player):
 def play(self):
   print("the batsman is batting.")

#Define the drived class Bowler 
class Bowler:
  def play(self):
   print("the bowler is Bowling. ")

#create object of Batsman and Bowler classes 
batsman=Batsman()
bowler=Bowler()

#call the play() for each object
batsman.play()
bowler.play()