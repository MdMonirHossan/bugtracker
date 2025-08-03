import asyncio
import websockets

async def listen():

    uri = f"ws://localhost:8000/ws/logs/"
    
    try:
        async with websockets.connect(uri) as websocket:
            print(f"Connected to WebSocket: {uri}")
            await websocket.send("Hello from client")
            while True:
                response = await websocket.recv()
                print("Received:", response)
    except websockets.exceptions.ConnectionClosedOK:
        print("WebSocket connection closed normally.")
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"WebSocket connection closed with error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(listen())
