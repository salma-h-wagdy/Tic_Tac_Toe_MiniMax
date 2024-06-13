
import random
#import tkinter as tk 
from tkinter import *  #maba7bsh el beta3 da



class Tic_Tac_Toe:
    def __init__(self, root,choice):
        self.root = root
        self.turns=["X","O"]
        self.grid = [[None for _ in range(3)] for _ in range(3)]
        self.turn=random.choice(self.turns)
        self.header_label= None
        self.choice=choice
        self.create_grid()
        
        
    
    def create_grid(self):
        self.header_label = Label(
            self.root,
            text=self.turn+"'s turn",
            font=("Comic Sans MS", 20, "bold"),
            foreground="#000000",  
            background="#F0F0F0", 
            borderwidth=1,  
            relief="groove",  
        )
        self.header_label.grid(column=0, row=0, padx=10, pady=10, sticky="w")

        game_frame = LabelFrame(self.root)
        game_frame.grid(column=0, row=1, padx=10, pady=10, sticky="w")

        for row in range(3):
            for column in range(3):
                    
                    self.grid[row][column] = Button(game_frame, text="",width=10, font=('Comic Sans MS',20),bg="#F0F0F0",
                                        command= lambda row=row, column=column: self.next_move(row,column))
                    
                
                # else:
                #    row,column= self.findBestMove(self.grid)
                #    self.grid[row][column] = Button(game_frame, text="",width=10, font=('Comic Sans MS',20),bg="#F0F0F0",
                #                         command= self.next_move(row,column))
                
                    self.grid[row][column].grid(row=row,column=column, padx=10, pady=10, ipadx=20, ipady=20)

       
        if(self.turn!=self.choice):
            self.mini_AI()
                    
        reset_button = Button(game_frame, text="Restart", command=self.new_game,bg="#d5d7d2",font=("Comic Sans MS", 14))
        reset_button.grid(column=0, row=3, columnspan=3, padx=10, pady=10, sticky="ew")




    def new_game(self):
        self.turn=random.choice(self.turns)
        self.header_label.config(text=f"{self.turn}'s turn")
        for row in range(3):
            for column in range(3):
                self.grid[row][column].config(text="",bg="#F0F0F0")
        if(self.turn!=self.choice):
            self.mini_AI()
    
    def next_move(self,row,column):
            
        if self.grid[row][column]['text']=="" and not self.check_grid():
            self.grid[row][column]['text'] = self.turn
            check=self.check_grid()
            if check is False:
                self.turn = self.turns[1] if self.turn == self.turns[0] else self.turns[0]
                self.header_label.config(text=f"{self.turn}'s turn")
                if(self.turn!=self.choice):
                    self.mini_AI()

            elif check is True:
                self.header_label.config(text=f"{self.turn} wins")
            elif check == "t":
                self.header_label.config(text="It's a tie!")

                

    def mini_AI(self):
        row,column= self.findBestMove()
        if self.grid[row][column]['text']=="" and not self.check_grid():
            self.grid[row][column]['text'] = self.turn
            check=self.check_grid()
            if check is False:
                self.turn = self.turns[1] if self.turn == self.turns[0] else self.turns[0]
                self.header_label.config(text=f"{self.turn}'s turn")
            elif check is True:
                self.header_label.config(text=f"{self.turn} wins")
            elif check == "t":
                self.header_label.config(text="It's a tie!")


    def check_grid(self):
            win=False
            for row in range(3):
                if self.grid[row][0]['text'] == self.grid[row][1]['text'] == self.grid[row][2]['text'] != "":
                    if(self.grid[row][0]['text']==self.choice):
                        self.highlight_winner([(row, i) for i in range(3)])
                    else:
                        self.highlight_loser([(row, i) for i in range(3)])
                    return True

            for column in range(3):
                if self.grid[0][column]['text'] == self.grid[1][column]['text'] == self.grid[2][column]['text'] != "":
                    if(self.grid[0][column]['text']==self.choice):
                        self.highlight_winner([(i, column) for i in range(3)])
                    else:
                        self.highlight_loser([(i, column) for i in range(3)])
                    return True

            if self.grid[0][0]['text'] == self.grid[1][1]['text'] == self.grid[2][2]['text'] != "":
                if(self.grid[0][0]['text']==self.choice):
                    self.highlight_winner([(i, i) for i in range(3)])
                else:
                        self.highlight_loser([(i, i) for i in range(3)])
                return True

            elif self.grid[0][2]['text'] == self.grid[1][1]['text'] == self.grid[2][0]['text'] != "":
                if(self.grid[0][2]['text']==self.choice):
                    self.highlight_winner([(i, 2-i) for i in range(3)])
                else:
                        self.highlight_loser([(i, 2-i) for i in range(3)])
                return True

            elif self.empty_squares() is False:

                for row in range(3):
                    for column in range(3):
                        self.highlight_tie()
                return "t"

            else:
                return False

    def highlight_winner(self, positions):
        for row, column in positions:
            self.grid[row][column].config(bg="#4ada2f")

    def highlight_loser(self, positions):
        for row, column in positions:
            self.grid[row][column].config(bg="#fc1c3e")            

    def highlight_tie(self):
        for row in range(3):
            for column in range(3):
                self.grid[row][column].config(bg="#f89c0d")

    def empty_squares(self):

        return any(self.grid[row][column]['text'] == "" for row in range(3) for column in range(3))

    def minimax(self, depth, isMax) :  
        score = self.evaluate() 

        if (score == 10) :  
            return score 
    
       
        if (score == -10) : 
            return score 
    
       
        if (self.empty_squares()) : 
            return 0
    
        if (isMax) :      
            best = -1000 
    
            for i in range(3) :
                for j in range(3) : 
                
                    if (self.grid[i][j]['text']=="") : 
                    
                        self.grid[i][j]['text'] = self.turn  
    
                        best = max( best, self.minimax( depth + 1,not isMax) ) 
    
                        self.grid[i][j]['text']=""
            return best 
    
        else : 
            best = 1000 
    
            for i in range(3) :          
                for j in range(3) : 
                
                    if (self.grid[i][j]['text']=="") : 
                    
                        self.grid[i][j]['text'] = self.turn  
    
                        
                        best = min(best, self.minimax( depth + 1, not isMax)) 
    
                        self.grid[i][j]['text']=""
            return best 
    
    def findBestMove(self) :  
        bestVal = -1000 
        bestMove = (-1, -1)  
    
        
        for i in range(3) :      
            for j in range(3) : 
            
                if (self.grid[i][j]['text']=="") :  
                
                    self.grid[i][j]['text'] = self.turn 
    
                    moveVal = self.minimax( 0, False)  
    
                    self.grid[i][j]['text']=""
    
                   
                    if (moveVal > bestVal) :                 
                        bestMove = (i, j) 
                        bestVal = moveVal 
    
        return bestMove 


    def evaluate(self):
        for row in range(3):
            if self.grid[row][0]['text'] == self.grid[row][1]['text'] == self.grid[row][2]['text'] != "":
                return 10 if self.grid[row][0]['text'] != self.choice else -10

        for column in range(3):
            if self.grid[0][column]['text'] == self.grid[1][column]['text'] == self.grid[2][column]['text'] != "":
                return 10 if self.grid[0][column]['text'] != self.choice else -10

        if self.grid[0][0]['text'] == self.grid[1][1]['text'] == self.grid[2][2]['text'] != "":
            return 10 if self.grid[0][0]['text'] != self.choice else -10

        if self.grid[0][2]['text'] == self.grid[1][1]['text'] == self.grid[2][0]['text'] != "":
            return 10 if self.grid[0][2]['text'] != self.choice else -10

        return 0

