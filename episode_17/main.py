import uvicorn
import asyncio
from fastapi import FastAPI
from fastapi_standalone_docs import StandaloneDocs
from fastapi.responses import StreamingResponse, HTMLResponse
import aiofiles

"""

    response classes:
        - Response
        - JSONResponse
        - PlainTextResponse
        - HtmlResponse
        - RedirectResponse
        - FileResponse
        - StreamingResponse
        - ORJSONResponse
        - default_response_class
        
"""


app = FastAPI(default_response_class=HTMLResponse)
StandaloneDocs(app)

async def stream_text():
    for i in range(0, 5):
        message = f"Hello {i} \n"
        yield message.encode("utf-8") # byte
        await asyncio.sleep(1)


async def stream_video():
    async with aiofiles.open("../16_sobhanpoor.mp4", "rb") as f:
        while True:
            message = await f.read(1024 * 1024)

            if message is None:
                break

            yield message
            await asyncio.sleep(1)


@app.get("/stream_text")
async def stream_text():
    return StreamingResponse(stream_text(), media_type="text/plain")


@app.get("/stream_video")
async def stream_text():
    return StreamingResponse(stream_video(), media_type="video/mp4")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8002)