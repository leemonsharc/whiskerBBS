import asyncio
import telnetlib3
import time
import string
from snek import main as snakegame

# shell
async def shell(reader, writer):
    # welcome
    writer.write("\r\nWelcome to Skai's Telnet Server!\r\n")
    writer.write('Type "exit" to disconnect.\r\n')
    # process commands
    while True:
        # define command and write caret
        command = ""
        writer.write(':3 ')
        # input loop
        while True:
            inp = await reader.read(1)
            if not inp:
                return

            # echo
            writer.write(inp)
            # backspace
            if inp in ('\x08', '\x7f'):
                if command:
                    command = command[:-1]
                    writer.write("\b \b")
                continue

            # end line
            if inp in ("\r", "\n"):
                break
            #concat onto command to make command variable work
            else:
                command += inp.lower()

        # strip command
        command = command.strip()
        # if command is this, do that
        if command == "help":
            writer.write('\r\nhelp - display this message\r\n')
            writer.write('hello - get a nice greeting\r\n')
            writer.write('snek - play a game of snek\r\n')
            writer.write('clear - clear the screen\r\n')
        elif command == "exit":
            writer.write('\r\ngoodbye, my friend!\r\n')
            break
        elif command == "hello":
            writer.write('\r\nmeow!\r\n')
        elif command == "snek":
            await snek(writer, reader)
        elif command == "clear":
            await cls(writer)
        else:
            writer.write(f'\r\nUnknown command: {command}\r\n')

        # debug prints
        print(inp)
        print(command)

    writer.close()

# define cls
async def cls(writer):
    writer.write("\\033[H\\033[2J")
    writer.write("\x1b[H\x1b[2J")
    await writer.drain()

# snek
async def snek(writer, reader):
    # cls and rules
    await cls(writer)
    writer.write("""Welcome to Snek!\r\n
Rules & Controls:\r\n
Control your snek with WASD\r\n
Do not hit the walls.\r\n
Eat beris to score points. (*)\r\n""")
    # wait for input
    while True:
        inp = await reader.read(1)
        if not inp:
            break
        if inp in string.ascii_letters:
            break
    # cls and game
    await cls(writer)
    await snakegame(writer, reader)

# main
async def main():
    # define server
    server = await telnetlib3.create_server(
        host='31.97.209.167',
        port=23,
        shell=shell
    )
    # debug print
    print(f"Telnet server listening on {server.sockets[0].getsockname()}")
    await server.wait_closed()

# run main
if __name__ == '__main__':
    asyncio.run(main())

