from dataclasses import dataclass


@dataclass
class CsvFields:
    code: str = 'код'
    project: str = 'проект'
