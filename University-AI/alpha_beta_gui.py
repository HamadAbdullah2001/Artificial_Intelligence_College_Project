from tkinter import *
from tkinter import messagebox
import random
import numpy as np
import main as m
import time

class Time:

    total_search_time = 0

class State:

    depth_tree = 0
    horizon = 0
    size_of_tree = 0
    node_counter = 1
    board = np.array([" ", " ", " ", " ", " ", " ", " ", " ", " "])

    def reset(self):
        State.depth_tree = 0
        State.horizon = 0
        State.size_of_tree = 0
        State.node_counter = 1
        State.board = np.array([" ", " ", " ", " ", " ", " ", " ", " ", " "])

    def print_board(self, board):
        for i in range(0, board.size, 3):
            print(self.board[i] + ' | ' + self.board[i+1] + ' | ' + self.board[i+2])
            if i >= 6:
                break
            print(9 * '-')

    def clear_board(self):
        self.board = np.array([" ", " ", " ", " ", " ", " ", " ", " ", " "])

    def successors(self):
        moves = []
        for i in range(0, self.board.size):
            if self.board[i] == ' ':
                moves.append(i)
        return moves

    def chances_to_win(self, symbol):
        best_chances = []
        for i in range(0, self.board.size):
            if self.board[i] == symbol:
                best_chances.append(i)
        return best_chances

class Alpha_Beta_Pruning_Algorithm:

    state = State()

    def evaluation(self, state):
        winning_states = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]])
        for player in ("X", "O"):
            best_positions = state.chances_to_win(player)
            for winning_state in winning_states:
                player_win = True
                for i in winning_state:
                    if i not in best_positions:
                        player_win = False
                        break
                if player_win:
                    return player
        return None

    def check_terminal(self, state):
        if self.evaluation(state) != None:
            return True
        for i in state.board:
            if i == " ":
                return False
        return True

    def utility(self, state):
        if self.evaluation(state) == "X":
            return -100 # Decimal('-Infinity')
        elif self.evaluation(state) == "O":
            return 100 # Decimal('Infinity')
        else:
            return 0 # 0

    def min_value(self, state, player, depth, alpha, beta):
        if self.check_terminal(state) or depth > State.horizon:
            return self.utility(state)
        best = 1  # Decimal('Infinity')
        for a in state.successors():
            State.node_counter += 1
            state.board[a] = player
            v = self.max_value(state, self.changePlayer(player), depth + 1, alpha, beta) + best
            state.board[a] = " "
            best = np.minimum(best, v)
            beta = np.minimum(best, beta)
            if beta <= alpha:
                break
        return best

    def max_value(self, state, player, depth, alpha, beta):
        if self.check_terminal(state) or depth > State.horizon:
            return self.utility(state)
        best = -1  # Decimal('-Infinity')
        for a in state.successors():
            State.node_counter += 1
            state.board[a] = player
            v = self.min_value(state, self.changePlayer(player), depth + 1, alpha, beta) + best
            state.board[a] = " "
            best = np.maximum(best, v)
            alpha = np.maximum(alpha, best)
            if beta <= alpha:
                break
        return best

    def alpha_beta(self, state, player, depth, alpha, beta):
        choices = {}
        for a in state.successors():
            State.node_counter += 1
            state.board[a] = player
            v = self.min_value(state, self.changePlayer(player), depth + 1, alpha, beta)
            state.board[a] = " "
            if v >= 0:
                choices[a] = v
        if len(choices) > 0:
            return self.largest(state, choices)
        else:
            return random.choice(state.successors())

    def largest(self, state, dic):
        max = list(dic.values())[0]
        ind = list(dic.keys())[0]
        for i in dic.keys():
            if dic[i] > max and state.board[i] == ' ':
                max = dic[i]
                ind = i
        print('Best action of the set of choices to move : ' + str(ind))
        return ind

    def is_end_game(self, state):
        return self.check_terminal(state)

    def changePlayer(self, player):
        if player == "X":
            return "O"
        else:
            return "X"

