from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def health_check():
    return "The health check is successfull"


@app.get("/home")
async def home_check():
    return "This is home sweet home brother"