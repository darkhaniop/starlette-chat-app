import asyncio
from typing import cast

from hypercorn.asyncio import serve
from hypercorn.config import Config
from hypercorn.typing import Framework
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse, HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocket


async def websocket_endpoint(websocket: WebSocket) -> None:
    print(f"ws client: {hex(id(websocket))}")
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>WebSocket Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8080/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


async def chat_response(_request: Request) -> HTMLResponse:
    return HTMLResponse(html)


def create_app() -> Starlette:
    async def homepage(_request: Request) -> JSONResponse:
        return JSONResponse({"result": "Hello World!"})

    app = Starlette(
        debug=True,
        routes=[
            Route("/", homepage),
            Route("/chat", chat_response),
            WebSocketRoute("/ws", websocket_endpoint),
        ],
    )
    return app


def get_config() -> Config:
    config = Config()
    config.bind = ["localhost:8080"]
    config.use_reloader = True
    return config


def cli() -> None:
    asyncio.run(main())


async def main() -> None:
    app = create_app()
    config = get_config()
    shutdown_trigger = asyncio.Event()

    await serve(
        app=cast(Framework, app), config=config, shutdown_trigger=shutdown_trigger.wait
    )


if __name__ == "__main__":
    asyncio.run(main())
