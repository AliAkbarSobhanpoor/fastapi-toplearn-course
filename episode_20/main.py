import random
from string import hexdigits
import uvicorn
from fastapi import FastAPI, Request
from fastapi_standalone_docs import StandaloneDocs
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static") # localhost:8000/static/main.css
templates = Jinja2Templates(directory="templates")
StandaloneDocs(app)


@app.get("/random-color", response_class=HTMLResponse)
def home(request: Request) -> str:
    hex_code = "".join(random.choices(hexdigits.lower(), k=6))
    hex_color = f"#{hex_code}"  # -> #a5beb9

    return templates.TemplateResponse(
        request=request,
        name="random_color.html",
        context={
            "color": hex_color,
        }
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)