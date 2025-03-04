from pymongo import MongoClient

class MongoDB:
    def __init__(self, uri="mongodb+srv://doadmin:VBj19g2YyE5i0678@db-mongodb-lon1-56586-3969746e.mongo.ondigitalocean.com/admin?tls=true&authSource=admin"):
        # Inicializa la conexión a MongoDB con la URI proporcionada
        self.client = MongoClient(uri)

    def get_collection(self, db_name, collection_name):
        # Devuelve la colección de la base de datos especificada
        db = self.client[db_name]
        collection = db[collection_name]
        return collection

    def close_connection(self):
        # Cierra la conexión con MongoDB
        self.client.close()