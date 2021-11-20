# from _typeshed import Self
from typing import List,AnyStr
from enum import Enum
import math

class Document:
    def __init__(self) -> None:
        self.Load_Document()
    
    def Load_Document(self):
        source = open('./data/insurance.csv', 'r')
        lines = source.readlines()
        self.Parse_header(lines[0])
        self.Parse_lines(lines[1:])
        source.close()

    def Parse_lines(self,lines:List[str]):
        self.rows:List[Row] = []
        for line in lines: 
            row = Row(line)
            self.rows.append(row)

    def Parse_header(self, lines:List[str]):
        pass


class Region(Enum):
    Southeast = 0
    Southwest = 1
    Northeast = 2
    Northwest = 3


class Row:
    def __init__(self, line:str) -> None:
        list_values:List[str] = line.strip().split(',')
        self.age:int = self.Parse_age(list_values[0])
        self.isfemale:bool = self.Parse_sex(list_values[1])
        self.bmi:float = self.Parse_bmi(list_values[2])
        self.children_count:int = self.Parse_children_count(list_values[3])
        self.smoker:bool = self.Parse_smoker(list_values[4])
        self.region:Region = self.Parse_region(list_values[5])
        self.charges:float = self.Parse_charges(list_values[6])


    def Parse_age(self,value:str) -> int:
        return int(value)

    def Parse_sex(self,value:str) -> bool:
        if value == 'female':
            return True
        return False

    def Parse_bmi(self) -> float:
        return float

    def Parse_children_count(self) -> int:
        return int

    def Parse_smoker(self) -> bool:
        return bool

    def Parse_region(self,value:str) -> Region:
        if value == 'southeast':
            return Region.Southeast
        elif value == 'southwest':
            return Region.Southwest
        elif value == 'northeast':
            return Region.Northeast
        else:
            return Region.Northwest

    def Parse_charges(self) -> float:
        return float


document = Document()
document.Load_Document()