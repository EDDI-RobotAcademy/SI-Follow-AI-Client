from abc import ABC, abstractmethod


class PhaseService(ABC):
    @abstractmethod
    def get_current_phase(self, *args, **kwargs):
        pass
