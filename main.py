from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Hello from FastAPI!'}

def add(a, b):
    return a + b
