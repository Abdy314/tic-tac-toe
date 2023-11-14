from tkinter import *
import random


def next_turn(row, column):
    global player
    global players_wins
    global game_count
    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column]['text'] = player

        if check_winner() is False:
            player = players[0] if player == players[1] else players[1]
            label.config(text=(player + " turn"))
        elif check_winner() is True:
            label.config(text=(player + " wins"))
            game_count+=1
            game_count_label.config(text="Games Played: " + str(game_count))
            if player == "x":
                players_wins[0] += 1
            else:
                players_wins[1] += 1
            count_label.config(text=players[0] + " wins: " + str(players_wins[0]) + "       "
                         + players[1] + " wins: " + str(players_wins[1]))
        elif check_winner() == "Tie":
            game_count+=1
            game_count_label.config(text="Games Played: " + str(game_count))
            label.config(text="It's a Tie!!!!")


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    if buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    if empty_spaces() is False:
        return "Tie"
    return False


def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return True
    return False


def new_game():
    player = random.choice(players)
    label.config(text="Game restarted! " + player + " turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column]['text'] = ""
            buttons[row][column].config(bg='SystemButtonFace')


window = Tk()

window.title("Tic-Tac-Toe Game")

players = ["x", "o"]

player = random.choice(players)

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + " turn", font=('times new roman', 40))
label.pack(side="top")

players_wins = [0, 0]

game_count = 0
game_count_label = Label(text="Games Played: " + str(game_count), font=('times new roman', 40))
game_count_label.pack(side="bottom")

count_label = Label(text=players[0] + " wins: " + str(players_wins[0]) + "       "
                         + players[1] + " wins: " + str(players_wins[1]), font=('times new roman', 40))
count_label.pack(side="bottom")

reset = Button(text="restart", font=('times new roman', 20), command=new_game)
reset.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('times new roman', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
