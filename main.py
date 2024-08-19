from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get("/")
async def get():
    return HTMLResponse(content = "<html><body><h1>(:D)|￣|_</h1></body></html>")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(data)

