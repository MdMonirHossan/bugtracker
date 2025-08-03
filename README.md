# Bug Tracker
A real-time bug tracking system built with Django, Django REST Framework (DRF), Django Channels (WebSocket), JWT authentication, and Redis for WebSocket communication.


## Features
- JWT-based authentication
- Project, Bug, Comment, and ActivityLog models
- Clean RESTful API with DRF
- CRUD API for (`Pagination`):
    - Project
    - Bug
    - Comment
    - Activity Log
- Real-time WebSocket updates for bug events and comments
- Redis-backed WebSocket support using Django Channels

## Setup Instructions
- **Clone the repo or Unzip the file.**
```bash
git clone git@github.com:MdMonirHossan/bugtracker.git
    
cd bugtracker
```
- **Create a virtual environment & Activate**
```bash 
python -m venv venv
```
- **Install dependencies**
```bash
pip install -r requirements.txt
```
- **Setup & run Redis in docker** 
<br><small>If you don't have redis setup locally</small>
```dockerfile
docker run -d --name redis -p 6379:6379 redis
```
- **Run migrations**
```bash
python mange.py migrate
```
- **Start server on port `8000` (Port should be `8000`)**
```bash
python manage.py runserver
```
App will be available at:
[http://localhost:8000](http://localhost:8000)

Swagger Docs
[http://localhost:8000/swagger](http://localhost:8000/swagger)

Redoc Docs
[http://localhost:8000/redoc](http://localhost:8000/redoc)

## WebSocket
**Available Socket URL**
`ws://localhost:8000/ws/project/<project_id>`
`ws://localhost:8000/ws/user/?token={access_token}`
`ws://localhost:8000/ws/logs/`
- Events:
  - `bug.created`
  - `bug.updated`
  - `comment.created`
  - `stream_log`

## Connect to WebSocket 
### WebSocket Test Script (Python) <br>
**`You'll find these script in project root directory`**
- **Project Room by Project ID (Create or Update Bug)** 
```bash 

cd /bugtracket/scripts/bug_websocket.py

# Run in multiple Terminal for joining in different project room
$ python bug_websocket.py
```
<small><b>***`This will ask for project ID`***<b></small>

- **User Room by User ID (Create Comment)**
```bash

cd /bugtracker/scripts/comment_websocket.py

# Run the script in multiple Terminal to get real-time notification
$ python comment_websocket.py
```
<small><b>***`This will ask for User Credentials`***</b></small>

- **Stream log**
```bash

cd /bugtracker/scripts/stream_log_websocket.py

# Run the script in multiple Terminal to get real-time notification
$ python stream_log_websocket.py
```

### WobSocket Test Script (`Javascript`):
- **Project Room by Project ID (Create or Update Bug)**
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
- **User Room by User ID (Create Comment)**
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

- **Stream Log room (Create)**
```javascript
// Run this script in multiple browser console. Try to run it under http://localhost:8000 to avoid "CSP connect src"
let socket = new WebSocket("ws://localhost:8000/ws/logs/");
	
	socket.onmessage = (event) => {
	  console.log("📨 Received:", JSON.parse(event.data));
	};
	
	socket.onopen = () => {
	  console.log("✅ WebSocket connected");
	};

```

## Project workflow/planning available at
**=> [Workflow/Planning](https://github.com/MdMonirHossan/bugtracker/blob/main/Project_planning.txt)**


## API Endpoints

| Method | Endpoint                                  | Description                   |
| ------ | ----------------------------------------- | ----------------------------- |
|        |                       **Auth**                                             |
| POST   | `/api/register`                           | User registration             |
| POST   | `/api/token`                              | Get JWT tokens                |
| POST   | `/api/token/refresh`                      | Get JWT tokens with Refresh   |
|        |                        **Project**                                         | 
| GET    | `/api/projects`                           | List user projects            |
| POST   | `/api/projects`                           | Create a new project          |
| GET    | `/api/projects/<id>`                      | Get project by ID             |
| PUT    | `/api/projects/<id>`                      | Update existing Project       |
| PATCH  | `/api/projects/<id>`                      | Partially Update a Project    |
| Delete | `/api/projects/<id>`                      | Delete a Project by ID        |
|        |                        **Bug**                                             |
| GET    | `/api/bugs`                               | List bugs                     |
| POST   | `/api/bugs`                               | Create new bugs               |
| GET    | `/api/bugs/<id>`                          | Get bug by ID                 |
| PUT    | `/api/bugs/<id>`                          | Update existing bug by ID     |
| PATCH  | `/api/bugs/<id>`                          | Partially Update bug by ID    |
| DELETE | `/api/bugs/<id>`                          | Delete bug by ID              |
| GET    | `/api/bugs/assigned`                      | Bugs assigned to request user |
| GET    | `/api/bugs/filter/?status=Open&project=1` | Filter bugs by status/project |
|        |                      **Comment**                                         |
| GET    | `/api/comments`                           | List Comments                 |
| POST   | `/api/comments`                           | Create new comment            |
| GET    | `/api/comments/<id>`                      | Get comment by ID             |
| PUT    | `/api/comments/<id>`                      | Update existing comment by ID |
| PATCH  | `/api/comments/<id>`                      | Partially Update comment by ID|
| DELETE | `/api/comments/<id>`                      | Delete comment by ID          |
|        |                        **Activity Log**                                  |
| GET    | `/api/activity_logs`                      | List logs                     |
| GET    | `/api/activity_logs/<id>`                 | Get logs by ID                |    