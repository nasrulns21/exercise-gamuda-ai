from fastapi import APIRouter, FastAPI

left = APIRouter(prefix="/left-window", tags=["left"])
right = APIRouter(prefix="/right-window", tags=["right"])

@left.get("")
async def left_window(): return {"window": "left", "status": "open"}

@right.get("")
async def right_window(): return {"window": "right", "status": "open"}

app = FastAPI(title="Window Routers")
app.include_router(left)
app.include_router(right)
