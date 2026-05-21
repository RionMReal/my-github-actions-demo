from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Hello from FastAPI v2!'}

def add(a, b):
    return a + b
