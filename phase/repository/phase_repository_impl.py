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
    
    def get_backlogs(self, *args, **kwargs):
        user_token = args[0]
        return """
    **Backlog 1: Basic Calculator Operations**

* Define the following basic calculator operations:
        + Addition
        + Subtraction
        + Multiplication
        + Division
        + Modulus (remainder)
* Implement the calculator to perform these operations on integers and floating-point numbers

**Backlog 2: Advanced Calculator Operations**

* Define the following advanced calculator operations:
        + Exponentiation
        + Square root
        + Logarithm
        + Trigonometric functions (sin, cos, tan)
* Implement the calculator to perform these operations on integers and floating-point numbers

**Backlog 3: Command-Line Interface (CLI)**

* Develop a command-line interface for the calculator that allows users to input calculations using text commands (e.g. "2 + 3" 
or "/ 4")
* Implement a parser to handle syntax errors and invalid inputs
* Allow users to save and load calculations from files

**Backlog 4: Graphical User Interface (GUI)**

* Develop a graphical user interface for the calculator that allows users to input calculations using buttons and text fields
* Implement a layout system to arrange the GUI elements in a visually appealing way
* Use a library like Tkinter or PyQt to create the GUI

**Backlog 5: Error Handling**

* Develop a robust error handling system that catches and handles exceptions raised during calculation operations
* Implement error messages that provide useful information about the cause of the error
* Allow users to retry calculations with a new input

**Backlog 6: Unit Tests**

* Write unit tests for individual calculator functions to ensure they are working correctly
* Use a testing framework like Pytest or Unittest to write and run tests
    """