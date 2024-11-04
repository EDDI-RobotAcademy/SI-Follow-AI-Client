import os
import pickle
import sys

from made.chat_chain.service.chat_chain_service_impl import ChatChainServiceImpl
from made.phase import import_all_modules

from llama_agent_operation.repository.llama_agent_operation_repository import (
    LlamaAgentOperationRepository,
)

sys.path.append(
    os.path.join(os.path.dirname(__file__), "..", "..", "made_dev_example_for_llama")
)
import_all_modules("made_dev_example_for_llama.phases")

from made_dev_example_for_llama.states.env_states import EnvStates


class LlamaAgentOperationRepositoryImpl(LlamaAgentOperationRepository):
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
        ks = ["config", "model_name", "user_token", "task", "project", "base_url"]
        kwargs = {k: v for k, v in zip(ks, args)}
        chain = ChatChainServiceImpl(
            task_prompt=kwargs["task"],
            directory=os.path.join(
                "project_zoo", kwargs["user_token"], kwargs["project"]
            ),
            base_url=f"{kwargs['base_url']}/v1/",
            model=kwargs["model_name"],
            phases=[
                "DemandAnalysis",
                "ProductBacklogUpdate",
                "SprintCompletion",
                "CodeAndFormat",
                "CodeReview",
                "Test",
                "SprintReview",
                "NextSprintCompletion",
                "IncrementalCodeAndFormat",
                "CodeReview",
                "Test",
                "SprintReview",
                "EnvironmentDoc",
                "Manual",
            ],
            env_states=EnvStates(),
            save_chain=True,
            git_management=True,
        )
        chain.run()

    def get_file_list(self, *args, **kwargs):
        ks = ["user_token", "project_name"]
        kwargs = {k: v for k, v in zip(ks, args)}
        chain_checkpoint_path = os.path.join(
            "project_zoo", kwargs["user_token"], kwargs["project_name"], "chain.pkl"
        )
        with open(chain_checkpoint_path, "rb") as f:
            chain_dict = pickle.load(f)
        env = chain_dict["env"]
        file_names = env.states.codes.keys()
        return [
            os.path.join(
                "project_zoo", kwargs["user_token"], kwargs["project_name"], file_name
            )
            for file_name in file_names
        ]

    def get_file_content(self, *args, **kwargs):
        ks = ["user_token", "project_name", "file_name"]
        kwargs = {k: v for k, v in zip(ks, args)}
        chain_checkpoint_path = os.path.join(
            "project_zoo", kwargs["user_token"], kwargs["project_name"], "chain.pkl"
        )
        with open(chain_checkpoint_path, "rb") as f:
            chain_dict = pickle.load(f)
        env = chain_dict["env"]
        codes = env.states.codes
        file_name = kwargs["file_name"].split(kwargs["project_name"]).strip("/")
        content = codes[file_name]
        return content