class Game:

    # Disable all buttons

    def disable_enable_all_buttons(self, state):
        for i in buttons:
            i.config(state=state)

    # Check who wins :

    def check_win(self, symbol):
        global winner, msg
        winner = False
        msg = ""
        if buttons[0]["text"] == buttons[1]["text"] == buttons[2]["text"] == symbol:
            winner = True
            msg = (symbol + " WINS")
            self.disable_enable_all_buttons(DISABLED)
            self.open_win()
        elif buttons[3]["text"] == buttons[4]["text"] == buttons[5]["text"] == symbol:
            winner = True
            msg = (symbol + " WINS")
            self.disable_enable_all_buttons(DISABLED)
            self.open_win()
        elif buttons[6]["text"] == buttons[7]["text"] == buttons[8]["text"] == symbol:
            winner = True
            msg = (symbol + " WINS")
            self.disable_enable_all_buttons(DISABLED)
            self.open_win()

        elif buttons[0]["text"] == buttons[3]["text"] == buttons[6]["text"] == symbol:
            winner = True
            msg = (symbol + " WINS")
            self.disable_enable_all_buttons(DISABLED)
            self.open_win()
        elif buttons[1]["text"] == buttons[4]["text"] == buttons[7]["text"] == symbol:
            winner = True
            msg = (symbol + " WINS")
            self.disable_enable_all_buttons(DISABLED)
            self.open_win()
        elif buttons[2]["text"] == buttons[5]["text"] == buttons[8]["text"] == symbol:
            winner = True
            msg = (symbol + " WINS")
            self.disable_enable_all_buttons(DISABLED)
            self.open_win()

        elif buttons[0]["text"] == buttons[4]["text"] == buttons[8]["text"] == symbol:
            winner = True
            msg = (symbol + " WINS")
            self.disable_enable_all_buttons(DISABLED)
            self.open_win()
        elif buttons[2]["text"] == buttons[4]["text"] == buttons[6]["text"] == symbol:
            winner = True
            msg = (symbol + " WINS")
            self.disable_enable_all_buttons(DISABLED)
            self.open_win()

        if counter == 9 and not winner:
            msg = ("TIE!!")
            self.disable_enable_all_buttons(DISABLED)
            self.open_win()

    def computer_move(self):
        self.disable_enable_all_buttons(DISABLED)
        MIN = -100
        MAX = 100
        start = time.time()
        computer_move = algorithm.alpha_beta(state, "O", 1, MIN, MAX)
        end = time.time() - start
        Time.total_search_time += end
        buttons[computer_move]["text"] = "O"
        # buttons[computer_move].config(image=PhotoImage(file="C:\\Users\\Hamad\\AI_Project\\images\\zero.png", master=root))
        # buttons[computer_move].pack(side=TOP)
        state.board[computer_move] = "O"
        buttons[computer_move].invoke()
        State.depth_tree += 1
        State.size_of_tree += State.node_counter
        State.node_counter = 1
        self.disable_enable_all_buttons(NORMAL)
        self.check_win("O")

    # Button clicked function :

    def b_click(self, button : Button, ind : int):
        global clicked, counter
        if button["text"] == " " and clicked:
            button["text"] = "X"
            # button.config(image=PhotoImage(file="C:\\Users\\Hamad\\AI_Project\\images\\cross.png", master=root))
            state.board[ind] = "X"
            clicked = False
            counter += 1
            self.check_win("X")
            if winner:
                return
            State.depth_tree += 1
            State.node_counter += 1
            self.computer_move()
        elif button["text"] == " " and not clicked:
            clicked = True
            counter += 1
        else:
            messagebox.showerror("Tic Tac Toe", "This box is already selected\nPlease pick another box...")

    # Reset Game :

    def reset(self):
        # X starts first :
        global clicked, counter
        clicked = True
        counter = 0

        # Define the buttons :
        global buttons, state, algorithm
        state = State()
        algorithm = Alpha_Beta_Pruning_Algorithm()
        State.reset(state)
        state.clear_board()
        state.reset()
        State.horizon = h

        buttons = [
            Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda : self.b_click(buttons[0], 0)),
            Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda : self.b_click(buttons[1], 1)),
            Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda : self.b_click(buttons[2], 2)),
            Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda : self.b_click(buttons[3], 3)),
            Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda : self.b_click(buttons[4], 4)),
            Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda : self.b_click(buttons[5], 5)),
            Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda : self.b_click(buttons[6], 6)),
            Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda : self.b_click(buttons[7], 7)),
            Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda : self.b_click(buttons[8], 8)),
        ]

        # Grid the buttons onto the screen :

        buttons[0].grid(row=0, column=0)
        buttons[1].grid(row=0, column=1)
        buttons[2].grid(row=0, column=2)

        buttons[3].grid(row=1, column=0)
        buttons[4].grid(row=1, column=1)
        buttons[5].grid(row=1, column=2)

        buttons[6].grid(row=2, column=0)
        buttons[7].grid(row=2, column=1)
        buttons[8].grid(row=2, column=2)

    def open_win(self):
        global new
        root.destroy()
        new = Tk()
        new.title("New Window")
        width = 700  # Width
        height = 300  # Height
        screen_width = new.winfo_screenwidth()
        screen_height = new.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        new.geometry('%dx%d+%d+%d' % (width, height, x, y))
        new.resizable(0, 0)

        if msg.__contains__("X"):
            color = "green"
            message = msg + "\nHumans still smarters!!"
        elif msg.__contains__("O"):
            color = "red"
            message = msg + "\nAI will control the world!!"
        else:
            color = "orange"
            message = msg
        label = Label(new, text="\n" + message + "\nWanna play again?", fg=color, font=("Helvetica", 20))
        b1 = Button(new, text="Try Again", font=("Helvetica", 20), height=3, width=8, bg="SystemButtonFace", command=lambda: self.create_root())
        b1.grid(columnspan=5, row=5, column=0)
        b1.place(relx=0.25, rely=0.7, anchor='center')
        b2 = Button(new, text="Main menu", font=("Helvetica", 20), height=3, width=8, bg="SystemButtonFace", command=lambda: self.main_menu())
        b2.grid(columnspan=5, row=5, column=2)
        b2.place(relx=0.75, rely=0.7, anchor='center')
        label.pack()

        results = "\n\n\nThe depth of the tree : " + str(State.depth_tree)
        results += "\nThe size of the tree : " + str(State.size_of_tree)
        results += "\nThe total search time : " + str(Time.total_search_time)[0:4] + " s"
        label2 = Label(new, text=results, font=("Helvetica", 10))
        label2.pack()

    def main_menu(self):
        new.destroy()
        m.new_game()

    def create_root(self):
        new.destroy()
        main()

    def exit_game(self):
        root.destroy()
        m.new_game()

def main():
    global root, h
    State.horizon = h
    game = Game()
    root = Tk()
    root.title('Tic Tac Toe')
    root.eval('tk::PlaceWindow . center')
    root.resizable(0, 0)
    menu = Menu(root)
    root.config(menu=menu)
    options = Menu(menu, tearoff=False)
    menu.add_cascade(label="Options", menu=options)
    options.add_command(label="Reset Game", command=game.reset)
    options.add_command(label="Exit Game", command=game.exit_game)
    game.reset()

    root.mainloop()

if __name__ == "__main__":
    main()