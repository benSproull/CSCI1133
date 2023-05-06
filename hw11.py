# Problem A
class Item():
    '''
    Purpose: The object is to take in a csv_string and find the name, price, category, and store for each one
    Instance variables: csv_string = a user inputted csv file that has names, price, and category for items in that store
                        store = what store you are looking at for the items
    Methods: __init__ is the contructor and sets everything up for the other methods to run through
             __str__ prints out a string of the name, category and price of a desired item
             __lt__ lets the user know if the current store and better prices then the other store by returning True or False


    '''
    def __init__(self, csv_string, store):
        items = csv_string.split(',')
        self.name = items[0]
        self.price = float(items[1])
        self.category = items[2]
        self.store = store

    def __str__(self):
        return f"{self.name} ({self.category}): ${self.price}"

    def __lt__(self, other):
        if self.price < other.price:
            return True
        else:
            return False

class Store():
    '''
    Purpose: The object of this class is to seperate items in each store and find the cheapest outfit
    Instance variables: name = the name of the store you are splitting up
                        filename = the csv file that is inputted and wanting to be split up
    Methods: __init__ is the Constructor to set everything up and make it readily availible for the rest of the methods to run it through
             __str__ returns a string of all the items
             cheapest_outfit picks out which outfit would be the cheapest and returns it back to the user
             

    '''
    def __init__(self, name, filename):
        self.name = name
        self.items = []
        f = open(filename, 'r')
        lines = f.readlines()
        print(lines)
        for i in range(1, len(lines)):
            items = Item(lines[i].strip(), name)
            self.items = self.items + [items]
        f.close()

    def __str__(self):
        s = self.name
        for i in self.items:
            s = s + str(i)
        return s

    def cheapest_outfit(store_list):
        outfit = {'Head': None, 'Torso': None, 'Legs': None, 'Feet': None}
        items = store.items
        for item in items:
            category = item.category
            if outfit[category] == None or item < outfit[category]:
                outfit[category] = item.price


        return outfit

def choose_store(store_list):
        lowest_price = store_list[0]
        price = 0

        for store in store_list:
            outfit = store.cheapest_outfit()
            if len(outfit) == 0:
                print(store.name,': Outfit Incomplete')
            elif len(outfit) == 4:
                total_price = sum(outfit.values())

                if total_price < price:
                    lowest_price = store
                price = total_price
                print(f"{store.name}: ${total_price}")
        print(lowest_price)




def main():

    safety_pants = Item('Orange Saftey Pants', 34.66, 'Legs', 'Sparkles')
    print(safety_pants.name)
    print(safety_pants.price)
    print(safety_pants.category)
    print(safety_pants.store)
    print(safety_pants)

    store1 = Store('Sparkles', 'sparkles.csv')
    print(store1.name)
    print(store1.items)
