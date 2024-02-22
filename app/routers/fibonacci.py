from fastapi import APIRouter, HTTPException, Depends, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import Page, paginate

from app.worker.tasks import computeFibonacciTask, computeFibonacciTaskReturnSequence

from app.utils.redis_wrapper import redisWrapper
from app.models.blacklist_response_model import BlacklistResponse
from app.models.fibonacci_response_model import FibonacciResponse

import logging

router = APIRouter(
    prefix="/fibonacci",
    tags=["fibonacci"]
)

@router.get("/count/{number}", status_code=200)
async def FibValueForNumber(number: int) -> FibonacciResponse:
    try:
        result = computeFibonacciTask.delay(number)
        return FibonacciResponse(number=str(result.get()))
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid input. Please provide a valid integer")
    except Exception as e:
        raise HTTPException(status_code=400, detail="Unexpected error")

@router.get("/count/from1toN/{number}", status_code=200)
async def getFrom1toN(number: int, cache = Depends(redisWrapper.getRedisInstance)) -> Page[FibonacciResponse]:
    try:
        result = list(computeFibonacciTaskReturnSequence.delay(number).get())
        blacklist = await cache.execute_command("smembers", "numbers:blacklist")
        blacklist = list(map(lambda x : str(int(x)), blacklist))
        return paginate([FibonacciResponse(number=x) for x in result if x not in blacklist])
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid input. Please provide a valid integer")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/blacklist/add/{number}", status_code=201)
async def addNumberToBlacklist(number: int, response: Response, cache = Depends(redisWrapper.getRedisInstance)):
    cmdExecutionResult = await cache.execute_command("sadd", "numbers:blacklist", number)
    if not cmdExecutionResult:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return cmdExecutionResult

@router.delete("/blacklist/delete/{number}", status_code=204)
async def deleteNumberFromBlacklist(number: int, response: Response, cache = Depends(redisWrapper.getRedisInstance)):
    cmdExecutionResult = await cache.execute_command("srem", "numbers:blacklist", number)
    if not cmdExecutionResult:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return cmdExecutionResult

@router.delete("/blacklist/delete", status_code=204)
async def flushBlacklist(response: Response, cache = Depends(redisWrapper.getRedisInstance)):
    cmdExecutionResult = await cache.execute_command("del", "numbers:blacklist")
    if not cmdExecutionResult:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return cmdExecutionResult

@router.get("/blacklist/get", status_code=200)
async def getBlacklist(response: Response, cache = Depends(redisWrapper.getRedisInstance)) -> BlacklistResponse:
    blacklist = await cache.execute_command("smembers", "numbers:blacklist")
    blacklist = list(map(lambda x : str(int(x)), blacklist))
    if not blacklist:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return BlacklistResponse(numbers=blacklist)
