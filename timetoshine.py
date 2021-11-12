from _typeshed import Self
from typing import List,AnyStr
import math 



class Document:
    def Load_Document():
        source = open('insurance.csv', 'r')
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






class Row:
    def __init__(self, column) -> None:
        self.column = column 
        pass

    def Parse_age():
        pass

    def Parse_sex():
        pass

    def Parse_bmi():
        pass

    def Parse_children_count():
        pass

    def Parse_smoker(self) -> int:
        if x == 'yes':
            x = 1 
        else:
            x = 0 
        pass 

    def Parse_region():
        pass

    def Parse_charges():
        pass