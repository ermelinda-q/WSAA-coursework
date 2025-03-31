# Demonstration of the type of function a data layer might have
# Based on topic 8 - WSAA by A. Beatty

class book_dao:
    # get all books
    def get_all(self):
        return [{"id":1, "title":"blah","author":"someone","price":999}]
    # find by id
    def find_by_id(self, id):
        return {"id":1, "title":"blah","author":"someone","price":999}
    # create a book
    def create(self, book):
        return {"id":1, "title":"blah","author":"someone","price":999}
    # update book
    def update(self, id, book):
        return {"id":1, "title":"blah","author":"someone","price":999}
    # delete a book
    def delete(self, id):
        return True
    
book_dao = book_dao()
    
if __name__ == "__main__":
    book = {"id":1, "title":"blah","author":"someone","price":999}
    print("test getall")
    print(f"\t{book_dao.get_all()}")
    print("test find_by_id(1)")
    print(f"\t{book_dao.find_by_id(1)}")
    print("test create")
    print(f"\t{book_dao.create(book)}")
    print("test update")
    print(f"\t{book_dao.update(1, book)}")
    print("test delete")
    print(f"\t{book_dao.delete(1)}")
    
        