class Problem:

    STATUS_UNSOLVED = "US"
    STATUS_ACCEPTED = "AC"
    STATUS_WRONG_ANSWER = "WA"
    STATUS_TIME_LIMIT_EXCEED = "TL"
    STATUS_COMPILER_ERROR = "CE"

    def __init__(
        self,
        id: int,
        title: str,
        description: str,
        inputs: list,
        expected_outputs: list,
        submission_result: str,
        total_of_correct_outputs: int,
    ):

        self._id = id
        self._title = title
        self._description = description

        self._inputs = inputs
        self._expected_outputs = expected_outputs

        self._submission_result = submission_result
        self._total_of_correct_outputs = total_of_correct_outputs
        
    def compare_outputs(self, code_outputs: list) -> int:
        correct_outputs = 0

        for it_code_outputs, it_expected_outputs in zip(code_outputs, self._expected_outputs):
            if it_code_outputs == it_expected_outputs:
                correct_outputs += 1
        return correct_outputs
    
    def evaluete_submission(self, code_outputs: list) -> str:
        submission_correct_outputs = self.compare_outputs(code_outputs)

        if code_outputs[0] == "@TL@" or code_outputs[0] == "@CE@":
             self._submission_result = code_outputs[0]
        else:
        
            if submission_correct_outputs == len(self._expected_outputs):
                self._submission_result = self.STATUS_ACCEPTED
            else:
                self._submission_result = self.STATUS_WRONG_ANSWER

        self._total_of_correct_outputs = submission_correct_outputs


    
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id
    
    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        self._title = title

    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, description: str) -> None:
        self._description = description

    @property
    def inputs(self) -> list:
        return self._inputs

    @inputs.setter
    def inputs(self, inputs: list) -> None:
        self._inputs = inputs

    @property
    def expected_outputs(self) -> list:
        return self._expected_outputs

    @expected_outputs.setter
    def expected_outputs(self, expected_outputs: list) -> None:
        self._expected_outputs = expected_outputs

    @property
    def submission_result(self) -> str:
        return self._submission_result

    @submission_result.setter
    def submission_result(self, submission_result: str) -> None:
        self._submission_result = submission_result

    @property
    def total_of_correct_outputs(self) -> int:
        return self._total_of_correct_outputs

    @total_of_correct_outputs.setter
    def total_of_correct_outputs(self, total_of_correct_outputs: int) -> None:
        self._total_of_correct_outputs = total_of_correct_outputs