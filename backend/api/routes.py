from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class StrategyStatus(BaseModel):
    name: str
    status: str  # running | idle | error
    last_profit: float
    last_tx: str

@router.get("/strategies", response_model=List[StrategyStatus])
def get_strategies():
    # จำลองข้อมูล (จริง ๆ จะอ่านจาก DB, Redis, หรือไฟล์ JSON)
    strategies = [
        {"name": "Arbitrage ETH/USDT", "status": "running", "last_profit": 1.2, "last_tx": "0xabc..."},
        {"name": "Sandwich Hunter", "status": "idle", "last_profit": 0.4, "last_tx": "0xdef..."},
        {"name": "Liquidation Hunter", "status": "running", "last_profit": 3.1, "last_tx": "0x123..."},
        # ... ครบ 11 ตัว
    ]
    return strategies
