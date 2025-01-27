#two rooks
import matplotlib.pyplot as plt
import random

NO_OF_SPOKES = 18
rook_location = []
while len(rook_location) < 2:
    row = random.randint(0, 7)
    col = random.randint(0, 7)
    if not any(r == row or c == col for r, c in rook_location): #To ensure no rook is in the same column or row
        rook_location.append((row, col))
print(f"A non-challenging configuration with 2 rooks at {rook_location}")

#outline of chessboard
for i in range(NO_OF_SPOKES):
    plt.plot([i, i], [0, 8], color='black')  #Vertical lines
    plt.plot([0, 8], [i, i], color='black')  #Horizontal lines

#black and white square
for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 1:
            plt.scatter(col + 0.5, 7.5 - row, color='black', s=700, marker='s') #marker='s' stands for square shape

for rook in rook_location:
    plt.text(rook[1] + 0.5, 7.5 - rook[0], '♖', fontsize=20, ha='center', va='center', color='pink') #ha = horizontal, va = vertical
#plt.text(x, y, s, ..) #x coor, y coor, string to display

plt.gca().set_aspect("equal")
plt.axis([-1, 9, -1, 9])
plt.show()

#modify version
import random
import matplotlib.pyplot as plt

def rooks_proportion(n): #n is the number of trials
    non_challenging_count = 0
    for i in range(n):
        rook1 = (random.randint(0, 7), random.randint(0, 7))
        rook2 = (random.randint(0, 7), random.randint(0, 7))

        if rook1[0] != rook2[0] and rook1[1] != rook2[1]: #check if its non-challenging or not
            non_challenging_count += 1

    proportion = non_challenging_count / n
    print(f"Proportion of non-challenging configurations: {proportion:.2f}")

#main program
n = 1000
rooks_proportion(n)

#three rooks
import random
import matplotlib.pyplot as plt

NO_OF_SPOKES = 18
def rooks_proportion(n):
    non_challenging_count = 0

    for i in range(n):
        rook1 = (random.randint(0, 7), random.randint(0, 7))
        rook2 = (random.randint(0, 7), random.randint(0, 7))
        rook3 = (random.randint(0, 7), random.randint(0, 7))

        if rook1[0] != rook2[0] and rook1[1] != rook2[1] and rook1[0] != rook3[0] and rook1[1] != rook3[1] and rook2[0] != rook3[0] and rook2[1] != rook3[1]:
            non_challenging_count += 1

    proportion = non_challenging_count / n
    print(f"Proportion of non-challenging configurations: {proportion:.2f}")

    for i in range(NO_OF_SPOKES):
        plt.plot([i, i], [0, 8], color='black')  #Vertical lines
        plt.plot([0, 8], [i, i], color='black')  #Horizontal lines

    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 1:
                plt.scatter(col + 0.5, 7.5 - row, color='black', s=700, marker='s')

    for rook in [rook1, rook2, rook3]:
        plt.text(rook[1] + 0.5, 7.5 - rook[0], '♖', fontsize=20, ha='center', va='center', color='pink')

    plt.gca().set_aspect("equal")
    plt.axis([-1, 9, -1, 9])
    plt.show()

#main program
n = 1000
rooks_proportion(n)

#n rooks
import random
import matplotlib.pyplot as plt

NO_OF_SPOKES = 18

def rooks_proportion(num_of_rooks, n):
    non_challenging_count = 0

    for i in range(n):
        rooks = []
        for j in range(num_of_rooks):
            rooks.append((random.randint(0, 7), random.randint(0, 7)))

        non_challenging = True
        for i in range(num_of_rooks):
            for j in range(i + 1, num_of_rooks):
                if rooks[i][0] == rooks[j][0] or rooks[i][1] == rooks[j][1]:
                    non_challenging = False

        if non_challenging:
            non_challenging_count += 1

    proportion = non_challenging_count / n
    print(f"Proportion of non-challenging configurations: {proportion:.2f}")

    for i in range(NO_OF_SPOKES):
        plt.plot([i, i], [0, 8], color='black')  #Vertical lines
        plt.plot([0, 8], [i, i], color='black')  #Horizontal lines

    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 1:
                plt.scatter(col + 0.5, 7.5 - row, color='black', s=700, marker='s')

    for rook in rooks:
        plt.text(rook[1] + 0.5, 7.5 - rook[0], '♖', fontsize=20, ha='center', va='center', color='pink')

    plt.gca().set_aspect("equal")
    plt.axis([-1, 9, -1, 9])
    plt.show()

#main program
n = 1000
num_of_rooks = int(input("Enter number of rooks between 2 and 8: "))

if num_of_rooks >= 2 and num_of_rooks <= 8:
    rooks_proportion(num_of_rooks, n)
else:
    print("bro invalid. Please enter a number between 2 and 8 only.")
