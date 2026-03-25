import asyncio
import websockets

async def send_confirmation():
    uri = "ws://129.21.41.192:8000"
    async with websockets.connect(uri) as ws:
        await ws.send("Up and running!") 
        response = await ws.recv()
        print("Server response:", response)

if __name__ == "__main__":
    asyncio.run(send_confirmation())