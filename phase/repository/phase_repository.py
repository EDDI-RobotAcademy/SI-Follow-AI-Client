from abc import ABC, abstractmethod


class PhaseRepository(ABC):
    @abstractmethod
    def get_current_phase(self, *args, **kwargs):
        pass
