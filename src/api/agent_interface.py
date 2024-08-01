import asyncio
from aiohttp import web

async def handle_request(request):
    data = await request.json()
    result = await process_data_async(data)
    return web.json_response(result)

async def process_data_async(data):
    await asyncio.sleep(1)  # Simulating I/O-bound operation
    return {"processed_data": data * 2}

app = web.Application()
app.router.add_post('/process', handle_request)

if __name__ == '__main__':
    web.run_app(app)

print("Asynchronous API interface activated.")
