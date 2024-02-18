from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "This is the root"}

@app.get("/count")
async def FibValueForNumber():
    pass

@app.get("/count/from1toN")
async def getFrom1toN():
    pass

@app.post("/blacklist/add")
async def addNumberToBlacklist():
    pass

@app.delete("/blacklist/delete")
async def deleteNumberFromBlacklist():
    pass
