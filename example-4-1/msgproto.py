from asyncio import StreamReader, StreamWriter


async def read_msg(stream: StreamReader) -> bytes:
    size_bytes = await stream.readexactly(4)
    size = int.from_bytes(size_bytes, "big")
    data = await stream.readexactly(size)
    return data


async def send_msg(stream: StreamWriter, data: bytes) -> None:
    size_bytes = len(data).to_bytes(4, "big")
    stream.writelines([size_bytes, data])
    await stream.drain()
