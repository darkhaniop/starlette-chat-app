# starlette-chat-sample

The purpose of this project is to check a minimal Starlette-based chat app functionality.
It also verifies the full-duplex communication capability over WebSockets.

> [!NOTE]
> This is only a basic example of a Starlette app, and not meant to be deployed for production.

## Usage

Start the server:
```shell
python app/main.py
```

In a web-browser, navigate to [localhost:8080/chat](http://localhost:8080/chat).
Messages would be received by all connected clients.

### Usage with FastAPI

Since FastAPI uses Starlette under the hood, this sample can be easily adapted to work with FastAPI.

## Limitations

As stated in the note above, this app is not meant to be used as is.
One of the limitations of the current implementation is the fact that upon receiving a new message, the server would attempt to send it to all previously connected clients in sequence.
Which means that some clients would experience unnecesssary delays.
Furthermore, the server does not skip already disconnected clients, which would introduce extra delays caused by socket errors.