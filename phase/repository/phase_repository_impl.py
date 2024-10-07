from phase.repository.phase_repository import PhaseRepository


class PhaseRepositoryImpl(PhaseRepository):
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

    def get_current_phase(self, *args, **kwargs):
        user_token = args[0]
        print('#'*30)
        print('current phase: ', 'testtesttest')
        print('user token: ', user_token)
        print('#'*30)
        return 'testtesttest'
