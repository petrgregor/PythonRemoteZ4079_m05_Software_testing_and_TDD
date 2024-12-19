# With Dependency Injection


class Database:
    def save(self, data):
        print(f"Ukládám do databáze: {data}")


class FileStorage:
    def save(self, data):
        print(f"Ukládám do souboru: {data}")


class DataService:

    def __init__(self, storage):
        self.storage = storage

    def save(self, data):
        self.storage.save(data)


if __name__ == '__main__':
    database = Database()
    file_storage = FileStorage()

    service = DataService(database)
    service.save("Nějaká data.")

    service2 = DataService(file_storage)
    service2.save("Jiná data.")
