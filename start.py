from tkinter import *
from Game import Tic_Tac_Toe

class Start:
    def __init__(self, root):
        self.root = root
        self.choice = None
        self.page()
        
        
    
    def page(self):
        self.header_label = Label(
            self.root,
            text="Choose a Letter",
            font=("Comic Sans MS", 30, "bold"),
            foreground="#000000",  
            background="#F0F0F0", 
            borderwidth=1,  
            relief="groove",  
        )
        self.header_label.grid(column=0, row=0,columnspan=3, padx=10, pady=10, sticky="w")

        x_button = Button(self.root, text="X",bg="#d5d7d2",font=("Comic Sans MS", 20), command=self.set_x)
        x_button.grid(column=0, row=2, padx=10, pady=10, sticky="ew")

        o_button = Button(self.root, text="O",bg="#d5d7d2",font=("Comic Sans MS", 20),command=self.set_o)
        o_button.grid(column=1, row=2, padx=10, pady=10, sticky="ew")
    
    def set_x(self):
        self.choice ="X"
        self.start_game()
    def set_o(self):
        self.choice ="O"
        self.start_game()

    def start_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        Tic_Tac_Toe(self.root, self.choice, quit_callback=self.quit_to_start)

    def quit_to_start(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.page()