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

    def average_column(self,value)->float:
        list_values = []
        for value in self.rows:
            list_values.append(value)
            return list_values
        average = sum(list_values) / len(list_values)
        average(float)
        return average

    def sum_column(self,value)-> float:
        list_values = []
        for value in self.rows:
            list_values.append(value)
            return list_values
        return sum(list_values)

    def standard_deviation(self,value)-> float:
        list_variance= []
        value = 0
        for value in self.rows:
            variance = (value - self.average_column(value)) **2
            list_variance.append(variance)
            return list_variance
        std = math.sqrt((sum(list_variance) / len(list_variance)))
        return std





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

    def Parse_bmi(self,value) -> float:
        return float(value)

    def Parse_children_count(self,value) -> int:
        return int(value)

    def Parse_smoker(self,value) -> bool:
        if value == 'yes':
            return True
        return False

    def Parse_region(self,value:str) -> Region:
        if value == 'southeast':
            return Region.Southeast
        elif value == 'southwest':
            return Region.Southwest
        elif value == 'northeast':
            return Region.Northeast
        else:
            return Region.Northwest

    def Parse_charges(self,value) -> float:
        return float(value)




# document = Document()
