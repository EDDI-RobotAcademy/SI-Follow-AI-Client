from llama_agent_operation.repository.llama_agent_operation_repository_impl import (
    LlamaAgentOperationRepositoryImpl,
)
from llama_agent_operation.service.llama_agent_operation_service import LlamaAgentOperationService


class LlamaAgentOperationServiceImpl(LlamaAgentOperationService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__llamaAgentOperationRepository = (
                LlamaAgentOperationRepositoryImpl.getInstance()
            )

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def operateSIAgent(self, *args, **kwargs):
        self.__llamaAgentOperationRepository.operate(*args, **kwargs)
        return {"status": "done"}

    def get_file_list(self, *args, **kwargs):
        user_token = args[0]
        project_name = args[1]
        created_files = self.__llamaAgentOperationRepository.get_file_list(
            *args, **kwargs
        )
        return {
            "user_token": user_token,
            "project_name": project_name,
            "file_list": created_files,
        }

    def get_file_content(self, *args, **kwargs):
        user_token = args[0]
        project_name = args[1]
        file_name = args[2]
        file_content = self.__llamaAgentOperationRepository.get_file_content(
            *args, **kwargs
        )
        return {
            "user_token": user_token,
            "project_name": project_name,
            "file_name": file_name,
            "file_content": file_content,
        }
