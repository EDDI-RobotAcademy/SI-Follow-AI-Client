from abc import ABC, abstractmethod


class SIOperationService(ABC):
    @abstractmethod
    def operateSIAgent(self, *args, **kwargs):
        pass
