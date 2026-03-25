import asyncio
import websockets

async def recieve_confirmation(ws):
    print(f"Connection from: {ws.remote_address}")
    try:
        #Confirmation
        confirmation_message = await ws.recv()
        print(confirmation_message)
        await ws.send("Recieved Confirmation Successfully!")

    except websockets.exceptions.ConnectionClosed:
        print(f"Connection closed by client: {ws.remote_address}")
    
    finally:
        print(f"Handler for {ws.remote_address} finsihed")
        print("Closing server...")
        server.close()
        print("Server closed.")

async def main():
    global server
    server = await websockets.serve(recieve_confirmation, "0.0.0.0", 8000)
    print("Server running on ws://0.0.0.0:8000")

    await server.wait_closed()

if __name__ == "__main__":
    # Run the asynchronous server function
    asyncio.run(main())
