import uuid
from typing import Annotated
import uvicorn
from fastapi import FastAPI, Request, Form, Cookie
from fastapi import status
from fastapi_standalone_docs import StandaloneDocs
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.staticfiles import StaticFiles

products = [
    {
        "id": 1,
        "name": "Dell XPS 16 (2026)",
        "price": 113940000,
        "description": "اولترابوک ممتاز با صفحه‌نمایش خیره‌کننده ۴K OLED، حاشیه‌های باریک و بدنه آلومینیومی باکیفیت. ایده‌آل برای تولیدکنندگان محتوا و حرفه‌ای‌ها.",
        "processor": "Intel Core Ultra 9 285H",
        "ram": "32 GB LPDDR5x",
        "storage": "1 TB NVMe SSD",
        "display": "16.3-inch 4K (3840x2400) OLED, 120Hz, touch",
        "battery": "99 Wh, up to 12 hours"
    },
    {
        "id": 2,
        "name": "Apple MacBook Air 15\" M4",
        "price": 83940000,
        "description": "لپ‌تاپ نازک و سبک بدون فن با تراشه M4 اپل، عمر باتری فوق‌العاده و صفحه‌نمایش زنده Liquid Retina. گزینه‌ای عالی برای بهره‌وری روزمره.",
        "processor": "Apple M4 (8-core CPU, 10-core GPU)",
        "ram": "16 GB unified memory",
        "storage": "512 GB SSD",
        "display": "15.3-inch Liquid Retina (2880x1864), 500 nits",
        "battery": "66.5 Wh, up to 18 hours"
    },
    {
        "id": 3,
        "name": "Lenovo ThinkPad X1 Carbon Gen 13",
        "price": 128940000,
        "description": "اولتراپورتال کلاس بیزینسی با صفحه‌کلید افسانه‌ای، ویژگی‌های امنیتی قدرتمند و شاسی فیبرکربنی بادوام. ساخته شده برای مسافران حرفه‌ای.",
        "processor": "Intel Core Ultra 7 265H vPro",
        "ram": "32 GB LPDDR5x",
        "storage": "1 TB NVMe SSD",
        "display": "14-inch WQXGA (2560x1600) IPS, 400 nits, low power",
        "battery": "57 Wh, up to 15 hours"
    },
    {
        "id": 4,
        "name": "Asus ROG Zephyrus G16 (2026)",
        "price": 149940000,
        "description": "لپ‌تاپ باریک گیمینگ با گرافیک NVIDIA GeForce RTX 5090، صفحه‌نمایش mini-LED با نرخ تازه‌سازی بالا و مدیریت حرارت عالی برای بازی‌های سنگین و کارهای خلاقانه.",
        "processor": "AMD Ryzen AI 9 HX 370",
        "ram": "32 GB LPDDR5x",
        "storage": "2 TB NVMe SSD",
        "display": "16-inch QHD+ (2560x1600) mini-LED, 240Hz, HDR1000",
        "battery": "90 Wh, up to 8 hours (mixed use)"
    },
    {
        "id": 5,
        "name": "HP Spectre x360 16 (2026)",
        "price": 98940000,
        "description": "لپ‌تاپ ۲ در ۱ همه‌کاره با صفحه‌نمایش OLED لمسی زنده، قلم تعبیه‌شده و طراحی براق جواهری. گزینه‌ای عالی برای هنرمندان و دانشجویان.",
        "processor": "Intel Core Ultra 7 265H",
        "ram": "16 GB LPDDR5x",
        "storage": "1 TB NVMe SSD",
        "display": "16-inch 4K (3840x2160) OLED, 120Hz, touch, anti‑reflection",
        "battery": "83 Wh, up to 14 hours"
    },
    {
        "id": 6,
        "name": "Acer Swift Go 14 (2026)",
        "price": 53940000,
        "description": "اولتراپورتال مقرون‌به‌صرفه اما قدرتمند با صفحه‌نمایش OLED شارپ، طراحی سبک و عملکرد عالی برای دانشجویان و کارهای اداری.",
        "processor": "Intel Core Ultra 5 225H",
        "ram": "16 GB LPDDR5x",
        "storage": "512 GB NVMe SSD",
        "display": "14-inch 2.8K (2880x1800) OLED, 90Hz",
        "battery": "65 Wh, up to 13 hours"
    },
    {
        "id": 7,
        "name": "Microsoft Surface Laptop 7 (13.8\")",
        "price": 77940000,
        "description": "لپ‌تاپ جمع‌وجور فوق‌ممتاز با صفحه‌نمایش PixelSense زنده، عمر باتری تمام‌روز و روکش آلکانتارا یا فلزی لوکس. عالی برای حرفه‌ای‌های در حال حرکت.",
        "processor": "Intel Core Ultra 7 265H",
        "ram": "16 GB LPDDR5x",
        "storage": "512 GB NVMe SSD",
        "display": "13.8-inch PixelSense (2304x1536), 120Hz, touch, Dolby Vision IQ",
        "battery": "54 Wh, up to 16 hours"
    },
    {
        "id": 8,
        "name": "Lenovo Legion 7i Pro (2026)",
        "price": 191940000,
        "description": "جایگزین قدرتمند دسکتاپ با صفحه‌نمایش ۱۶ اینچی mini-LED، گرافیک برتر NVIDIA RTX 5090 و خنک‌سازی فلز مایع پیشرفته برای بازی ۴K و رندرینگ سه‌بعدی.",
        "processor": "Intel Core i9-15900HX",
        "ram": "64 GB DDR5-5600",
        "storage": "2 TB NVMe SSD (RAID 0)",
        "display": "16-inch 4K (3840x2160) mini-LED, 160Hz, HDR, G-SYNC",
        "battery": "99.9 Wh, up to 6 hours (light use)"
    },
    {
        "id": 9,
        "name": "Framework Laptop 13 (AMD)",
        "price": 65940000,
        "description": "لپ‌تاپ فوق‌قابل تعمیر و ماژولار ۱۳ اینچی با پورت‌های قابل تعویض و مادربردهای قابل ارتقا. انتخابی پایدار برای علاقه‌مندان به تعمیر و کاربران دغدغه‌مند به حریم خصوصی.",
        "processor": "AMD Ryzen 7 7840U",
        "ram": "32 GB DDR5-5600 (user-upgradeable)",
        "storage": "1 TB NVMe SSD (user-upgradeable)",
        "display": "13.5-inch 2.8K (2256x1504) IPS, 120Hz, 3:2 aspect ratio",
        "battery": "61 Wh, up to 11 hours"
    },
    {
        "id": 10,
        "name": "Acer Aspire 5 (2026)",
        "price": 35940000,
        "description": "لپ‌تاپ همه‌کاره اقتصادی با صفحه‌نمایش FHD شفاف، عملکرد کافی برای کارهای روزمره و صفحه‌کلید عددی. گزینه‌ای عالی برای استفاده خانگی، دانشجویان و کارهای سبک اداری.",
        "processor": "Intel Core i5-13500H",
        "ram": "8 GB DDR4",
        "storage": "512 GB NVMe SSD",
        "display": "15.6-inch FHD (1920x1080) IPS, 60Hz, anti-glare",
        "battery": "50 Wh, up to 9 hours"
    }
]

carts: dict[str, dict[int, int]] = {}  # -> {unique_cart_id: {1:2, 2:3}}

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
StandaloneDocs(app)


def get_cart_items_count(cart_id: str) -> int:
    if cart_id and cart_id in carts:
        return len(carts[cart_id])
    return 0


@app.get("/", response_class=HTMLResponse, name="products")
async def shop(request: Request, cart_id: Annotated[str | None, Cookie()] = None):
    return templates.TemplateResponse(
        request=request,
        name="product-list.html",
        context={
            "products": products,
            "cart_item_count": get_cart_items_count(cart_id),
        }
    )


@app.get("/product/{product_id}", response_class=HTMLResponse, name="product_detail")
async def product_detail(request: Request, product_id: int, cart_id: Annotated[str | None, Cookie()] = None):
    for product in products:
        if product["id"] == product_id:
            return templates.TemplateResponse(
                request=request,
                name="product-detail.html",
                context={
                    "product": product,
                    "cart_item_count": get_cart_items_count(cart_id),
                }
            )

    return templates.TemplateResponse(
        request=request,
        name="404.html",
        status_code=404
    )


class CartItemsForm(BaseModel):
    quantity: Annotated[int, Field(gt=0)]
    product_id: Annotated[int, Field(gt=0)]


@app.post("/add_to_cart", response_class=RedirectResponse, name="add_to_cart", status_code=status.HTTP_302_FOUND)
async def add_to_cart(
        form_data: Annotated[CartItemsForm, Form()],
        cart_id: Annotated[str | None, Cookie()] = None
):
    if cart_id:
        cart = carts.get(cart_id)
        if cart:
            cart[form_data.product_id] = form_data.quantity
        else:
            carts[cart_id] = {
                form_data.product_id: form_data.quantity
            }
    else:
        cart = {
            form_data.product_id: form_data.quantity
        }
        cart_id = str(uuid.uuid4())
        carts[cart_id] = cart

    response = RedirectResponse(f"/product/{form_data.product_id}", status_code=status.HTTP_302_FOUND)
    response.set_cookie(
        key="cart_id",
        value=cart_id,
        max_age=30 * 24 * 60 * 60,
    )
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001)
