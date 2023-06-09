import asyncio
from asyncio import StreamReader, StreamWriter


async def echo(reader: StreamReader, writer: StreamWriter):
    print("new connection")
    try:
        while data := await reader.readline():
            writer.write(data.upper())
            await writer.drain()
        print("leaving connection")
    except asyncio.CancelledError:
        print("cancelled connection")


async def main(host="127.0.0.1", port=8888):
    server = await asyncio.start_server(echo, host, port)
    async with server:
        await server.serve_forever()


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("shutting down")
