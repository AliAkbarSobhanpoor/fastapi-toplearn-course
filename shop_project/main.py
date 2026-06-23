from urllib import request

import uvicorn
from fastapi import FastAPI, Request
from fastapi_standalone_docs import StandaloneDocs
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
StandaloneDocs(app)

@app.get("/")
async def shop(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="product-list.html",
        context={}
    )

@app.get("/product/{product_id}")
async def shop(request: Request, product_id: int):
    return templates.TemplateResponse(
        request=request,
        name="product-detail.html",
        context={}
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
