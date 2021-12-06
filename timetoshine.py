# from _typeshed import Self
from typing import List,AnyStr
from enum import Enum
import math
from matplotlib import pyplot as plt 

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

    def average_column(self, select_number)->float:
        list_values = []
        for row in self.rows:
            list_values.append(row.charges)
        average = sum(list_values) / len(list_values)
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

    def region_distribution(self)-> plt:
        values_region = []
        for row in self.rows:
            values_region.append(row.region)
        Southeast_count = values_region.count(Region.Southeast)
        Southwest_count = values_region.count(Region.Southwest)
        Northeast_count = values_region.count(Region.Northeast)
        Northwest_count = values_region.count(Region.Northwest)
        names = ['southeast', 'southwest', 'northeast','northwest']
        values = [Southeast_count, Southwest_count, Northeast_count, Northwest_count]
        maximum = max(values)
        normalized_values = []
        for value in values:
            normalized = value/maximum
            normalized_values.append(normalized)
        plt.figure(figsize=(1,3))

        plt.subplot(1,3,1)
        plt.bar(names,normalized_values)
        plt.xticks(range(4),names,rotation = 90)
        
        plt.subplot(1,3,2)
        plt.scatter(names, normalized_values)
        plt.xticks(range(4),names,rotation = 90)
        
        plt.subplot(1,3,3)
        plt.plot(normalized_values)
        plt.xticks(range(4),names,rotation = 90)

        # fig.('Regional Distribution')
        plt.show()

        
    # regrese = pro vek a cenu pojistky (predpovis cenu pojistky na zaklade veku - kolik pro takovej vek ocekam pojistku (polinomicka ale muzes udelat linearni (quadraticky)))
    # methoda leastsquares = 

        





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




document = Document()
# average = document.average_column()
document.region_distribution()