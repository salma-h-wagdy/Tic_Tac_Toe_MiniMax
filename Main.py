from tkinter import *

# from Game import Tic_Tac_Toe
from start import Start
def main():
    root = Tk()
    root.title("Tic Tac Toe Game :D")
    # Tic_Tac_Toe(root)
    Start(root)
    root.mainloop()


if __name__ == "__main__":
    main()
