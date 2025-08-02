import asyncio
import websockets

async def listen():
    project_id = input('Enter project id to join within a room: ')

    if not project_id:
        print("Project ID not provided. Exiting.")
        return


    uri = f"ws://localhost:8000/ws/project/{project_id}/"
    
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
