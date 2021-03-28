class Student:
 def __init__(self,scores = []):
   self.scores = scores

 def avg(self):
   return round(sum(self.scores)/ len(self.scores))

# objects / instance

kings = Student(scores = [2,3,5,3,5,10])
tayo= Student(scores= [4,5,8,8,12])

print(kings.avg())
print(tayo.avg())