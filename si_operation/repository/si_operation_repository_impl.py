from si_operation.repository.si_operation_repository import SIOperationRepository

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'si_agent'))

from si_agent.runner import Runner


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
        ks = ['config', 'model_name', 'user_token', 'task', 'project', 'base_url']
        kwargs = {k:v for k, v in zip(ks, args)}
        runner = Runner()
        runner.run(**kwargs)

