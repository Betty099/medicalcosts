# from _typeshed import Self
from typing import List,AnyStr
from enum import Enum
import math
from matplotlib import pyplot as plt 
import numpy as np
from numpy.lib.function_base import average
from numpy.lib.polynomial import poly 
from random import randint
from typing import Callable


class Point: 
    def __init__(self,x,y) -> None:
        self.x:float = x
        self.y:float = y

    def distance(self,point) -> float:
        point_distance = math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        return point_distance



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

    def average_column_charges(self)->float:
        # list_values = []
        # for row in self.rows:
        #     list_values.append(row.charges)
        # average = sum(list_values) / len(list_values)
        # return average
        return self.average_column(lambda row: row.charges)
        

    def average_column_age(self)->float:
        return self.average_column(lambda row: row.age)


    def average_column(self, select_property: Callable):
        list_values = []
        for row in self.rows:
            selected_value = select_property(row)
            list_values.append(selected_value)
        average = sum(list_values) / len(list_values)
        return average
    


        # selector a pouzil lambdu -> v te lambe bude brat parametr row a v tom sahne na jeden parametr (funkce sahne na lambdu a da selector)

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
            variance = (value - self.average_column_charges(value)) **2
            list_variance.append(variance)
            return list_variance
        std = math.sqrt((sum(list_variance) / len(list_variance)))
        return std

    def region_distribution(self)-> None:
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
        # plt.show()

    def regrese_age(self)->plt:
        x_age = []
        y_insurance_in_USD = []
        for row in self.rows:
            x_age.append(row.age)
            y_insurance_in_USD.append(row.charges)
        # age_array = np.array(x_age)
        # list_of_errors_insurance = []
        # for value in insurance_in_USD:
        #     error = (value - self.average_column(value)**2)
        #     list_of_errors_insurance.append(error)
        
        # plt.plot(age,list_of_errors_insurance)
        n = len(x_age)
        
        average_insurance = self.average_column_charges()
        average_age = self.average_column_age()


        errors_x = []
        errors_y = []
        for x in x_age:
            x_error = x - average_age
            errors_x.append(x_error)
        for y in y_insurance_in_USD:
            y_error = y - average_insurance
            errors_y.append(y_error)

        variance_list_x = []
        for x in errors_x:
            var = x **2
            variance_list_x.append(var)
        sum_deviation_x = sum(variance_list_x)
        varinace_x = sum_deviation_x / n
        variance_list_y = []
        for y in errors_y:
            var = y ** 2
            variance_list_y.append(var)
        sum_deviation_y = sum(variance_list_y)
        variance_y = sum_deviation_y / n

        # prejmenuj si nesmysly

        errors_x_y_times = [a*b for a,b in zip(errors_x,errors_y)]
        covariance_x_y = sum(errors_x_y_times)/n
        print(f'covar_x_y:{covariance_x_y}')
        a_1 = covariance_x_y / varinace_x
        a_0 = average_insurance - (a_1 * average_age)
        
        prediction_start = (a_1 * x_age[0]) + a_0
        prediction_end = (a_1 * x_age[-1]) + a_0
        prediction_insurance = []
        for x in x_age:
            prediction = a_1 * x + a_0
            prediction_insurance.append(prediction)
        loss = 0.0
        for y_real , y_prediction in zip(y_insurance_in_USD,prediction_insurance):
            rozdil = (y_real - y_prediction) **2
            loss += rozdil
            

        print('loss', loss)
        print('a1: ', a_1)
        print('a0: ', a_0)

        plt.figure()
        plt.suptitle('Linear Regrese')
        plt.xlabel('Age')
        plt.ylabel('Insurance') 


        plt.scatter(x_age,y_insurance_in_USD)
        plt.plot([x_age[0], x_age[-1]],[prediction_start, prediction_end],'-r')
        plt.plot([x_age[0], x_age[-1]],[average_insurance, average_insurance],'-g')
        plt.show()

    
        
    # regrese = pro vek a cenu pojistky (predpovis cenu pojistky na zaklade veku - kolik pro takovej vek ocekam pojistku (polinomicka ale muzes udelat linearni (quadraticky)))
    # methoda leastsquares = 
    # k_means jsou skupiny -> ja mu rekne kolik skupin

    def np_regression(self):
        x = []
        y = []
        for row in self.rows:
            x.append(row.age)
            y.append(row.charges)
        x = np.array(x)
        y = np.array(y)
        cov_x_y = np.cov(x,y)
        var_x = np.var(x)
        y_mean = np.mean(y)
        x_mean = np.mean(x)

        a_1 = cov_x_y[0] / var_x
        a_0 = y_mean - (a_1 * x_mean)
        polyfit = np.polynomial.polynomial.polyfit(x,y,1)
        print(f'a1: {a_1} \n a0: {a_0} \n polyfit: {polyfit}')


    def k_means(self):
        points:List[Point] = []
        ages = []
        charges = []
        for row in self.rows: 
            ages.append(row.age)
            charges.append(row.charges)
        age_max = max(ages)
        charges_max = max(charges)

        for row in self.rows:
            point = Point(row.age / age_max, row.charges / charges_max)
            points.append(point)
        k_1 = Point(0,0)
        k_2 = Point(1,1)
        n = 3
        for i in range(n):
            k_1_points:List[Point] = []
            k_2_points:List[Point] = []
            for point in points:
                k_1_distance = point.distance(k_1)
                k_2_distance = point.distance(k_2)
                if k_1_distance <= k_2_distance:
                    k_1_points.append(point)
                else: 
                    k_2_points.append(point)
            k_1_x = []
            k_1_y = []
            for point in k_1_points:
                k_1_x.append(point.x)
                k_1_y.append(point.y)
            
            k_2_x = []
            k_2_y = []
            for point in k_2_points:
                k_2_x.append(point.x)
                k_2_y.append(point.y)
            
            plt.figure()
            plt.scatter(k_1_x,k_1_y, c = 'r')
            plt.scatter(k_2_x,k_2_y, c = 'b')
            plt.scatter(k_1.x , k_1.y , 100, c = 'g')
            plt.scatter(k_2.x, k_2.y, 100, c = 'y')
            plt.show()

            k_1 = Point(average(k_1_x), average(k_1_y))
            k_2 = Point(average(k_2_x), average(k_2_y))

        
       
        
        



        
        





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
# document.region_distribution()
# document.regrese_age()

# document.np_regression()
# document.regrese_age()
# document.k_means()
promena = document.average_column(lambda row: row.charges)
print(promena)