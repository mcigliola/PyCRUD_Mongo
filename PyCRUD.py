
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30242
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data):
        """ CREATE: Insert a document into the collection.
        Args:
            data (dict): A dictionary representing the document to be created.
                        Must contain a key-value pair.                
        Returns:
            bool: True if successful, else False. """
        if data is not None:
            try:
                self.collection.insert_one(data)  # data should be dictionary  
                print("Document created successfully")
                return True
            except Exception as e:
                print("An error occurred while creating: ", str(e))
                return False        
        else:
            raise ValueError("Nothing to save, because data parameter is empty")


    def read(self, query):
        """ READ: Read a document from the collection.
        Args:
            query (dict): A dictionary representing the document to be found.
                        Must contain a key-value pair.           
        Returns:
            list of results if successful, else empty list."""
        if query is not None:
            try:
                results = list(self.collection.find(query))
                return results
            except Exception as e:
                print("An error occurred while querying: ", str(e))
                return []
        else:
            raise ValueError("Query parameter is empty")
     
        
    def update(self, query, data):
        """UPDATE: Update one or more documents in the collection.
        Args:
            query (dict): A dictionary representing the document(s) to be updated.
                        Must contain a key-value pair.
            data (dict): A dictionary representing the updated values.
                        Must contain a key-value pair.
        Returns:
            number of documents successfully updated."""
        
        if not query:
            raise ValueError("Query parameter is empty")
        
        try:
            update_result = self.collection.update_many(query, {'$set': data})
            if update_result.modified_count == 0:
                print("No matching results found")

            return update_result.modified_count
                
        except Exception as e:
            print("An error occurred while updating: ", str(e))    
            return 0
        
    def delete(self, query):
        """ DELETE: Delete a document from the collection.
        Args:
            query (dict): A dictionary representing the document to be found.
                        Must contain a key-value pair.           
        Returns:
            number of documents successfully deleted."""

        if not query:
            raise ValueError("Query parameter is empty")
        
        try:
            delete_result = self.collection.delete_many(query)  
            if delete_result.deleted_count == 0:
                print("No matching results found to delete")
            
            return delete_result.deleted_count
        
        except Exception as e:
            print("An error occurred while deleting: ", str(e))
            return 0
        
                
                
            