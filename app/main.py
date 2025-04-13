import asyncio
from typing import cast

from hypercorn.asyncio import serve
from hypercorn.config import Config
from hypercorn.typing import Framework
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


def create_app():
    async def homepage(request) -> JSONResponse:
        return JSONResponse({"result": "Hello World!"})

    app = Starlette(debug=True, routes=[Route("/", homepage)])
    return app


def get_config() -> Config:
    config = Config()
    config.bind = ["localhost:8080"]
    config.use_reloader = True
    return config


def cli() -> None:
    asyncio.run(main())


async def main():
    app = create_app()
    config = get_config()
    shutdown_trigger = asyncio.Event()

    await serve(
        app=cast(Framework, app), config=config, shutdown_trigger=shutdown_trigger.wait
    )


if __name__ == "__main__":
    asyncio.run(main())
