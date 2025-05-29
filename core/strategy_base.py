# core/strategy_base.py

from abc import ABC, abstractmethod

class StrategyBase(ABC):
    def __init__(self, config):
        self.config = config
        self.name = self.__class__.__name__

    @abstractmethod
    def check_opportunity(self):
        """เช็คว่ามีโอกาสทำกำไรมั้ย"""
        pass

    @abstractmethod
    def build_transaction(self):
        """สร้าง transaction ที่จะ execute flash loan"""
        pass

    @abstractmethod
    def execute(self, web3):
        """ส่ง TX จริงไปยัง blockchain"""
        pass

    def log(self, msg):
        print(f"[{self.name}] {msg}")
