from _typeshed import Self
from typing import List,AnyStr
import math 
from enum import Enum


class Document:
    def Load_Document():
        source = open('./data/insurance.csv', 'r')
        lines = source.readlines()
        source.close()

    def Parse_lines(self,lines:List[str]):
        self.lines:List[Row] = []
        for line in lines: 
            row_list:List[str] = line.strip().split(',')
            row = Row(row_list)
            self.lines.append(row)

    def Parse_header(self, lines:List[str]):
        pass


class Region(Enum):
    Southeast = 0
    Southwest = 1
    Northeast = 2
    Nortwest = 3


class Row:
    def __init__(self) -> None:
        pass

    def Parse_age(self) -> int:
        pass

    def Parse_sex(self) -> bool:
        pass

    def Parse_bmi(self) -> float:
        pass

    def Parse_children_count(self) -> int:
        pass

    def Parse_smoker(self) -> bool:
        pass 

    def Parse_region(self) -> Region:
        pass

    def Parse_charges(self):
        pass



