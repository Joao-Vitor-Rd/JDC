from ..enums import EvaluationResult
from ..enums import EvaluationFlags

class Problem:

    def __init__(
        self,
        id: int,
        title: str,
        description: str,
        inputs: list,
        expected_outputs: list,
        time_limit: float,
        submission_result: EvaluationResult,
        total_of_correct_outputs: int
    ):

        self._id = id
        self._title = title
        self._description = description

        self._inputs = inputs
        self._expected_outputs = expected_outputs
        self._time_limit = time_limit

        self._submission_result = submission_result
        self._total_of_correct_outputs = total_of_correct_outputs

            
    def evaluate_submission(self, code_outputs: list):
        correct_outputs = 0
        submission_result = EvaluationResult.WA

        for output, expected in zip(code_outputs, self._expected_outputs):
            if output == EvaluationFlags.TL_FLAG: 
                submission_result = EvaluationResult.TL
                break

            if output == EvaluationFlags.CE_FLAG:
                submission_result = EvaluationResult.CE
                break
            
            if output == EvaluationFlags.RE_FLAG:
                submission_result = EvaluationResult.RE
                break
            
            if output == expected:
                correct_outputs += 1
        
        if correct_outputs == len(self._expected_outputs):
            submission_result = EvaluationResult.AC
        
        self._update_result(correct_outputs,submission_result)
        
    def _update_result(self, correct_outputs: int, submission_result: EvaluationResult):
        self.total_of_correct_outputs = correct_outputs
        self.submission_result = submission_result

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
    def time_limit(self) -> float:
        return self._time_limit

    @time_limit.setter
    def time_limit(self, time_limit: float) -> None:
        self._time_limit = time_limit

    @property
    def submission_result(self) -> EvaluationResult:
        return self._submission_result

    @submission_result.setter
    def submission_result(self, submission_result: EvaluationResult) -> None:
        self._submission_result = submission_result

    @property
    def total_of_correct_outputs(self) -> int:
        return self._total_of_correct_outputs

    @total_of_correct_outputs.setter
    def total_of_correct_outputs(self, total_of_correct_outputs: int) -> None:
        self._total_of_correct_outputs = total_of_correct_outputs
