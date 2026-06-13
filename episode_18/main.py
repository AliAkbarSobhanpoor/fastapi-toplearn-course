import uvicorn
from fastapi import FastAPI, Cookie
from fastapi_standalone_docs import StandaloneDocs
from fastapi.responses import HTMLResponse, Response
from typing import Annotated

app = FastAPI(default_response_class=HTMLResponse)
StandaloneDocs(app)

"""
    
    headers:
        usages
        
    cookies:

"""

@app.get("/")
async def root() -> HTMLResponse:
    return HTMLResponse("Hello World", headers={
        "X-Name": "AliAkbar"
    })

@app.get("/root_2")
async def root_2(
        response: Response,
        cart_items: Annotated[str | None, Cookie(alias="cart-items")] = None
):
    print(cart_items)
    response.headers["X-Name"] = "AliAkbar"
    response.headers["X-Family-Name"] = "Sobhanpoor"
    response.set_cookie("cart-items", "1,2,3", max_age=10)
    return "Hello World"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)