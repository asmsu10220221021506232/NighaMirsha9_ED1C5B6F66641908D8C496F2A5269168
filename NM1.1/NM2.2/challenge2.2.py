class Player:
  def paly(self):
    print("The player is playing Cricket.")

class Batsman(Player):
  def play(self):
    print("The batsman is batting.")

class Bowler(Player):
  def play(self):
    print("The bowler is bowling.")

# Create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

#Call the play method for each objects
batsman.play()
bowler.play()