import sys
import csv

#MICHAEL HELLER
#PROFESSOR SCHERR

#-----INVENTORY CLASS-----

class Inventory:

    def __init__(self):
        self.items = []
        self.count = 0
        self.create_inventory()


    def read_csv(self, filename):
        csvFile = open(filename, 'r')
        csvFile.readline()
        dataList = list(csv.reader(csvFile))
        return dataList


    def create_inventory(self):
        self.book_data()
        self.cd_vinyl_data()
        self.collectible_data()
        self.electronics_data()
        self.fashion_data()
        self.home_garden_data()

        
    def check_type(self, item):
        if isinstance(item, Book) == True:
            return 'Book'
        elif isinstance(item, Cd_vinyl) == True:
            return 'Cd_vinyl'
        elif isinstance(item, Collectible) == True:
            return 'Collectible'
        elif isinstance(item, Electronics) == True:
            return 'Electronics'
        elif isinstance(item, Fashion) == True:
            return 'Fashion'
        elif isinstance(item, Home_garden) == True:
            return 'Home_garden'
        
   
    def print_inventory(self, begin = 0, end = -1):
        count = 0
        if begin > 1:
            count = begin
            end += 1
        for i in self.items[begin:end]:
            print('\n------------\n' + 'ID: ' + str(count))  
            print(str(i))
            count += 1
        
        
        
    def compute_inventory(self):
        price_sum = 0
        for i in self.items:
            mul = i.price*i.quantity
            price_sum += mul
        return price_sum
          


    def print_category(self, cat_name):
        count = 0
        for i in self.items:
            count += 1
            cat = self.check_type(i)
            cat2 = cat_name
            if cat == cat2:
                print('\n------------\n' + 'ID: ' + str(count))
                print(str(i))
        
            

    def search_item(self, item_name):
        count = 0
        for i in self.items:
            if item_name in i.name:
                print('\n------------\n' + 'ID: ' + str(count))
                print(str(i))
            count += 1

    def book_data(self):
        book_list = self.read_csv('book.csv')
        for i in book_list:
            name = i[0]
            price = float(i[4])
            quantity = int(i[6])
            pub_date = i[1]
            pub = i[2]
            author = i[3]
            ISBN = i[5]
            book_obj = Book(name, price, quantity, ISBN, pub_date, pub, author)
            self.items.append(book_obj)


    def cd_vinyl_data(self):
        cd_vinyl_list = self.read_csv('cd_vinyl.csv')
        for i in cd_vinyl_list:
            name = i[0]
            price = float(i[5])
            quantity = int(i[6])
            label = i[2]
            date = i[4]
            artists = i[1]
            ASIN = i[3]
            cd_vinyl_obj = Cd_vinyl(name, price, quantity, artists, label, ASIN, date)
            self.items.append(cd_vinyl_obj)


    def collectible_data(self):
        collectible_list = self.read_csv('collectible.csv')
        for i in collectible_list:
            name = i[0]
            price = float(i[1])
            quantity = int(i[4])
            date = i[2]
            owner = i[3]
            collectible_obj = Collectible(name, price, quantity, date, owner)
            self.items.append(collectible_obj)


    def electronics_data(self):
        electronics_list = self.read_csv('electronics.csv')
        for i in electronics_list:
            name = i[0]
            price = float(i[1])
            quantity = int(i[4])
            date = i[2]
            manufacturer = i[3]
            electronics_obj = Electronics(name, price, quantity, date, manufacturer)
            self.items.append(electronics_obj)


    def fashion_data(self):
        fashion_list = self.read_csv('fashion.csv')
        for i in fashion_list:
            name = i[0]
            price = float(i[1])
            quantity = int(i[4])
            date = i[2]
            manufacturer = i[3]
            fashion_obj = Fashion(name, price, quantity, date, manufacturer)
            self.items.append(fashion_obj)

            
    def home_garden_data(self):
        home_garden_list = self.read_csv('home_garden.csv')
        for i in home_garden_list:
            name = i[0]
            price = float(i[1])
            quantity = int(i[4])
            date = i[2]
            manufacturer = i[3]
            home_garden_obj = Home_garden(name, price, quantity, date, manufacturer)
            self.items.append(home_garden_obj)

    

#-----MAIN ITEM CLASS-----
                    
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        s = ''
        s += 'Name: ' + self.name + '\n' + 'Price: ' + str(self.price) + '\n' \
             + 'Quantity: ' + str(self.quantity)
        return s
        
        
        

#-----ALL SUBCLASSES-----

class Ebay(Item):
    def __init__(self, name, price, quantity, date, manufacturer):
        super().__init__(name, price, quantity)
        self.date = date
        self.manufacturer = manufacturer
    

    def __str__(self):
        s = super().__str__()
        s += '\n' + 'Date: ' + self.date + '\n' + 'Manufacturer: ' \
             + self.manufacturer
        return s
        

class Book(Item):
    def __init__(self, name, price, quantity, ISBN, publishing_date, publisher, author):
        super().__init__(name, price, quantity)
        self.ISBN = ISBN
        self.publishing_date = publishing_date
        self.publisher = publisher
        self.author = author

    def __str__(self):
        s = super().__str__()
        s += '\n' + 'Author: ' + self.author + '\n' + 'ISBN: ' + self.ISBN \
             + '\n' + 'Publishing Date: ' + self.publishing_date \
             + '\n' + 'Publisher: ' + self.publisher
        return s
                                

class Cd_vinyl(Item):
    def __init__(self, name, price, quantity, artists, label, ASIN, date):
        super().__init__(name, price, quantity)
        self.artists = artists
        self.label = label
        self.ASIN = ASIN
        self.date = date
    def __str__(self):
        s = super().__str__()
        s += '\n' + 'Artists: ' + self.artists + '\n' + 'ASIN ' + self.ASIN \
             + '\n' + 'Date: ' + self.date \
             + '\n' + 'Label: ' + self.label
        return s
                                

class Electronics(Ebay):
    def __init__(self, name, price, quantity, date, manufacturer):
        super().__init__(name, price, quantity, date, manufacturer)
    def __str__(self):
        return super().__str__()

class Fashion(Ebay):                     
    def __init__(self, name, price, quantity, date, manufacturer):
        super().__init__(name, price, quantity, date, manufacturer)

    def __str__(self):
        return super().__str__()

class Home_garden(Ebay):
    def __init__(self, name, price, quantity, date, manufacturer):
        super().__init__(name, price, quantity, date, manufacturer)
    def __str__(self):
       return super().__str__()
        
class Collectible(Item):
    def __init__(self, name, price, quantity, date, owner):
        super().__init__(name, price, quantity)
        self.date = date
        self.owner = owner 
        
    def __str__(self):
        s = super().__str__()
        s += '\n' + 'Owner: ' + self.owner \
             + '\n' + 'Date: ' + self.date
        return s

       




    

    
    

    

    
