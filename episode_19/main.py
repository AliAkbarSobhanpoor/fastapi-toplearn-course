import random
from string import hexdigits
import uvicorn
from fastapi import FastAPI
from fastapi_standalone_docs import StandaloneDocs
from starlette.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
from jinja2 import Template

app = FastAPI()
StandaloneDocs(app)

courses = [
    {
        "name": "Introduction to Python Programming",
        "teacher": "Dr. Emily Chen",
        "tags": ["programming", "python", "beginner", "coding"]
    },
    {
        "name": "Web Development with React",
        "teacher": "Prof. James Rodriguez",
        "tags": ["web", "react", "frontend", "javascript"]
    },
    {
        "name": "Data Science and Machine Learning",
        "teacher": "Dr. Sarah Khan",
        "tags": ["data science", "machine learning", "python", "analytics"]
    },
    {
        "name": "Digital Marketing Fundamentals",
        "teacher": "Prof. Linda Martinez",
        "tags": ["marketing", "seo", "social media", "business"]
    },
    {
        "name": "Graphic Design with Adobe Suite",
        "teacher": "Michael Thompson",
        "tags": ["design", "photoshop", "illustrator", "creative"]
    }
]


@app.get("/random-color", response_class=HTMLResponse)
def home() -> str:
    hex_code = "".join(random.choices(hexdigits.lower(), k=6))
    hex_color = f"#{hex_code}" # -> #a5beb9

    #language=html
    html_template = """
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Random Color Generator</title>
                <style>
                    body {
                        height: 100vh;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        background-color: {{ color }};
                        color: white;
                        font-size: 120px;
                        font-family: monospace;
                    }
                </style>
            </head>
            <body>
                <div id="color-code">{{ color }}</div>
            </body>
        </html>
    """

    template = Template(html_template)

    # template value
    return template.render({
        "color": hex_color,
    })

@app.get("/courses", response_class=HTMLResponse)
def home() -> str:
    hex_code = "".join(random.choices(hexdigits.lower(), k=6))
    hex_color = f"#{hex_code}" # -> #a5beb9

    #language=html
    html_template = """
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Courses list</title>
                
            </head>
            <body>
                <table border='1'>
                    <thead>
                        <td>name</td>
                        <td>teacher</td>
                        <td>tags</td>
                    </thead>
                    {% for course in courses %}
                        {% if course.name == "Introduction to Python Programming" %}
                            <tr>
                                <td>{{ course.name }}</td>
                                <td>{{ course.teacher }}</td>
                                <td>{{ course.tags }}</td>
                            </tr>
                        {% endif %}
                    {% endfor %}
                </table>
            </body>
        </html>
    """

    template = Template(html_template)
    # template tag
    # template value
    return template.render({
        "courses": courses,
    })


@app.get("/random-color-text", response_class=PlainTextResponse)
def home() -> str:
    hex_code = "".join(random.choices(hexdigits.lower(), k=6))
    hex_color = f"#{hex_code}"  # -> #a5beb9

    html_template = "hexa code is: {{ color }}"

    template = Template(html_template)
    # template tag
    # template value
    return template.render({
        "color": hex_color,
    })


if __name__ == "__main__":
    uvicorn.run("main:app" , host="0.0.0.0", port=8000, reload=True)