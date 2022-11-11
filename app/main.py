from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"data": "Hello World"}

@app.get("/item/{id}")
def read(id: int):
    return {"data": id}


if __name__ == '__main__':
    uvicorn.run(app)
