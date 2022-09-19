from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/spot/{id}")
def get_spot_id(spot_num: int, update_num: int):
    pass


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# All CRUD ops
@app.get("/forecast/{id}")
def get_forecast(id: int):
    pass


# All CRUD ops
@app.get("/request/{id}")
def get_request(id: int):
    pass


@app.post("/forecast/create")
def create_forecast() -> int:
    return 0


@app.post("/request/{id}/update")
def update_forecast(id: int, update, text, forecaster, corrected):
    pass


@app.get("/requests/unhandled")
def get_unhandled_requests():
    pass


@app.post("/request/{id}/mark/sent")
def mark_request_sent(id: int, update):
    pass


@app.delete("/request/{id}/delete")
def delete_request(id):
    pass
