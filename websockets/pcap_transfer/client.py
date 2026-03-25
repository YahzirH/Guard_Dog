import asyncio
import websockets

async def send_file():
    uri = "ws://129.21.41.192:8000"
    async with websockets.connect(uri) as ws:
        with open("/home/kali/Documents/guard_dog/test_file.txt", "rb") as f:  #open file in binary mode
            file_bytes = f.read()
        await ws.send(file_bytes)  # send bytes
        response = await ws.recv()
        print("Server response:", response)

if __name__ == "__main__":
    asyncio.run(send_file())