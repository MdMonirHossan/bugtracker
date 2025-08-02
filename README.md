# Bug Tracker
A real-time bug tracking system built with Django, Django REST Framework (DRF), Django Channels (WebSocket), JWT authentication, and Redis for WebSocket communication.


## Features
- JWT-based authentication
- Project, Bug, Comment, and ActivityLog models
- Real-time WebSocket updates for bug events and comments
- Clean RESTful API with DRF
- Redis-backed WebSocket support using Django Channels

## Setup Instructions
- Clone the repo or Unzip the file.
```bash
git clone git@github.com:MdMonirHossan/bugtracker.git
    
cd bugtracker
```
- Create a virtual environment & Activate
```bash 
python -m venv venv
```
- Install dependencies
```bash
pip install -r requirements.txt
```
- Setup & run Redis in docker
```dockerfile
docker run -d --name redis -p 6379:6379 redis
```
- Run migrations
```bash
python mange.py migrate
```
- Start server on port `8000` (Port should be `8000`)
```bash
python manage.py runserver
```
App will be available at:
[http://localhost:8000](http://localhost:8000)

Swagger Docs
[http://localhost:8000/swagger](http://localhost:8000/swagger)

Redoc Docs
[http://localhost:8000/redoc](http://localhost:8000/redoc)

## 💬 WebSocket
**Available Socket URL**
`ws://localhost:8000/ws/project/<project_id>`
`ws://localhost:8000/ws/user/?token={access_token}`
- Events:
  - `bug.created`
  - `bug.updated`
  - `comment.created`

## Connect to WebSocket 
### WebSocket Test Script (Python) <small>You'll find these script in project root directory</small>
- Project Room by Project ID(Create or Update Bug) 
```bash 
/bugtracket/scripts/bug_websocket.py
# Run in multiple Terminal for joining in different project room
$ python bug_websocket.py
```

- User Room by User ID (Create Comment)
```bash
/bugtracker/scripts/comment_websocket.py

# Run the script in multiple Terminal to get real-time notification
$ python comment_websocket.py
```

### WobSocket Test Script (`Javascript`):
- Project Room by Project ID (Create or Update Bug)
```javascript
// Run this script in multiple browser console with different project ID. Try to run it under http://localhost:8000 to avoid CSP connect src
let socket = new WebSocket("ws://localhost:8000/ws/project/2/");
	
	socket.onmessage = (event) => {
	  console.log("📨 Received:", JSON.parse(event.data));
	};
	
	socket.onopen = () => {
	  console.log("✅ WebSocket connected");
	};

```
- User Room by User ID (Create Comment)
```javascript
// Run this script in multiple browser console with different access token. Try to run it under http://localhost:8000 to avoid CSP connect src
const token = "jwt_token"
	let socket = new WebSocket(`ws://localhost:8000/ws/user/?token=${token}`)

	socket.onmessage = (event) => {
	  console.log("📨 Received:", JSON.parse(event.data));
	};

	socket.onopen = () => {
	  console.log("✅ WebSocket connected");
	};
```



## API Endpoints

- POST `/api/token/`: Get JWT
- GET `/api/bugs/assigned/`: Bugs assigned to you
- GET `/api/bugs/filter_by_status/?status=Open&project=1`

| Method | Endpoint                      | Description                   |
| ------ | ----------------------------- | ----------------------------- |
| POST   | `/api/register`               | User registration             |
| POST   | `/api/token`                  | Get JWT tokens                |
| POST   | `/api/token/refresh`          | Get JWT tokens with Refresh                |
| GET    | `/api/projects`               | List user projects            |
| POST   | `/api/projects/`              | Create a new project          |
| GET    | `/api/bugs/`                  | List bugs                     |
| GET    | `/api/bugs/assigned/`         | Bugs assigned to current user |
| GET    | `/api/bugs/filter_by_status/` | Filter bugs by status/project |
| POST   | `/api/comments/`              | Add comment to a bug          |


