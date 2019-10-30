print("Testing on Terminal")
name = input ("what's your name?\n")
print ("hello,",name)
#== lab 5 ex10==
class Computer:
  def __init__(self,cpu,color,portability):
      self.c = cpu
      self.co = color
      self.p = portability
  def playGame(self,nameofGame):
      if self.p:
         print("You are playing",nameofGame,"on your laptop")
      else:
         print("You are playing",nameofGame,"on your desktop")
class laptop(Computer):
  def __init__(self,cpu,color):
      Computer. __init__(self,cpu,color,'True')
class desktop(Computer):
  def __init__(self,cpu,color):
      Computer. _init_(self,cpu,color,'False')
myMac = laptop('A6','white')
print("My pc runs on",myMac.c)