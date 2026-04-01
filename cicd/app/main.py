import os

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()

APP_NAME = os.getenv("APP_NAME", "FastAPI Dummy Project")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Render the landing page."""
    return f"""
    <html>
        <head><title>{APP_NAME}</title></head>
        <body>
            <h1>Welcome to {APP_NAME}</h1>
            <p>Routes available: /health, /items/{{id}}, /calculate</p>
        </body>
    </html>
    """


@app.get("/health")
async def health_check():
    """Return application health status."""
    return {"status": "ok", "app_name": APP_NAME}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    """Retrieve an item by ID with an optional query string."""
    if item_id < 0:
        raise HTTPException(status_code=400, detail="Item ID must be positive")

    item_data = {"item_id": item_id}
    if q:
        item_data.update({"query": q, "description": f"You searched for {q}"})
    else:
        item_data.update({"description": "No query provided"})

    return item_data


@app.get("/calculate")
async def calculate(op: str, x: float, y: float):
    """Perform a simple mathematical operation."""
    if op == "add":
        result = x + y
    elif op == "sub":
        result = x - y
    elif op == "mul":
        result = x * y
    elif op == "div":
        if y == 0:
            raise HTTPException(status_code=400, detail="Division by zero")
        result = x / y
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

    return {"operation": op, "x": x, "y": y, "result": result}
