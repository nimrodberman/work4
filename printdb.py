import sys
from DAO import Employees , Suppliers , Activities , Coffee_stands , Products
from DTO import Employee , Supplier , Activity , Coffee_stand , Product
from _Repository import repo
import os.path



def main():
    repo.print()

if __name__ == '__main__':
    main()