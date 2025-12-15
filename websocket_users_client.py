import asyncio

import websockets


async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"
        await websocket.send(message)

        for i in range(1, 6):
            message = await websocket.recv()
            print(f"{i} Сообщение пользователя: {message}")


asyncio.run(client())