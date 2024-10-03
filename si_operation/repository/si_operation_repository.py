from abc import ABC, abstractmethod


class SIOperationRepository(ABC):
    @abstractmethod
    def operate(self, *args, **kwargs):
        pass
