from ...application.dtos import ProblemBriefDTO
from ...domain.entities import Problem

class ProblemMapper:

    @staticmethod
    def to_brief_dto(row: dict) -> ProblemBriefDTO:
        return ProblemBriefDTO(
            id=row['id'],
            title=row['title']
        )
    
    @staticmethod
    def to_brief_dtos(rows: list) -> list[ProblemBriefDTO]:
        return [ProblemMapper.to_brief_dto(row) for row in rows] 
       
    @staticmethod
    def to_problem(row: dict, test_cases: list = None) -> Problem:
        inputs = []
        expected_outputs = []
        
        if test_cases:
            for test in test_cases:
                input_value = test['input_value'].replace('\\n', '\n') if test['input_value'] else ''
                expected_value = test['expected_output'].replace('\\n', '\n') if test['expected_output'] else ''
                inputs.append(input_value)
                expected_outputs.append(expected_value)
        
        return Problem(
            id=row['id'],
            title=row['title'],
            description=row['description'],
            submission_result=row.get('submission_result'),
            total_of_correct_outputs=row.get('total_of_correct_outputs'),
            inputs=inputs,
            expected_outputs=expected_outputs
        )