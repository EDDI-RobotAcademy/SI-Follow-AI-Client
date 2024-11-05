from abc import ABC, abstractmethod


class FinetuneService(ABC):
    @abstractmethod
    def supervised_finetuning(self):
        pass