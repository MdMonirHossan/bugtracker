import asyncio
import websockets
import requests

async def listen():
    username = input('Enter a username: ')
    password = input('Enter password: ')

    if not (username and password):
        print("Please provide Username and Password. Exiting.")
        return

    payload = {
        'username': username.strip(), 
        'password': password.strip()
    }

    auth_response = requests.post('http://localhost:8000/api/token', data=payload)

    if not auth_response:
        print('Authentication failed!. Please provide valid credentials.')
        return 
    
    access_token = auth_response.json()['access']

    uri = f"ws://localhost:8000/ws/user/?token={access_token}"
    
    try:
        async with websockets.connect(uri) as websocket:
            print(f"Connected to WebSocket: {uri.split('?')[0]}")
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
