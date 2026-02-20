from ...application.dtos import ProblemBriefDTO

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
