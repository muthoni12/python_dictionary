'''

Given a list of dictionaries containing data such as productNmae, exclprice
passed to a function as a parameter, together with the tax rate.
Calculate the incl of each product.
Then print thier values.

incl = excl + vat
vat = excl * tax
e.g
product = [
        {
            "prodname" : "Milk",
            "excl": 50
        },
        {
            "prodname" : "Bread",
            "excl": 40   
        }
    ]

output
milk 65
bread 55
'''

def calculateincl(products, rate):
    incl = 0
    for product in products:
        vat = product["excl"] * rate
        incl = product["excl"] + vat
        print(product["prodname"] +" "+ str(incl))

calculateincl([
    {
        "prodname": "Milk",
        "excl": 50
    },
    {
        "prodname": "Milk",
        "excl": 40   
    }
], 0.16)


'''
Given a list of dictionaries containing data such as productNmae, exclprice
passed to a function as a parameter, together with the tax rate.
Calculate the incl of each product.
Then return a list of dictionaries containing the product and their respective incl prices.
'''

def calculateincl(products, rate):
    incl = {}
    for product in products:
        vat = product["excl"] * rate
        incl = product["excl"] + vat
    
        return {product["prodname"], incl}

calculateincl([
    {
        "prodname": "Milk",
        "excl": 50
    },
    {
        "prodname": "bread",
        "excl": 40   
    }
], 0.16)

'''
def calculateincl(products, rate):
    incl = {}
    for product in products:
        vat = product["excl"] * rate
        incl = product["excl"] + vat
    
        return {product["prodname"], incl}

P = [
    {
        "prodname": "Milk",
        "excl": 50
    },
    {
        "prodname": "bread",
        "excl": 40   
    }
]
calculate(p, 0.16)
'''
