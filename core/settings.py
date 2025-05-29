# config/settings.py

import os
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    "RPC_URL": os.getenv("RPC_URL"),
    "PRIVATE_KEY": os.getenv("PRIVATE_KEY"),
    "FLASHLOAN_CONTRACT": "0x123...abc",  # FlashLoan contract ของคุณ
    "GAS_LIMIT": 5_000_000,
    "GAS_MULTIPLIER": 1.1,
}

STRATEGY_LIST = [
    "arbitrage_eth_usdt",
    "sandwich_bot",
    "mev_liquidation",
    # เพิ่มกลยุทธ์อื่น ๆ ที่ต้องการรัน
]
