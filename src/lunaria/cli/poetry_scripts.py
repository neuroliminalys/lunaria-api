import uvicorn

def run_dev():
    uvicorn.run("lunaria.main:app", host="0.0.0.0", port=8000, reload=True)
