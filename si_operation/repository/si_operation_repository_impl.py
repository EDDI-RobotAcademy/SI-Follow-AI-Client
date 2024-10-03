from si_operation.repository.si_operation_repository import SIOperationRepository


class SIOperationRepositoryImpl(SIOperationRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def operate(self, *args, **kwargs):
        # TODO: 이 부분에서 SI Agent 구동하도록 만들어주세요.
        # 작성된 형태 보고 상황에 맞게 리팩토링해두겠습니다.
        pass
