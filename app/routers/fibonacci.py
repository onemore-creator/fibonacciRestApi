from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import Page, paginate

from app.worker.tasks import computeFibonacciTask, computeFibonacciTaskReturnSequence

from app.config import Config

import aioredis

router = APIRouter(
    prefix="/fibonacci",
    tags=["fibonacci"]
)

@router.get("/count/{number}")
async def FibValueForNumber(number: int):
    try:
        result = computeFibonacciTask.delay(number)
        return jsonable_encoder({'result': result.get()}), 200
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid input. Please provide a valid integer")
    except Exception as e:
        raise HTTPException(status_code=400, detail="Unexpected error")

@router.get("/count/from1toN/{number}", response_model=Page[str])
async def getFrom1toN(number: int):
    try:
        result = computeFibonacciTaskReturnSequence.delay(number)
        return paginate(result.get())
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid input. Please provide a valid integer")
    except Exception as e:
        raise HTTPException(status_code=400, detail="Unexpected error")


@router.post("/blacklist/add/{number}")
async def addNumberToBlacklist(number: int):
    pass

@router.delete("/blacklist/delete/{number}")
async def deleteNumberFromBlacklist(number: int):
    pass
