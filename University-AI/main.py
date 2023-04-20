from tkinter import *
import Tic_Tac_Toe
from tkinter import messagebox

def myClick(symbol, h):

    if h != 0:
        root.destroy()
        new_mode.destroy()
        if symbol == 'm':
            Tic_Tac_Toe.h = h
            Tic_Tac_Toe.algo_selected = 'm'
            Tic_Tac_Toe.main()
        else:
            Tic_Tac_Toe.h = h
            Tic_Tac_Toe.algo_selected = 'a'
            Tic_Tac_Toe.main()
        return

    try:
        horizon = int(e.get())
        if horizon >= 1 and horizon <= 9:
            root.destroy()
            new_hor.destroy()
            if symbol == 'm':
                Tic_Tac_Toe.h = horizon
                Tic_Tac_Toe.algo_selected = 'm'
                Tic_Tac_Toe.main()
            else:
                Tic_Tac_Toe.h = horizon
                Tic_Tac_Toe.algo_selected = 'a'
                Tic_Tac_Toe.main()
        else:
            new_hor.destroy()
            messagebox.showerror("Invalid input")
    except:
        new_hor.destroy()
        messagebox.showerror("Invalid input")

def select_the_mode(symbol):
    global new_mode
    select_mode_horizon.destroy()
    new_mode = Tk()
    new_mode.title('Select the mode')
    width = 600  # Width
    height = 300  # Height
    screen_width = new_mode.winfo_screenwidth()
    screen_height = new_mode.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    new_mode.geometry('%dx%d+%d+%d' % (width, height, x, y))
    new_mode.resizable(0, 0)

    label = Label(new_mode, text="Select the mode.", font=("Helvetica", 20))

    b1 = Button(new_mode, text="Easy", font=("Helvetica", 20), height=3, width=8, bg="SystemButtonFace", command=lambda: myClick(symbol, 3))
    b1.grid(columnspan=5, row=5, column=0)
    b1.place(relx=0.2, rely=0.5, anchor='center')

    b2 = Button(new_mode, text="Normal", font=("Helvetica", 20), height=3, width=8, bg="SystemButtonFace", command=lambda: myClick(symbol, 6))
    b2.grid(columnspan=5, row=5, column=2)
    b2.place(relx=0.5, rely=0.5, anchor='center')

    b3 = Button(new_mode, text="Hard", font=("Helvetica", 20), height=3, width=8, bg="SystemButtonFace", command=lambda: myClick(symbol, 9))
    b3.grid(columnspan=5, row=5, column=4)
    b3.place(relx=0.8, rely=0.5, anchor='center')

    label.pack()

def select_the_horizon(symbol):
    global e, new_hor
    select_mode_horizon.destroy()
    new_hor = Tk()
    new_hor.title('Enter the horizon')
    width = 300  # Width
    height = 100  # Height
    screen_width = new_hor.winfo_screenwidth()
    screen_height = new_hor.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    new_hor.geometry('%dx%d+%d+%d' % (width, height, x, y))
    new_hor.resizable(0, 0)

    label = Label(new_hor, text="Enter the horizon.\n", font=("Helvetica", 10))
    label.pack()
    e = Entry(new_hor, justify=CENTER, width=10)
    e.pack()
    Button(new_hor, text="Enter", command=lambda : myClick(symbol, 0)).pack()

def play_mode_or_enter_horizon(symbol):
    global select_mode_horizon
    select_mode_horizon = Tk()
    select_mode_horizon.title('Tic Tac Toe')
    width = 600  # Width
    height = 300  # Height
    screen_width = select_mode_horizon.winfo_screenwidth()
    screen_height = select_mode_horizon.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    select_mode_horizon.geometry('%dx%d+%d+%d' % (width, height, x, y))
    select_mode_horizon.resizable(0, 0)

    label = Label(select_mode_horizon, text="Wanna to enter the horizon manually?\nor select default mode?", font=("Helvetica", 20))
    b1 = Button(select_mode_horizon, text="Default\nMode", font=("Helvetica", 20), height=3, width=8, bg="SystemButtonFace", command=lambda: select_the_mode(symbol))
    b1.grid(columnspan=5, row=5, column=0)
    b1.place(relx=0.25, rely=0.7, anchor='center')
    b2 = Button(select_mode_horizon, text="Enter\nhorizon", font=("Helvetica", 20), height=3, width=8, bg="SystemButtonFace", command=lambda: select_the_horizon(symbol))
    b2.grid(columnspan=5, row=5, column=2)
    b2.place(relx=0.75, rely=0.7, anchor='center')
    label.pack()

def run_min_max():
    play_mode_or_enter_horizon('m')

def run_alpha_beta():
    play_mode_or_enter_horizon('a')

def new_game():
    main()

def kill_app():
    root.destroy()

def main():
    global root, algo_selected
    root = Tk()
    root.title('Tic Tac Toe')
    width = 400  # Width
    height = 400  # Height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)

    label = Label(root, text="Welcome to Tic Tac Toe Game.\n\nPlease select the algorithm\nyou want.", font=("Helvetica", 20))
    b1 = Button(root, text="Min Max\nAlgorithm", font=("Helvetica", 15), height=2, width=9, bg="SystemButtonFace", command=lambda: run_min_max())
    b1.grid(columnspan=5, row=0, column=5)
    b1.place(relx=0.5, rely=0.5, anchor='center')

    b2 = Button(root, text="Alpha Beta\nAlgorithm", font=("Helvetica", 15), height=2, width=9, bg="SystemButtonFace", command=lambda: run_alpha_beta())
    b2.grid(columnspan=5, row=2, column=5)
    b2.place(relx=0.5, rely=0.7, anchor='center')

    b3 = Button(root, text="Exit", font=("Helvetica", 15), height=2, width=9, bg="SystemButtonFace", command=kill_app)
    b3.grid(columnspan=5, row=4, column=5)
    b3.place(relx=0.5, rely=0.9, anchor='center')
    label.pack()
    root.mainloop()

if __name__ == "__main__":
    main()





# import alpha_beta_xo
# import min_max_xo

# key = True
# while key:
#     print('WELCOME TO TIC TAC TOE GAME')
#     algo_select = str(input('Min-Max (m) or Alpha-Beta (a) : '))
#     if algo_select.lower() == 'm':
#         min_max_xo.main()
#     elif algo_select.lower() == 'a':
#         alpha_beta_xo.main()
#     else:
#         print('Invalid input')
#         continue
#     while True:
#         again = input('Wanna choose another algorithm? (y/n) : ')
#         if again.lower() == 'n':
#             key = False
#             break
#         if again.lower() != 'y':
#             print('Invalid input')
#             continue
#         else:
#             print(20 * '-')
#             break