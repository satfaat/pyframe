from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world() -> dict[str, str]:
    return {"message": "OK"}
