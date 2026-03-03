class Database:
    def __init__(self):
        self.data = {}
        self.next_id = 1

    def create(self, value):
        self.data[self.next_id] = value
        output = self.next_id
        self.next_id += 1
        return output

    def read(self, item_id):
        if item_id in self.data:
            return self.data[item_id]
        else:
            return None

    def update(self, item_id, new_value):
        if item_id in self.data:
            self.data[item_id] = new_value
            return True
        else:
            return False

    def delete(self, item_id):
        if item_id in self.data:
            self.data.pop(item_id)
            return True
        else:
            return False

if __name__ == "__main__":
    # create database object
    db = Database()

    # create 2 items in the database
    x = db.create(10)
    y = db.create(20)

    # print the ids of the items
    print(x)
    print(y)

    # print the value of the first item
    print(db.read(1))

    # update first item to new value
    a = db.update(1, 30)

    # print result of that update
    print(a)

    # print value of the new value
    print(db.read(1))

    # delete 2nd item
    b = db.delete(2)

    # print result of delete
    print(b)

    # attempt to read deleted item and print result
    print(db.read(2))