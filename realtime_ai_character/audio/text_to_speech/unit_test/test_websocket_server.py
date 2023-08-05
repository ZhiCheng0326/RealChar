import asyncio
import websockets

async def audio_server(websocket, path):
    while True:
        audio_chunk = await websocket.recv()
        if not audio_chunk:
            break
        print(f"Received audio chunk: {len(audio_chunk)} bytes")
        # You can process the audio_chunk as needed here

async def run_server():
    server = await websockets.serve(audio_server, "127.0.0.1", 8000)
    print("WebSocket server started.")
    await server.wait_closed()

# Only execute the server when the script is run directly, not when imported as a module
if __name__ == "__main__":
    asyncio.run(run_server())