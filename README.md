# PyCRUD_Mongo

<h2>About the Project</h2>

PyCRUD is a project that uses a simple Python script to provide CRUD (Create, Read, Update, Delete) functionality for a dataset through MongoDB.  PyCRUD leverages the Python driver pyMongo to create an easy-to-use database management tool.  The project is an example of how to implement the pyMongo tool in MongoDB to facilitate streamlined interactions with the database content.  

<h2>Getting Started</h2>

Note that to implement PyCRUD, you must first ensure that you have MongoDB installed on your machine and that you have imported the dataset you wish to use.  The following screenshot demonstrates the use of the mongoimport tool:

 ![](/Images/Picture1.png)

You will also need to create a user with read/write permissions for your database as shown below:
 
![](/Images/Picture2.png)

![](/Images/Picture3.png)

To get a local copy of PyCRUD up and running, follow these steps:
1.	Download the PyCRUD.py file save to your Jupyter directory.
2.	Upload the module into Jupyter and initialize to begin using CRUD commands.

<h2>Installation</h2>

Tools needed to use PyCRUD include:
•	MongoDB - This project is intended as a means to streamline interaction with a database in MongoDB.  Using another database program will not work.  
•	PyCRUD – Download of the PyCRUD.py file is required to use it locally on your machine.
•	Jupyter – This is a user-friendly way to run the PyCRUD module and execute the CRUD commands to interact with your chosen database.  It removes much of the learning curve required for other Python integrated development environments so that you can get right to work.

<h2>Usage</h2>

<h3>Code Example</h3>
The following code snippet shows the create() method, which allows the user to create a new document in the database.

![](/Images/Picture4.png) 

This next code snippet shows the read() method, which finds an existing document in the database based on the user’s search criteria and returns its contents.

![](/Images/Picture5.png)
 

The update() method finds existing documents in the database based on the search criteria and then applies an update to all matching documents.

![](/Images/Picture6.png)
 

Finally, the delete() method finds all documents matching the search criteria and deletes them from the database.

![](/Images/Picture7.png)


<h2>Tests</h2>

![](/Images/Picture8.png)	
![](/Images/Picture9.png)
 


<h2>Screenshots</h2>
The following screenshots demonstrate the functionality of PyCRUD:	

![](/Images/Picture10.png) 

![](/Images/Picture11.png)

![](/Images/Picture12.png)
 
 

