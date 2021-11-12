'''
Randomly generates word OR imput custom word.
Every guess the stickman gets closer to hanging.
Stickman:
 
 =========
 ]       ]
 ]       o
 ]      /#\ 
 ]     + # +
 ]      / \
_]_    =   =
'''
#Generate word or choose your own
#Show word hidden
#Guess a letter
#if letter not in word then draw the figure 1 step
#if good then unhide that letter



#Generate random word
import random
WORDS = ("cat","ssss")
Word = random.choice(WORDS)


#Start game
def Start():
  Win = False
  while Win == False:
    Hidden_Chars = len(Word)*'-'
    

    print("The word is : "+ Hidden_Chars  )
    print("You have "+ str(Amount_Wrong)  + " Wrong awnsers")
    print(" ")
    print(Figure_States[Amount_Wrong])
    Guessed_Letter = input("Guess a letter: ")


    # Only enter 1 letter
    if len(Guessed_Letter) > 1:
      print("____________Only enter enter 1 letter____________")
      print(Start())

    Index_In_Word = Word.find(Guessed_Letter)
    print(Index_In_Word)

    
    # Check if Guessed letter in word
    Wrong_Guessed = -1
    Amount_Wrong = 0
    if Wrong_Guessed == Index_In_Word:
      Amount_Wrong = Amount_Wrong + 1 

    else:
      print("Correct")  




# Figure states.
Figure_States = ["""
  
  
 
   
  
  
  
 __]__""","""
   
   ]       
   ]      
   ]     
   ]     
   ]     
   ]     
 __]__""" ,"""
   =========
   ]       
   ]      
   ]     
   ]     
   ]     
   ]     
 __]__""" ,"""
   =========
   ]       ]
   ]       o
   ]      
   ]     
   ]     
   ]     
 __]__"""  ,"""
   =========
   ]       ]
   ]       o
   ]       # 
   ]       # 
   ]      
   ]     
 __]__""" ,"""
   =========
   ]       ]
   ]       o
   ]      /#
   ]     + # 
   ]      
   ]     
 __]__"""  , """
   =========
   ]       ]
   ]       o
   ]      /#\ 
   ]     + # +
   ]      
   ]     
 __]__""" , """
   =========
   ]       ]
   ]       o
   ]      /#\ 
   ]     + # +
   ]      / 
   ]     =   
 __]__"""  ,"""
   =========
   ]       ]
   ]       o
   ]      /#\ 
   ]     + # +
   ]      / |
   ]     =   =
 __]__"""  ]



print(Start())


