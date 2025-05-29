# scripts/run_all.py

from core.flashloan_engine import FlashloanEngine
from config.settings import CONFIG

if __name__ == "__main__":
    engine = FlashloanEngine(CONFIG)
    engine.run()
