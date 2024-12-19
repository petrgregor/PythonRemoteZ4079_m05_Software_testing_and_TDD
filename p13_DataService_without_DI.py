# Without Dependency Injection


class Database:
    def save(self, data):
        print(f"Ukládám do databáze: {data}")


class DataService:

    def __init__(self):
        self.db = Database()

    def save(self, data):
        self.db.save(data)


if __name__ == '__main__':
    service = DataService()
    service.save("Nějaká data.")
