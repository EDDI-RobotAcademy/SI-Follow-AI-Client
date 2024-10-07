import os
import sys

from first_user_defined_function_domain.service.fudf_service_impl import FudfServiceImpl
from first_user_defined_function_domain.service.request.fudf_just_for_test_request import FudfJustForTestRequest
from first_user_defined_function_domain.service.response.fudf_just_for_test_response import FudfJustForTestResponse
from si_operation.service.si_operation_service_impl import SIOperationServiceImpl
from si_operation.service.request.si_operation_request import SIOperationRequest
from si_operation.service.response.si_operation_response import SIOperationResponse
from watchdog_operation.service.watchdog_operation_service_impl import WatchdogOperationServiceImpl
from watchdog_operation.service.request.watchdog_service_request import WatchdogOperationRequest
from watchdog_operation.service.response.watchdog_service_response import WatchdogOperationResponse
from phase.service.phase_service_impl import PhaseServiceImpl
from phase.service.request.get_current_phase_service_request import GetCurrentPhaseRequest
from phase.service.response.get_current_phase_service_response import GetCurrentPhaseResponse

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'si_agent'))

from template.custom_protocol.service.custom_protocol_service_impl import CustomProtocolServiceImpl
from template.request_generator.request_class_map import RequestClassMap
from template.response_generator.response_class_map import ResponseClassMap

from user_defined_protocol.protocol import UserDefinedProtocolNumber


class UserDefinedProtocolRegister:
    @staticmethod
    def registerFirstUserDefinedProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        firstUserDefinedFunctionService = FudfServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.FIRST_USER_DEFINED_FUNCTION_FOR_TEST,
            FudfJustForTestRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.FIRST_USER_DEFINED_FUNCTION_FOR_TEST,
            FudfJustForTestResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.FIRST_USER_DEFINED_FUNCTION_FOR_TEST,
            firstUserDefinedFunctionService.justForTest
        )

    @staticmethod
    def registerSIAgentOperationProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        siAgentOperationService = SIOperationServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.SI_AGENT_OPERATION,
            SIOperationRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.SI_AGENT_OPERATION,
            SIOperationResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.SI_AGENT_OPERATION,
            siAgentOperationService.operateSIAgent
        )
        
        
    @staticmethod
    def registerWatchdogOperationProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        watchdogOperationService = WatchdogOperationServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.WATCHDOG_OPERATON,
            WatchdogOperationRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.WATCHDOG_OPERATON,
            WatchdogOperationResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.WATCHDOG_OPERATON,
            watchdogOperationService.operateWatchdog
        )
        
        
    @staticmethod
    def registerGetCurrentPhaseProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        phaseService = PhaseServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.GET_CURRENT_PHASE,
            GetCurrentPhaseRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.GET_CURRENT_PHASE,
            GetCurrentPhaseResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.GET_CURRENT_PHASE,
            phaseService.get_current_phase
        )
        

    @staticmethod
    def registerUserDefinedProtocol():
        UserDefinedProtocolRegister.registerFirstUserDefinedProtocol()
        UserDefinedProtocolRegister.registerSIAgentOperationProtocol()
        UserDefinedProtocolRegister.registerWatchdogOperationProtocol()
        UserDefinedProtocolRegister.registerGetCurrentPhaseProtocol()
