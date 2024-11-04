from abc import ABC, abstractmethod


class LlamaAgentOperationService(ABC):
    @abstractmethod
    def operateSIAgent(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def get_file_list(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def get_file_content(self, *args, **kwargs):
        pass
