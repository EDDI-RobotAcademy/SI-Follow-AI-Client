import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'custom_model'))

from finetune.service.finetune_service import FinetuneService
from custom_model.train.service.train_service_impl import TrainServiceImpl
from custom_model.to_ollama.service.to_ollama_service_impl import ToOllamaServiceImpl


class FinetuneServiceImpl(FinetuneService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__train_service = TrainServiceImpl.get_instance()
            cls.__instance.__to_ollama_service = ToOllamaServiceImpl.get_instance()

        return cls.__instance

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance
    
    def supervised_finetuning(self, *args, **kwargs):
        user_token, model_name, model_id, dataset_id = args[:4]
        save_path = os.path.join("model_zoo", user_token, model_name)
        self.__train_service.sft(save_path=save_path, model_id=model_id, dataset_id=dataset_id)
        model_id = model_id if model_id else self.__train_service.MODEL_ID
        self.__to_ollama_service.to_ollama(model_id, save_path, save_path)
        return {
            "finetune": "started"
        }
