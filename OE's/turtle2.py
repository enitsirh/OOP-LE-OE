#OOP LA26
from abc import ABC, abstractmethod

class NinjaTurtle(ABC):
    @property
    @abstractmethod
    def alias(self):
        pass

class Leonardo(NinjaTurtle):
    def __init__(self):
        self._alias = "leo"
    
    @property
    def alias(self):
        return self._alias


class Michelangelo(NinjaTurtle):
    def __init__(self):
        self._alias = "mikey"
    
    @property
    def alias(self):
        return self._alias


class Donatello(NinjaTurtle):
    def __init__(self):
        self._alias = "don"
    
    @property
    def alias(self):
        return self._alias


class Raphael(NinjaTurtle):
    def __init__(self):
        self._alias = "raph"
    
    @property
    def alias(self):
        return self._alias

if __name__ == "__main__":
    pong = Leonardo()
    print(pong.alias)
    print("TESTING ONLY")
