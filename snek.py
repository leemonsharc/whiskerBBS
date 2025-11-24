import asyncio
import time
import random

# initiate variables
foodPos = (random.randint(1, 20), random.randint(1, 20))
snek = {
    length = 3
    ate = False

        }

# create the board
board = (
"|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\r\n"
"||\r\n"
"||\r\n"
"||\r\n"
"||\r\n"
"||\r\n"
"||\r\n"
"||\r\n"
"||\r\n"
"||\r\n"
"||\r\n"
"||\r\n"
"||\r\n"
"||\r\n"
"||\r\n"
"||\r\n"
"||\r\n"
"||\r\n"
"||\r\n"
"||\r\n"
"||\r\n"
"|_____________________________________________|\r\n"
)
# process board
lines = board.splitlines()
innerWidth = len(lines[0]) - 2  # subtract the two border chars
boardMid = ["|" + (" " * innerWidth) + "|" for _ in range(20)]
board = [lines[0]] + boardMid + [lines[-1]]
board = "\r\n".join(board)

# function to update the board
def updateBoard():
    if snek.ate:
        foodPos = (random.randint(1, 45), random.randint(1, 20)

# main function
async def main(writer, reader):
    while True:
        writer.write(board)
        time.sleep(0.05)
        updateBoard()
