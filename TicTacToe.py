import tkinter as tk

class GameBoard:
    
    last_clicked = 2
    total_clicked = 0
    
    __slots__ = ['button','column', 'row', 'sign']
    
    style = {"width": 6, "height": 3, "bg": "#1a1a1a",
            "font": ("Helvetica", 25, "bold"), "relief": tk.FLAT}
    
    grid_style = {"sticky": tk.NSEW, "padx": 1, "pady": 1}
    
    def __init__(self, column, row):
        self.button = tk.Button(box_frame, cnf = GameBoard.style, command = self.click)
        self.button.grid(row = row, column = column, cnf = GameBoard.grid_style)
        self.column = column
        self.row = row
        self.sign = None

    @staticmethod
    def create_board():
        for y in range(3):
            row = [GameBoard(x, y) for x in range(3)]
            box_list.append(row)

    def click(self):       
        if GameBoard.last_clicked == 1 and self.sign == None:
            self.sign = 2
            self.button.config(text = "O", fg = "green")
            GameBoard.last_clicked = 2
            GameBoard.total_clicked += 1
        
        elif GameBoard.last_clicked == 2 and self.sign == None:
            self.sign = 1
            self.button.config(text = "X", fg = "red")
            GameBoard.last_clicked = 1
            GameBoard.total_clicked += 1
        
        turn_label.config(text = f"Last Played:\n player {GameBoard.last_clicked}")
        self.evaluate()

    def evaluate(self):
        x, y = self.column, self.row
        diagonals = [(0,0), (2,2), (1,1), (0,2), (2,0)]
        row_count, column_count = 0,0
        diagonal_count1, diagonal_count2 = 0,0
        
        #checks row
        for a in range(3):
            if box_list[y][a].sign == self.sign:
                row_count +=1
        
        #checks column
        for b in range(3):
            if box_list[b][x].sign == self.sign:
                column_count +=1
        
        #checks diagonals
        diagonals1 = diagonals[:3]
        for box in diagonals1:
            if box_list[box[0]][box[1]].sign==self.sign:
                diagonal_count1 +=1

        diagonals2 = diagonals[2:]
        for box in diagonals2:
            if box_list[box[0]][box[1]].sign==self.sign:
                diagonal_count2 +=1
       
        if row_count == 3 or column_count == 3 or diagonal_count1 == 3 or diagonal_count2 == 3:
            GameBoard.win()
            GameBoard.last_clicked = 3
            return True

        if GameBoard.total_clicked == 9:
            GameBoard.game_over()
            return True
        return False

    @staticmethod
    def win():
        turn_label.config(text = f'player {GameBoard.last_clicked}\nhas won',
                        fg = "red")
    
    @staticmethod
    def game_over():
        turn_label.config(text = f'Game Over',
                        fg = "red")

    @staticmethod
    def restart_board():
        box_list.clear()
        GameBoard.last_clicked = 2
        GameBoard.total_clicked = 0
        for box in box_frame.winfo_children():
            box.destroy()
        GameBoard.create_board()
        turn_label.config(text = "Last Played: ", fg = "yellow")

if __name__ == "__main__":

    box_list = []
    
    root = tk.Tk()
    root.resizable(False, False)
    
    box_frame = tk.Frame(root, bg = "black")
    box_frame.grid(row = 0, column = 0)

    GameBoard.create_board()
    menu_style = {"bg": "#1a1a1a", "fg": "yellow", "pady": 2,
                "font": ("Hevletica", 17, "bold"), "relief": tk.FLAT}
    
    menu_frame = tk.Frame(root, bg = "#1a1a1a", padx = 20)
    menu_frame.grid(row = 0, column = 1, sticky = tk.NSEW)

    restart_button = tk.Button(menu_frame,
                                cnf = menu_style,
                                text = "Restart",
                                command = GameBoard.restart_board)
    restart_button.grid(row = 0, column = 0, sticky = tk.NSEW, pady = 32)

    turn_label = tk.Label(menu_frame,
                        text = f"Last Played:",
                        cnf = menu_style)
    turn_label.grid(row = 1, column = 0, sticky = tk.NSEW, pady = 73)

    quit_button = tk.Button(menu_frame,
                            cnf = menu_style,
                            text = "Quit",
                            command = root.destroy)
    quit_button.grid(row = 2, column = 0, sticky = tk.NSEW, pady = 32)
    
    root.tk.mainloop()