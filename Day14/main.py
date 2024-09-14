from fastapi import FastAPI

# Create an instance of the FastAPI app
app = FastAPI()

@app.get("/")
def root ():
    return {"message": "Hello World!"}