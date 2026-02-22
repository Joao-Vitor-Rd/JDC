from ...domain.entities import Section


class SectionMapper:

    @staticmethod
    def to_entity(row: dict) -> Section:
        return Section(
            id=row['id'],
            title=row['nome']
        )
    
    @staticmethod
    def to_entities(rows: list) -> list:
        return [SectionMapper.to_entity(row) for row in rows]
