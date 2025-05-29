# strategies/arbitrage_eth_usdt.py

from core.strategy_base import StrategyBase
from web3 import Web3

class Strategy(StrategyBase):
    def __init__(self, config):
        super().__init__(config)
        self.token0 = "ETH"
        self.token1 = "USDT"
        self.dex_a = "Uniswap"
        self.dex_b = "Sushiswap"

    def check_opportunity(self):
        # Mock: สมมติราคาในแต่ละ DEX (ในงานจริงต้องดึงจาก smart contract หรือ oracle)
        price_uniswap = 2000   # ETH/USDT
        price_sushiswap = 2025

        # หากต่างกัน > 1% ถือว่าเป็นโอกาส
        diff = abs(price_uniswap - price_sushiswap) / price_uniswap
        return diff >= 0.01

    def build_transaction(self):
        self.log("📦 Building flash loan TX (mock)...")
        # จำลอง structure ของ transaction
        tx = {
            "from": Web3.to_checksum_address("0xYourBotAddress"),
            "to": Web3.to_checksum_address(self.config["FLASHLOAN_CONTRACT"]),
            "gas": self.config["GAS_LIMIT"],
            "data": "0xFLASHLOANDATA",  # placeholder
        }
        return tx

    def execute(self, web3):
        self.log("🚀 Sending TX to blockchain...")

        signed_tx = web3.eth.account.sign_transaction(
            self.build_transaction(),
            private_key=self.config["PRIVATE_KEY"]
        )
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        self.log(f"📬 TX sent: {web3.to_hex(tx_hash)}")
