import random
import numpy as np

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

class Game:

    state = State()

    def evaluation(self, state):
        winning_states = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]])
        for player in ("X", "O"):
            available_positions = state.chances_to_win(player) # get_available_positions()
            for winning_state in winning_states:
                player_win = True
                for i in winning_state:
                    if i not in available_positions:
                        player_win = False
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
            return 0 # Decimal(0)

    def min_value(self, state, player, depth, alpha, beta):
        if self.check_terminal(state) or depth > State.horizon:
            return self.utility(state)
        best = 1 # Decimal('Infinity')
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
        best = -1 # Decimal('-Infinity')
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

    def play_tic_tac_toe(self, state, depth, alpha, beta):
        while not self.is_end_game(state):
            human_action = self.get_input(state)
            state.board[human_action - 1] = "X"
            State.depth_tree += 1
            state.print_board(state.board)
            if self.is_end_game(state):
                return
            print("Computer choosing an action...")
            computer_action = self.alpha_beta(state, "O", depth, alpha, beta)
            state.board[computer_action] = "O"
            State.depth_tree += 1
            State.size_of_tree += State.node_counter
            State.node_counter = 1
            state.print_board(state.board)

    def is_end_game(self, state):
        return self.check_terminal(state)

    def changePlayer(self, player):
        if player == "X":
            return "O"
        else:
            return "X"

    def the_winner(self, state):
        if self.evaluation(state) == "X":
            return "YOU WINS!!"
        elif self.evaluation(state) == "O":
            return "AI WINS!!"
        elif self.check_terminal(state):
            return "TIE!!"

    def get_input(self, state):
        valid_input = False
        human_action = 0
        while not valid_input:
            try:
                human_action = int(input("You are X: Choose number from 1-9: "))
                if human_action in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                    if state.board[human_action - 1] == " ":
                        valid_input = True
                    else:
                        print('Invalid input, try again')
            except:
                print('Invalid input, try again')
        return human_action

    def horizon_selected(self):
        while True:
            try:
                horizon = int(input('Enter the horizon : '))
                if horizon >= 1 and horizon <= 9:
                    return horizon
                else:
                    print('Invalid input')
            except:
                print('Invalid input')

def main():
    MAX = 100  # Decimal('Infinity')
    MIN = -100  # Decimal('-Infinity')
    state = State()
    game = Game()
    want_to_play = "yes"
    while want_to_play == "yes":
        State.reset(state)
        state.clear_board()
        state.reset()
        State.horizon = game.horizon_selected()
        print()
        state.print_board(state.board)
        game.play_tic_tac_toe(state, 1, MIN, MAX)
        print('The depth of the tree : ' + str(State.depth_tree))
        print('The size of the tree :  ' + str(State.size_of_tree))
        print(game.the_winner(state))
        want_to_play = str(input("Wanna play again? (yes/no) : ").lower())

if __name__ == '__main__':
    main()