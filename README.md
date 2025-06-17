# starlette-chat-sample

The purpose of this project is to check a minimal Starlette-based chat app.
It also verifies the full-duplex communication capability.

## Usage

Start the server:
```shell
python app/main.py
```

In a web-browser, navigate to [localhost:8080/chat](http://localhost:8080/chat).
Messages are received by all connected clients.

### Usage with FastAPI

Since FastAPI uses Starlette under the hood, this sample can be easily adapted to work with FastAPI.