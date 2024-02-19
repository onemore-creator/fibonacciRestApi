from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from app.worker.tasks import compute_fibonacci_task 

router = APIRouter(
    prefix="/fibonacci",
    tags=["fibonacci"]
)

@router.get("/count/{number}")
async def FibValueForNumber(number: int):
    try:
        result = compute_fibonacci_task.delay(number)
        return jsonable_encoder({'input': number, 'task_id': result.id}), 202
    except ValueError:
        return jsonable_encoder({'error': 'Invalid input. Please provide a valid integer.'}), 400


@router.get("/count/from1toN/{number}")
async def getFrom1toN(number: int):
    pass

@router.post("/blacklist/add/{number}")
async def addNumberToBlacklist(number: int):
    pass

@router.delete("/blacklist/delete/{number}")
async def deleteNumberFromBlacklist(number: int):
    pass
