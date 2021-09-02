# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# <Michael Hause>,<08/31/2021>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
file_name = 'products.txt'
lstOfProductObjects = []
strChoice = ''
floatPrice = ''
class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Michael Hause>,<9/1/2021>,Modified code to complete assignment 8
    """

    # constructor for initial values
    def __init__(self, product_name = '', product_price = ''):
        self.__product_name = product_name
        self.__product_price = product_price # added double underscore to make the attribute private

    # getter function
    @ property
    def product_name(self):
        return str(self.__product_name)   #getter for product name

    @property
    def product_price(self):
        return str(self.__product_price)    #getter for product_price
# setter functions
    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:      #checks if a number is entered
            self.__product_name = value.lower()  #sets product name to value if not
        else:
            raise Exception ("Please exclude numbers from the name")    #error message if number is entered

    @product_price.setter
    def product_price(self, value):
        if str(value).isnumeric() == True:  #checks if value is a number
            self.__product_price = float(value)  #sets value as a float if true

#return product name and price as a string
def __str__(self):
    product_price = str(self.__product_price) #turns variable back into a string
    strProduct = self.__product_name + ',' + product_price

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:


    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    @staticmethod
    def save_data_to_file(file_name, lstOfProductObjects):
        file = open(file_name, "w")
        for row in lstOfProductObjects:
            row = row.__str__()
            file.write(row + '\n')
            file.close()
        print("Data saved Successfully!")

    @staticmethod
    def read_data_from_file(file_name, lstofProductObjects):
        file = open(file_name, "r")
        for row in file:
            lstrow = row.split(",")
            dicrow = {"product name": lstrow[0], "product price": lstrow[1]}
            lstofProductObjects.append(dicrow)
        file.close()
    @staticmethod
    def add_data_to_list(name, price, lstofProductObjects):
        strAddProduct = Product(name, price)
        lstofProductObjects.append(str(strAddProduct))
        print("New item added successfully!")
        return lstofProductObjects

    @staticmethod
    def remove_item_from_list(product, lstofProductObjects):
        for row in lstofProductObjects:
            if product.lower() in row["product name"]:
                lstofProductObjects.remove(row)
                print("item removed successfully!")
                break
        else:
            print("item not found")



# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:

    @staticmethod
    def print_menu_products():
        print('''
        Menu of Options:
                1) Add a new product name & price
                2) Remove an existing product
                3) Save Data to File        
                4) Load Data from File
                5) Exit Program
                ''')
        print()

    @staticmethod
    def input_menu_choice():
        menuchoice = str(input("Please select from the following options "))
        return menuchoice

    @staticmethod
    def display_current_list(lstofProductObjects):
        for row in lstOfProductObjects:
            print(row)

    @staticmethod
    def input_new_product():
        product1 = Product()
        strnewProd = str(input("Please enter a product to add: "))
        product1.product_name = strnewProd
        return product1, product1.product_name

    @staticmethod
    def input_new_price():
        strnewPrice = str(input("please enter its price: "))
        price1 = Product()
        price1.product_price = strnewPrice
        return price1, price1.product_price

    @staticmethod
    def product_to_remove():
        removeproduct = str(input("Which prouct would you like to remove? "))
        return removeproduct

    @staticmethod
    def yes_no_input(message):
        strYesNo = str(input(message)).lower()
        return strYesNo
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
#1
FileProcessor.read_data_from_file(file_name, lstOfProductObjects)
IO.display_current_list(lstOfProductObjects)
#2
while (True):
    IO.display_current_list(lstOfProductObjects)
    IO.print_menu_products()
    strChoice = IO.input_menu_choice()
#3
    if strChoice.strip() == '1':
        strProd = IO.input_new_product()
        floatPrice = IO.input_new_price()
        FileProcessor.add_data_to_list(strProd, floatPrice, lstOfProductObjects)
        continue
    if strChoice.strip() == '2':
        strremove = IO.product_to_remove()
        FileProcessor.remove_item_from_list(strremove, lstOfProductObjects)
        continue
    if strChoice.strip() == '3':
        strChoice = IO.yes_no_input("would you like to save? (y/n) ")
        if strChoice.lower() == 'y':
            FileProcessor.save_data_to_file(file_name, lstOfProductObjects)
        else:
            print("Data not saved")
        continue
    if strChoice.strip() == '4':
        strChoice = IO.yes_no_input("Are you sure you would like to reload saved data? (y/n) ")
        if strChoice.lower() == 'y':
            FileProcessor.read_data_from_file(file_name,lstOfProductObjects)
        else:
            print("Data not loaded")
        continue
    if strChoice.strip() == '5':
        strChoice = IO.yes_no_input("Are you sure you want to exit? (y/n)")
        if strChoice.lower() == 'y':
            break
        else:
            print("Exit Cancelled")
        continue

# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #

