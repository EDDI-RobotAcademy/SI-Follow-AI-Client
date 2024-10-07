from si_operation.repository.si_operation_repository_impl import SIOperationRepositoryImpl
from si_operation.service.si_operation_service import SIOperationService


class SIOperationServiceImpl(SIOperationService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__siOperationRepository = SIOperationRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def operateSIAgent(self, *args, **kwargs):
        self.__siOperationRepository.operate(*args, **kwargs)
        return {
            "status": "done"
        }
