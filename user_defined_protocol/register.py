import os
import sys

from first_user_defined_function_domain.service.fudf_service_impl import FudfServiceImpl
from first_user_defined_function_domain.service.request.fudf_just_for_test_request import (
    FudfJustForTestRequest,
)
from first_user_defined_function_domain.service.response.fudf_just_for_test_response import (
    FudfJustForTestResponse,
)
from finetune.service.finetune_service_impl import FinetuneServiceImpl
from finetune.service.request.finetune_request import FineTuneRequest
from finetune.service.response.finetune_response import FineTuneResponse
from gpu_management.service.gpu_management_service_impl import GPUManagementServiceImpl
from gpu_management.service.request.gpu_management_request import GPUManagementRequest
from gpu_management.service.response.gpu_management_response import (
    GPUManagementResponse,
)
from llama_agent_operation.service.llama_agent_operation_service_impl import (
    LlamaAgentOperationServiceImpl,
)
from llama_agent_operation.service.request.get_file_content_request import (
    LLamaGetFileContentRequest,
)
from llama_agent_operation.service.request.get_file_list_request import (
    LlamaGetFileListRequest,
)
from llama_agent_operation.service.request.llama_agent_operation_request import (
    LlamaAgentOperationRequest,
)
from llama_agent_operation.service.response.get_file_content_response import (
    LlamaGetFileContentResponse,
)
from llama_agent_operation.service.response.get_file_list_response import (
    LlamaGetFileListResponse,
)
from llama_agent_operation.service.response.llama_agent_operation_response import (
    LlamaAgentOperationResponse,
)
from llama_phase.service.llama_phase_service_impl import LlamaPhaseServiceImpl
from llama_phase.service.request.get_backlogs_service_request import (
    LlamaGetBacklogsRequest,
)
from llama_phase.service.request.get_code_review_service_request import (
    LlamaGetCodeReviewsRequest,
)
from llama_phase.service.request.get_current_phase_service_request import (
    LlamaGetCurrentPhaseRequest,
)
from llama_phase.service.request.get_test_reports_service_request import (
    LlamaGetTestReportsRequest,
)
from llama_phase.service.response.get_backlogs_service_response import (
    LlamaGetBacklogsResponse,
)
from llama_phase.service.response.get_code_review_service_response import (
    LlamaGetCodeReviewsResponse,
)
from llama_phase.service.response.get_current_phase_service_response import (
    LlamaGetCurrentPhaseResponse,
)
from llama_phase.service.response.get_test_reports_service_response import (
    LlamaGetTestReportsResponse,
)
from multiple_user_test_point.service.multiple_user_test_point_service_impl import (
    MultipleUserTestPointServiceImpl,
)
from multiple_user_test_point.service.request.user_test_point_request import (
    UserTestPointRequest,
)
from multiple_user_test_point.service.response.user_test_point_response import (
    UserTestPointResponse,
)
from phase.service.phase_service_impl import PhaseServiceImpl
from phase.service.request.get_backlogs_service_request import GetBacklogsRequest
from phase.service.request.get_code_review_service_request import GetCodeReviewsRequest
from phase.service.request.get_current_phase_service_request import (
    GetCurrentPhaseRequest,
)
from phase.service.request.get_test_reports_service_request import GetTestReportsRequest
from phase.service.response.get_backlogs_service_response import GetBacklogsResponse
from phase.service.response.get_code_review_service_response import (
    GetCodeReviewsResponse,
)
from phase.service.response.get_current_phase_service_response import (
    GetCurrentPhaseResponse,
)
from phase.service.response.get_test_reports_service_response import (
    GetTestReportsResponse,
)
from si_operation.service.request.get_file_content_request import GetFileContentRequest
from si_operation.service.request.get_file_list_request import GetFileListRequest
from si_operation.service.request.si_operation_request import SIOperationRequest
from si_operation.service.response.get_file_content_response import (
    GetFileContentResponse,
)
from si_operation.service.response.get_file_list_response import GetFileListResponse
from si_operation.service.response.si_operation_response import SIOperationResponse
from si_operation.service.si_operation_service_impl import SIOperationServiceImpl
from watchdog_operation.service.request.watchdog_service_request import (
    WatchdogOperationRequest,
)
from watchdog_operation.service.response.watchdog_service_response import (
    WatchdogOperationResponse,
)
from watchdog_operation.service.watchdog_operation_service_impl import (
    WatchdogOperationServiceImpl,
)

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "template"))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "si_agent"))
sys.path.append(
    os.path.join(os.path.dirname(__file__), "..", "made_dev_example_for_llama")
)

