# Database_Dashboard
PyCRUD README 

About the Project/Project Title
PyCRUD is a project that uses a simple Python script to provide CRUD (Create, Read, Update, Delete) functionality for a dataset through MongoDB.  PyCRUD leverages the Python driver pyMongo to create an easy-to-use database management tool.  

Motivation
The project is an example of how to implement the pyMongo tool in MongoDB to facilitate streamlined interactions with the database content.  

Getting Started
Note that to implement PyCRUD, you must first ensure that you have MongoDB installed on your machine and that you have imported the dataset you wish to use.  The following screenshot demonstrates the use of the mongoimport tool:

 

You will also need to create a user with read/write permissions for your database as shown below:
 

 

To get a local copy of PyCRUD up and running, follow these steps:
1.	Download the PyCRUD.py file save to your Jupyter directory.
2.	Upload the module into Jupyter and initialize to begin using CRUD commands.

Installation
Tools needed to use PyCRUD include:
•	MongoDB - This project is intended as a means to streamline interaction with a database in MongoDB.  Using another database program will not work.  
•	PyCRUD – Download of the PyCRUD.py file is required to use it locally on your machine.
•	Jupyter – This is a user-friendly way to run the PyCRUD module and execute the CRUD commands to interact with your chosen database.  It removes much of the learning curve required for other Python integrated development environments so that you can get right to work.

Usage

Code Example
The following code snippet shows the create() method, which allows the user to create a new document in the database.
 

This next code snippet shows the read() method, which finds an existing document in the database based on the user’s search criteria and returns its contents.

 

The update() method finds existing documents in the database based on the search criteria and then applies an update to all matching documents.

 

Finally, the delete() method finds all documents matching the search criteria and deletes them from the database.

 


























Tests
	 
 

















Screenshots
The following screenshots demonstrate the functionality of PyCRUD:	
 
 
 

Contact
Mary Cigliola

