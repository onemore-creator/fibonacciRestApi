from fastapi import APIRouter

router = APIRouter(
    prefix="/fibonacci",
    tags=["fibonacci"]
)

@router.get("/count/{number}")
async def FibValueForNumber(number: int):
    pass

@router.get("/count/from1toN/{number}")
async def getFrom1toN(number: int):
    pass

@router.post("/blacklist/add/{number}")
async def addNumberToBlacklist(number: int):
    pass

@router.delete("/blacklist/delete/{number}")
async def deleteNumberFromBlacklist(number: int):
    pass