from template.custom_protocol.service.custom_protocol_service_impl import (
    CustomProtocolServiceImpl,
)
from template.request_generator.request_class_map import RequestClassMap
from template.response_generator.response_class_map import ResponseClassMap
from user_defined_protocol.protocol import UserDefinedProtocolNumber


class UserDefinedProtocolRegister:
    @staticmethod
    def registerUserTestPointProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        multipleUserTestPointService = MultipleUserTestPointServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.USER_TEST_POINT, UserTestPointRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.USER_TEST_POINT, UserTestPointResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.USER_TEST_POINT,
            multipleUserTestPointService.operateUserTestPoint,
        )

    @staticmethod
    def registerFirstUserDefinedProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        firstUserDefinedFunctionService = FudfServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.FIRST_USER_DEFINED_FUNCTION_FOR_TEST,
            FudfJustForTestRequest,
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.FIRST_USER_DEFINED_FUNCTION_FOR_TEST,
            FudfJustForTestResponse,
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.FIRST_USER_DEFINED_FUNCTION_FOR_TEST,
            firstUserDefinedFunctionService.justForTest,
        )

    # @staticmethod
    # def registerSIAgentOperationProtocol():
    #     customProtocolService = CustomProtocolServiceImpl.getInstance()
    #     siAgentOperationService = SIOperationServiceImpl.getInstance()

    #     requestClassMapInstance = RequestClassMap.getInstance()
    #     requestClassMapInstance.addRequestClass(
    #         UserDefinedProtocolNumber.SI_AGENT_OPERATION, SIOperationRequest
    #     )

    #     responseClassMapInstance = ResponseClassMap.getInstance()
    #     responseClassMapInstance.addResponseClass(
    #         UserDefinedProtocolNumber.SI_AGENT_OPERATION, SIOperationResponse
    #     )

    #     customProtocolService.registerCustomProtocol(
    #         UserDefinedProtocolNumber.SI_AGENT_OPERATION,
    #         siAgentOperationService.operateSIAgent,
    #     )

    @staticmethod
    def registerLlamaAgentOperationProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        llamaAgentOperationService = LlamaAgentOperationServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.LLaMA_AGENT_OPERATION, LlamaAgentOperationRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.LLaMA_AGENT_OPERATION, LlamaAgentOperationResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.LLaMA_AGENT_OPERATION,
            llamaAgentOperationService.operateSIAgent,
        )

    @staticmethod
    def registerWatchdogOperationProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        watchdogOperationService = WatchdogOperationServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.WATCHDOG_OPERATON, WatchdogOperationRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.WATCHDOG_OPERATON, WatchdogOperationResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.WATCHDOG_OPERATON,
            watchdogOperationService.operateWatchdog,
        )

    # @staticmethod
    # def registerGetCurrentPhaseProtocol():
    #     customProtocolService = CustomProtocolServiceImpl.getInstance()
    #     phaseService = PhaseServiceImpl.getInstance()

    #     requestClassMapInstance = RequestClassMap.getInstance()
    #     requestClassMapInstance.addRequestClass(
    #         UserDefinedProtocolNumber.GET_CURRENT_PHASE, GetCurrentPhaseRequest
    #     )

    #     responseClassMapInstance = ResponseClassMap.getInstance()
    #     responseClassMapInstance.addResponseClass(
    #         UserDefinedProtocolNumber.GET_CURRENT_PHASE, GetCurrentPhaseResponse
    #     )

    #     customProtocolService.registerCustomProtocol(
    #         UserDefinedProtocolNumber.GET_CURRENT_PHASE, phaseService.get_current_phase
    #     )

    @staticmethod
    def registerLlamaGetCurrentPhaseProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        phaseService = LlamaPhaseServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.LLaMA_GET_CURRENT_PHASE,
            LlamaGetCurrentPhaseRequest,
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.LLaMA_GET_CURRENT_PHASE,
            LlamaGetCurrentPhaseResponse,
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.LLaMA_GET_CURRENT_PHASE,
            phaseService.get_current_phase,
        )

    # @staticmethod
    # def registerGetBacklogsProtocol():
    #     customProtocolService = CustomProtocolServiceImpl.getInstance()
    #     phaseService = PhaseServiceImpl.getInstance()

    #     requestClassMapInstance = RequestClassMap.getInstance()
    #     requestClassMapInstance.addRequestClass(
    #         UserDefinedProtocolNumber.GET_BACKLOGS, GetBacklogsRequest
    #     )

    #     responseClassMapInstance = ResponseClassMap.getInstance()
    #     responseClassMapInstance.addResponseClass(
    #         UserDefinedProtocolNumber.GET_BACKLOGS, GetBacklogsResponse
    #     )

    #     customProtocolService.registerCustomProtocol(
    #         UserDefinedProtocolNumber.GET_BACKLOGS, phaseService.get_backlogs
    #     )

    @staticmethod
    def registerLlamaGetBacklogsProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        phaseService = LlamaPhaseServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.LLaMA_GET_BACKLOGS, LlamaGetBacklogsRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.LLaMA_GET_BACKLOGS, LlamaGetBacklogsResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.LLaMA_GET_BACKLOGS, phaseService.get_backlogs
        )

    # @staticmethod
    # def registerGetFileListProtocol():
    #     customProtocolService = CustomProtocolServiceImpl.getInstance()
    #     SIOperationService = LlamaAgentOperationServiceImpl.getInstance()

    #     requestClassMapInstance = RequestClassMap.getInstance()
    #     requestClassMapInstance.addRequestClass(
    #         UserDefinedProtocolNumber.GET_FILE_LIST, GetFileListRequest
    #     )

    #     responseClassMapInstance = ResponseClassMap.getInstance()
    #     responseClassMapInstance.addResponseClass(
    #         UserDefinedProtocolNumber.GET_FILE_LIST, GetFileListResponse
    #     )

    #     customProtocolService.registerCustomProtocol(
    #         UserDefinedProtocolNumber.GET_FILE_LIST, SIOperationService.get_file_list
    #     )

    @staticmethod
    def registerLlamaGetFileListProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        SIOperationService = LlamaAgentOperationServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.LLaMA_GET_FILE_LIST, LlamaGetFileListRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.LLaMA_GET_FILE_LIST, LlamaGetFileListResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.LLaMA_GET_FILE_LIST,
            SIOperationService.get_file_list,
        )

    # @staticmethod
    # def registerGetFileContentProtocol():
    #     customProtocolService = CustomProtocolServiceImpl.getInstance()
    #     SIOperationService = SIOperationServiceImpl.getInstance()

    #     requestClassMapInstance = RequestClassMap.getInstance()
    #     requestClassMapInstance.addRequestClass(
    #         UserDefinedProtocolNumber.GET_FILE_CONTENT, GetFileContentRequest
    #     )

    #     responseClassMapInstance = ResponseClassMap.getInstance()
    #     responseClassMapInstance.addResponseClass(
    #         UserDefinedProtocolNumber.GET_FILE_CONTENT, GetFileContentResponse
    #     )

    #     customProtocolService.registerCustomProtocol(
    #         UserDefinedProtocolNumber.GET_FILE_CONTENT,
    #         SIOperationService.get_file_content,
    # )

    @staticmethod
    def registerLlamaGetFileContentProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        SIOperationService = LlamaAgentOperationServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.LLaMA_GET_FILE_CONTENT, LLamaGetFileContentRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.LLaMA_GET_FILE_CONTENT,
            LlamaGetFileContentResponse,
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.LLaMA_GET_FILE_CONTENT,
            SIOperationService.get_file_content,
        )

    @staticmethod
    def registerGetGPUstatusProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        GPUManagementService = GPUManagementServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.GET_GPU_STATUS, GPUManagementRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.GET_GPU_STATUS, GPUManagementResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.GET_GPU_STATUS,
            GPUManagementService.check_available,
        )

    @staticmethod
    def registerLlamaGetTestReportsProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        phaseService = LlamaPhaseServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.LLaMA_GET_TEST_REPORTS, LlamaGetTestReportsRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.LLaMA_GET_TEST_REPORTS,
            LlamaGetTestReportsResponse,
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.LLaMA_GET_TEST_REPORTS,
            phaseService.get_test_reports,
        )

    # @staticmethod
    # def registerGetTestReportsProtocol():
    #     customProtocolService = CustomProtocolServiceImpl.getInstance()
    #     phaseService = PhaseServiceImpl.getInstance()

    #     requestClassMapInstance = RequestClassMap.getInstance()
    #     requestClassMapInstance.addRequestClass(
    #         UserDefinedProtocolNumber.GET_TEST_REPORTS, GetTestReportsRequest
    #     )

    #     responseClassMapInstance = ResponseClassMap.getInstance()
    #     responseClassMapInstance.addResponseClass(
    #         UserDefinedProtocolNumber.GET_TEST_REPORTS, GetTestReportsResponse
    #     )

    #     customProtocolService.registerCustomProtocol(
    #         UserDefinedProtocolNumber.GET_TEST_REPORTS, phaseService.get_test_reports
    #     )

    # @staticmethod
    # def registerGetCodeReviewsProtocol():
    #     customProtocolService = CustomProtocolServiceImpl.getInstance()
    #     phaseService = PhaseServiceImpl.getInstance()

    #     requestClassMapInstance = RequestClassMap.getInstance()
    #     requestClassMapInstance.addRequestClass(
    #         UserDefinedProtocolNumber.GET_CODE_REVIEW, GetCodeReviewsRequest
    #     )

    #     responseClassMapInstance = ResponseClassMap.getInstance()
    #     responseClassMapInstance.addResponseClass(
    #         UserDefinedProtocolNumber.GET_CODE_REVIEW, GetCodeReviewsResponse
    #     )

    #     customProtocolService.registerCustomProtocol(
    #         UserDefinedProtocolNumber.GET_CODE_REVIEW, phaseService.get_code_reviews
    #     )

    @staticmethod
    def registerLlamaGetCodeReviewsProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        phaseService = LlamaPhaseServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.LLaMA_GET_CODE_REVIEW, LlamaGetCodeReviewsRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.LLaMA_GET_CODE_REVIEW, LlamaGetCodeReviewsResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.LLaMA_GET_CODE_REVIEW,
            phaseService.get_code_reviews,
        )

    @staticmethod
    def registerFinetuneProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        finetune_service = FinetuneServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.FINETUNE, FineTuneRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.FINETUNE, FineTuneResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.FINETUNE,
            finetune_service.supervised_finetuning,
        )

    @staticmethod
    def registerUserDefinedProtocol():
        UserDefinedProtocolRegister.registerFirstUserDefinedProtocol()
        # UserDefinedProtocolRegister.registerSIAgentOperationProtocol()
        UserDefinedProtocolRegister.registerLlamaAgentOperationProtocol()
        UserDefinedProtocolRegister.registerWatchdogOperationProtocol()
        # UserDefinedProtocolRegister.registerGetCurrentPhaseProtocol()
        UserDefinedProtocolRegister.registerLlamaGetCurrentPhaseProtocol()
        # UserDefinedProtocolRegister.registerGetBacklogsProtocol()
        UserDefinedProtocolRegister.registerLlamaGetBacklogsProtocol()
        # UserDefinedProtocolRegister.registerGetFileListProtocol()
        UserDefinedProtocolRegister.registerLlamaGetFileListProtocol()
        # UserDefinedProtocolRegister.registerGetFileContentProtocol()
        UserDefinedProtocolRegister.registerLlamaGetFileContentProtocol()
        UserDefinedProtocolRegister.registerGetGPUstatusProtocol()
        # UserDefinedProtocolRegister.registerGetTestReportsProtocol()
        UserDefinedProtocolRegister.registerLlamaGetTestReportsProtocol()
        # UserDefinedProtocolRegister.registerGetCodeReviewsProtocol()
        UserDefinedProtocolRegister.registerLlamaGetCodeReviewsProtocol()
        UserDefinedProtocolRegister.registerUserTestPointProtocol()
        UserDefinedProtocolRegister.registerFinetuneProtocol()
