import asyncio
import websockets

async def recieve_confirmation(ws):
    print(f"Connection from: {ws.remote_address}")
    try:
        file_bytes = await ws.recv()
        print(file_bytes)
        await ws.send("Recieved Confirmation Successfully!")
    except websockets.exceptions.ConnectionClosed:
        print(f"Connection closed by client: {ws.remote_address}")
    finally:
        print(f"Handler for {ws.remote_address} finsihed")

async def main():
    async with websockets.serve(recieve_confirmation, "0.0.0.0", 8000):
        print("Server running on ws://0.0.0.0:8000")
        await asyncio.Future()

if __name__ == "__main__":
    # Run the asynchronous server function
    asyncio.run(main())
