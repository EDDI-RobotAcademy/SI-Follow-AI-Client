import os
import pickle

from llama_phase.repository.llama_phase_repository import LlamaPhaseRepository


class LlamaPhaseRepositoryImpl(LlamaPhaseRepository):
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
        user_token, project_name = args
        chain_checkpoint_path = os.path.join(
            "project_zoo",
            user_token,
            project_name,
            "chain.pkl",
        )
        with open(chain_checkpoint_path, "rb") as f:
            chain_dict = pickle.load(f)
        cur_phase = chain_dict["phase"]
        return cur_phase

    def get_backlogs(self, *args, **kwargs):
        user_token, project_name = args
        chain_checkpoint_path = os.path.join(
            "project_zoo",
            user_token,
            project_name,
            "chain.pkl",
        )
        with open(chain_checkpoint_path, "rb") as f:
            chain_dict = pickle.load(f)
        env = chain_dict["env"]
        backlog = env.states.product_backlog
        acceptance_criteria = env.states.product_acceptance_criteria
        backlog = backlog + acceptance_criteria
        return "\n".join(backlog)

    def get_test_reports(self, *args, **kwargs):
        user_token, project_name = args
        chain_checkpoint_path = os.path.join(
            "project_zoo",
            user_token,
            project_name,
            "chain.pkl",
        )
        with open(chain_checkpoint_path, "rb") as f:
            chain_dict = pickle.load(f)
        env = chain_dict["env"]
        test_reports = env.states.test_reports

        return test_reports

    def get_code_reviews(self, *args, **kwargs):
        user_token, project_name = args
        chain_checkpoint_path = os.path.join(
            "project_zoo",
            user_token,
            project_name,
            "chain.pkl",
        )
        with open(chain_checkpoint_path, "rb") as f:
            chain_dict = pickle.load(f)
        env = chain_dict["env"]
        review_comments = env.states.review_comments

        return review_comments
