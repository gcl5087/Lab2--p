
# Author: Grace Lavin gcl5087@psu.edu
# Collaborator: Keyu Lu lvl566@psu.edu
# Collaborator: Jacob Henderson jrh6533@psu.edu
# Collaborator: Kristina Balta kqb5799@psu.edu
# Section: 1
# Breakout: 5

# the problem I am having is how to use the run command 
def getLetterGrade(grade):
  if grade >= 93.0:
    letter = "A"
  elif grade >= 90.0:
    letter = "A-"
  elif grade >= 87.0:
    letter = "B+"
  elif grade >= 83.0:
    letter = "B"
  elif grade >= 80.0:
    letter = "B-"
  elif grade >= 77.0:
    letter = "C+"
  elif grade >= 70.0:
    letter = "C"
  elif grade >= 60.0:
    letter = "D"
  elif grade < 60:
    letter = "F"
  return letter

def run():
  gradeValue = input("Enter your CMPSCI 131 grade: ")
  gradeValue = float(gradeValue)
  letterAnswer = getLetterGrade(gradeValue)
  print(f"Your letter grade for CMPSC 131 is {letterAnswer}.")

if __name__ == "__main__":
  run()
