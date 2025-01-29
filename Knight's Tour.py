#introduction of knight tours
#This "game" is basically an implementation of Knight's Tour problem.
#You have to produce the longest possible sequence of moves of a
#chess knight, while visiting squares on the board only once.
#This sequence is called "tour". If your tour visits every square,
#then you have achieved a full tour. If you have achieved a full tour
#and from your last position you could move to your initial square,
#then you have achieved a closed full tour.
#Currently occupied square is highlighted in pale blue,
# while possible moves are shown with pale green. Click on the
# currently occupied square to undo.

#chessboard
#one knight
#the next possible move
#move until no more possible move
#total move
#maths behind it

#https://www.youtube.com/watch?v=X-e0jk4I938&t=332s
#https://www.maths-resources.com/knights/

#standard chessboard
import matplotlib.pyplot as plt
import numpy as np

NO_OF_SPOKES = 18
#outline of chessboard
for i in range(NO_OF_SPOKES):
    plt.plot([i, i], [0, 8], color='black')  #Vertical lines
    plt.plot([0, 8], [i, i], color='black')  #Horizontal lines

#black and white square
for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 1:
            plt.scatter(col + 0.5, 7.5 - row, color='black', s=700, marker='s') #marker='s' stands for square shape

plt.gca().set_aspect("equal")
plt.axis([-1, 9, -1, 9])
plt.show()
##################################################################################################################################
#chessboard and knight
import matplotlib.pyplot as plt

# Chessboard setup
NO_OF_SPOKES = 18
board_size = 8
knight_position = (0, 0)  # Starting position of the knight

def draw_chessboard():
    """Draws the chessboard using the given outline."""
    plt.clf()

    # Outline of the chessboard
    for i in range(NO_OF_SPOKES):
        plt.plot([i, i], [0, 8], color='black')  # Vertical lines
        plt.plot([0, 8], [i, i], color='black')  # Horizontal lines

    # Black and white squares
    for row in range(board_size):
        for col in range(board_size):
            if (row + col) % 2 == 1:
                plt.scatter(col + 0.5, 7.5 - row, color='black', s=700, marker='s')  # Black squares


def draw_knight():
    """Draws the knight at its current position."""
    plt.text(knight_position[1] + 0.5, 7.5 - knight_position[0], '♘', fontsize=20, ha='center', va='center',
             color='pink')

#col + 0.5: Centers the piece in the column.
#7.5 - row: Places the top row at y = 7.5, making sure the pieces are properly positioned.

draw_chessboard()
draw_knight()

plt.gca().set_aspect("equal")
plt.axis([-1, 9, -1, 9])
plt.show()

########################################################################################################################
#click to move the knight
def on_click(event):
    """Handles user clicks, allowing the knight to move freely."""
    global knight_position

    col = int(round(event.xdata)) #event.xdata # X-coordinate of the click in figure coordinates
    row = int(round(7.5 - event.ydata)) #event.ydata # Y-coordinate of the click in figure coordinates
    knight_position = (row, col)  # Update knight position
#7.5 ensures clicks align better with the center of squares.
#Using int(round(7.5 - event.ydata)) guarantees accurate row mapping.
    draw_chessboard()
    draw_knight()
    plt.gca().set_aspect("equal")
    plt.axis([-1, 9, -1, 9])
    plt.draw()

draw_chessboard()
draw_knight()

plt.gca().set_aspect("equal")
plt.axis([-1, 9, -1, 9])
plt.gcf().canvas.mpl_connect('button_press_event', on_click)
#gcf : Get Current Figure : current Matplotlib figure object (the window displaying the chessboard)
#canvas : interactive area where Matplotlib draws plots. :  manages user interactions (like clicks, key presses, etc.).
#.mpl_connect() listens for specific events (such as mouse clicks).
#'button_press_event' This tells Matplotlib: "Listen for mouse button clicks."
#on_click → This is the function that handles the event when the user clicks.
plt.show()
