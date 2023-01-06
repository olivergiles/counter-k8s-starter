from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    try:
        with open("/app/pv-data/count.txt", "r+") as f:
            data = f.read()
            x = int(data) + 1
            f.seek(0)
            f.write(str(x))
            f.truncate()
    except FileNotFoundError:
        with open("/app/pv-data/count.txt", "w") as f:
            x = 1
            f.write(str(x))
    return {"Read": f"{x} times"}
