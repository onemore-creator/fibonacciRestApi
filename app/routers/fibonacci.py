from fastapi import APIRouter, HTTPException, Depends, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import Page, paginate

from app.worker.tasks import computeFibonacciTask, computeFibonacciTaskReturnSequence

from app.utils.redis_wrapper import redisWrapper
import logging

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
async def getFrom1toN(number: int, cache = Depends(redisWrapper.getRedisInstance)):
    try:
        result = list(computeFibonacciTaskReturnSequence.delay(number).get())
        blacklist = await cache.execute_command("smembers", "numbers:blacklist")
        blacklist = list(map(lambda x : str(int(x)), blacklist))
        return paginate([x for x in result if x not in blacklist])
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid input. Please provide a valid integer")
    except Exception as e:
        raise HTTPException(status_code=400, detail="Unexpected error")


@router.post("/blacklist/add/{number}", status_code=200)
async def addNumberToBlacklist(number: int, response: Response, cache = Depends(redisWrapper.getRedisInstance)):
    result = await cache.execute_command("sadd", "numbers:blacklist", number)
    if not result:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    blacklist = await cache.execute_command("smembers", "numbers:blacklist")
    return result

@router.delete("/blacklist/delete/{number}", status_code=200)
async def deleteNumberFromBlacklist(number: int, response: Response, cache = Depends(redisWrapper.getRedisInstance)):
    result = await cache.execute_command("srem", "numbers:blacklist", number)
    if not result:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return result
