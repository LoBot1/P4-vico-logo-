from pygame import *


# def equal(player1,player2,p4):
#     coup_win = 0
#     if coup_win == 4 :
#         print("win")dd
        


def table():
     print("salut joueur")
     P4 =[(0,0,0,0,0,0,0), 
          (0,0,0,0,0,0,0),
          (0,0,0,0,0,0,0),
          (0,0,0,0,0,0,0),
          (0,0,0,0,0,0,0),
          (0,0,0,0,0,0,0)]
     for i in P4 :
          print (i) 

def menu():
         
     choix = input("do you want play ('yes' or 'no'):")
     if choix == 'yes':
          return table()
     elif choix == "non":
          print ("np see you next") 
     else : 
          print("you have to answer 'yes' or 'non'") + menu()     
menu()
     

     # def table():
#      input("do you want play :")
#      if input == "yes":
#           return 
#           P4 =[(0,0,0,0,0,0,0), 
#      (0,0,0,0,0,0,0),
#      (0,0,0,0,0,0,0),
#      (0,0,0,0,0,0,0),
#      (0,0,0,0,0,0,0),
#      (0,0,0,0,0,0,0)]
#           for i in P4 :
#                print (i) 
#      elif input == "no":
#           return "okay np see you next"
#      else :
#           print ("error") + table()
          
# table() 