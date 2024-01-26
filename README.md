# Simple RestAPI for a Parts Warehouse.
- The warehouse contains small parts used in electronic repair workshops. The API will be connected to a MongoDB database with some mockup data, including two collections: 'parts' and 'categories'. <br>
- CRUD functionality for both collections and adding one additional endpoint for search in a parts collection. <br>
- Containerize using Docker. <br>
- Input validation for both collections. <br>
- The API should return results in JSON format. 


1. MongoDB Setup:
- Create a MongoDB database named with your name (firstname_lastname) for the Parts Warehouse during the application kickstart.
- Implement two collections: 'parts' and 'categories'.
- Populate dataset with some startup data (minium: 1 main category, 2 side categories, 6 parts). 

2. Parts - Model Description: 
The 'Part' object model represents each part in the warehouse. The mandatory fields are as follows:
- serial_number (str): A unique serial number assigned to each part.
- name (str): The name or model of the part.
- description (str): A brief description of the part.
- category (str): The category to which the part belongs (e.g., resistor, capacitor, IC).
- quantity (int): The quantity of the part available in the warehouse.
- price (float): The price of a single unit of the part.
- location (dict): A dictionary specifying the exact location of the part in the warehouse, including sections such as room, bookcase, shelf, cuvette, column, row.

3. Categories - Model Description:
The 'Category' object model represents the categories to which parts belong. The mandatory fields
are as follows:
- name (str): The name of the category.
- parent_name (str): If empty, this is a base category. This will be used to create a category tree.

4. CRUD Operations:
Parts collection:
- Implement CRUD operations (Create, Read, Update, Delete) for the 'parts' collection.
- Ensure that a part cannot be assigned to a base category.
Categories collection:
- Implement CRUD operations for the 'categories' collection.
- Ensure that a category cannot be removed if there are parts assigned to it.
- Ensure that a parent category cannot be removed if it has child categories with parts assigned.

5. Search Endpoints:
Create one additional endpoint:
- Search for parts based on all mandatory fields – your own implementation.

6. Input Validation:
- Implement input validation for both collections.
- Pay special attention to the 'location' field in the 'parts' dataset, which includes sections such as
room, bookcase, shelf, cuvette, column, row.
- Ensure that each part belongs to a category and that a part cannot be in a base category.

7. Dockerization:
 - Dockerize the application, ensuring that it can be easily deployed and run in a containerized
environment.

8. Framework Choice:
- You have the flexibility to choose the Python frameworks you deem suitable for the task. Consider
justifying your choices in your submission.

9. JSON Format:
- Ensure that the API returns results in JSON format and can be consumed with Postman.
Submission Guidelines:
- Provide a GitHub repository with your codebase.
- Include clear instructions on how to set up and run the Dockerized application.
- Include a brief README explaining your approach, chosen frameworks, and any additional details
you would like to highlight – like accessible endpoints.
Evaluation Criteria:
- Code structure and organization.
- Implementation of CRUD operations and search endpoint.
- Proper usage of MongoDB for data storage.
- Input validation for both datasets, with special attention to the new 'location' field and category
relationships.
- Dockerization of the application.
- Clear and concise documentation (installation and API).


### MongoDb connection string and setup:
- mongodb+srv://rekrutacja:BZijftwEru0oELxT@cluster11.yxu8n2k.mongodb.net/
- database = 'FIRSTNAME_LASTNAME'; 