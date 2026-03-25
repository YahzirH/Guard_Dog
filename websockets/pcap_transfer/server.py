import asyncio
import websockets

async def recieve_pcap(ws):
    print(f"Connection from: {ws.remote_address}")
    try:
        #Recieve pcap name & size
        await ws.send("Ready to recieve files.")
        pcap_data = await ws.recv()
        print(pcap_data)

        #Recieve pcap file
        pcap_file = await ws.recv()
        with open("received.pcap", "wb") as f:
            f.write(pcap_file)

    except websockets.exceptions.ConnectionClosed:
        print(f"Connection closed by client: {ws.remote_address}")
    finally:
        print(f"Handler for {ws.remote_address} finsihed")

async def main():
    async with websockets.serve(recieve_pcap, "0.0.0.0", 8000):
        print("Server running on ws://0.0.0.0:8000")
        await asyncio.Future()

if __name__ == "__main__":
    # Run the asynchronous server function
    asyncio.run(main())