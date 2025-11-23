import asyncio
import telnetlib3
import time
import string
#import snek

async def shell(reader, writer):
    writer.write("\r\nWelcome to Skai's Telnet Server!\r\n")
    writer.write('Type "exit" to disconnect.\r\n')
    while True:
        command = ""
        writer.write('>> ')
        while True:
            inp = await reader.read(1)
            if not inp:
                return

            writer.write(inp)
            if inp in ('\x08', '\x7f'):
                if command:
                    command = command[:-1]
                    writer.write("\b \b")
                continue

            if inp in ("\r", "\n"):
                break
            else:
                command += inp.lower()

        command = command.strip()
        if command == "help"
            writer.write('\r\nhelp - display this message')
            writer.write('\r\nhello - get a nice greeting')
            writer.write('\r\nsnek - play a game of snek')
            writer.write('\r\nclear - clear the screen')
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

        print(inp)
        print(command)

    writer.close()
async def cls(writer):
    writer.write("\\033[H\\033[2J")
    writer.write("\x1b[H\x1b[2J")
    await writer.drain()

#snek
async def snek(writer, reader):
    await cls(writer)
    writer.write("""Welcome to Snek!\r\n
Rules & Controls:\r\n
Control your snek with WASD\r\n
Do not hit the walls.\r\n
Eat beris to score points. (*)\r\n""")
    while True:
        inp = await reader.read(1)
        if not inp:
            break
        if inp in string.ascii_letters:
            break
    await cls(writer)
    #snek.main(writer, reader)


async def main():
    server = await telnetlib3.create_server(
        host='31.97.209.167',
        port=23,
        shell=shell
    )
    print(f"Telnet server listening on {server.sockets[0].getsockname()}")
    await server.wait_closed()

if __name__ == '__main__':
    asyncio.run(main())
