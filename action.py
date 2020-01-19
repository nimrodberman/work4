import sys
from DAO import Employees , Suppliers , Activities , Coffee_stands , Products
from DTO import Employee , Supplier , Activity , Coffee_stand , Product
from _Repository import repo


def main(args):
    inputfilename = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            repo.Activities.insert(Activity(*line.split(","))) # insert the activity to the table  // todo : if the activitiy is cancelled do we still insert it to table?

            product = repo.Products.find(line.split(",")[0])
            buyOrSale = int(line.split(",")[1])
            if buyOrSale >= 0:
                product.quantity = product.quantity + buyOrSale
                repo.Products.update(product)

            else:
                if (product.quantity + buyOrSale) >= 0:
                    product.quantity = product.quantity + buyOrSale
                    repo.Products.update(product)

if __name__ == '__main__':
    main(sys.argv)