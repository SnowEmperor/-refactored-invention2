from fastapi import FastAPI


app = FastAPI()


@app.post("/items/{item_id}")
def dump_file(path_scan: str, file_name: str):
    from a322 import path_dump
    result = path_dump(path_scan, file_name)
    return result
