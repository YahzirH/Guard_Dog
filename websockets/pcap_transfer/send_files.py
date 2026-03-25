import asyncio
import websockets
import os

async def send_pcap_file(file_path, uri):
    async with websockets.connect(uri) as ws:
        print("Connection established.")

        transfer_consent = await ws.recv()
        print(transfer_consent)

        file_size = os.path.getsize(file_path)
        file_name = os.path.basename(file_path)
        
        print(f"Starting file transfer for {file_name} ({file_size} bytes)...")
        await ws.send(f"sending {file_name} ({file_size} bytes)...")
        with open(file_path, 'rb') as f:
              await ws.send(f.read()) 

        print(f"File {file_name} successfully sent.")

if __name__ == "__main__":
    websocket_uri = "ws://129.21.41.192:8000/" 
    pcap_file_path = "/home/kali/Documents/guard_dog/capture/wifi_capture.pcap" 

    # Check if file exists before attempting to send
    if os.path.isfile(pcap_file_path):
        asyncio.run(send_pcap_file(pcap_file_path, websocket_uri))
    else:
        print(f"Error: File not found at {pcap_file_path}")