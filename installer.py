import os
import time

os.system("cls")

while True:
  os.system("cls")
  print("")
  main = input(" Enter Your Library Name : ")
  
  try:
    os.system("cls")
    os.system("pip install " + main)
    
    time.sleep(4)
  except:
    print("")
    print(" I Can't Connect In A Moment Please Try Again")
    time.sleep(4)
