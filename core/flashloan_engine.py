# core/flashloan_engine.py

import importlib
from config.settings import STRATEGY_LIST
from web3 import Web3

class FlashloanEngine:
    def __init__(self, config):
        self.config = config
        self.web3 = Web3(Web3.HTTPProvider(config["RPC_URL"]))
        self.strategies = []

        for strategy_name in STRATEGY_LIST:
            module_path = f"strategies.{strategy_name}"
            strategy_module = importlib.import_module(module_path)
            strategy_class = getattr(strategy_module, "Strategy")
            self.strategies.append(strategy_class(config))

    def run(self):
        for strategy in self.strategies:
            strategy.log("⏳ Checking opportunity...")
            try:
                if strategy.check_opportunity():
                    strategy.log("✅ Opportunity found! Executing trade.")
                    tx = strategy.build_transaction()
                    strategy.execute(self.web3)
                else:
                    strategy.log("❌ No opportunity at the moment.")
            except Exception as e:
                strategy.log(f"⚠️ Error: {e}")
