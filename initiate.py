import sys
from DAO import Employees , Suppliers , Activities , Coffee_stands , Products
from DTO import Employee , Supplier , Activity , Coffee_stand , Product
from _Repository import repo
import os.path



def main(args):

    repo.create_tables()

    inputfilename = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            line.split(", ")
            if line[0]=="C":
                #print(line[:-1].split(", ")[1:])
                repo.Coffee_stands.insert(Coffee_stand(*line.split(", ")[1:]))

            if line[0]=="E":
                #print(line[:-1].split(", ")[1:])
                repo.Employees.insert(Employee(*line.split(", ")[1:]))

            if line[0]=="S":
                #print(line[:-1].split(", ")[1:])
                repo.Suppliers.insert(Supplier(*line.split(", ")[1:]))

            if line[0]=="P":
                #print(line[:-1].split(", ")[1:].__add__(["0"]))
                repo.Products.insert(Product(*line.split(", ")[1:].__add__(["0"])))



if __name__ == '__main__':
    main(sys.argv)