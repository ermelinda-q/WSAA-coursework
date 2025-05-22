# Concert Flute Database - WSAA Project

### Author: E.Qejvani

***

This web application is designed to manage a database of concert flutes. Developed using Flask (Python) with a frontend built in HTML, CSS, JavaScript, and AJAX, it provides a user-friendly interface to view, add, delete, and manage flute records efficiently.

***

## Features

- RESTful API endpoints for backend communication
- Built with Flask (Python)
- Uses HTML, CSS, JavaScript, and AJAX for the frontend
- Allows users to view, add, delete, and manage concert flute records via a web interface

***

## Technologies Used

- **Backend:** Flask (Python), MySQL
- **Frontend:** HTML, CSS, jQuery (AJAX)
- **Hosting:** PythonAnywhere

***

## Project Structure

```flute_app/
│
├── data/
│ ├── create_db.py
│ ├── populate_table.py
│ ├── flute_data.csv
│ └── WSAA Project Description
│
├── static/
│ │
│ └── images/
│   ├── flute-image.jpg
│   └── music.jpg
│ │
│ ├── main.css
│ └── style.css
│
├── templates/
│ ├── index.html
│ ├── delete_flute.html
│ ├── create_flute.html
│ ├── find_flute.html
│ ├── update_flute.html
│ └── view_all.html
│
├── fluteDAO.py 
├── dbconfig.py
├── server.py
├── requirements.txt
└── README.md - this file
```
***

## Set up Instructions

***

### Setting up the Database

To set up the flute database, you'll need these files: 
- create_db.py
- populate_table.py
- flute_data.csv. 

Step 1. Install Required Python Module
Make sure mysql-connector-python is installed by running the command:

```pip install mysql-connector-python```

Step 2: Create the Database and Table

Run the script to create the database and flute table:

```python create_db.py```

Step 3: Populate the Table with Data
Run the script to import data from the CSV file into the database:

```python populate_table.py```

After these steps, your database will be populated and ready to use with your web application.

***
### Local:

1. Clone the Repository

    ``` https://github.com/ermelinda-q/WSAA-coursework/tree/main/project ```

2. Create a Virtual Environment




## References:

- [HTML - Using Cards](https://www.w3schools.com/howto/howto_css_cards.asp)
- [CSS & HTML](https://www.freecodecamp.org/news/how-to-link-css-to-html/)
- [Flask render_template](https://www.geeksforgeeks.org/flask-rendering-templates/)
- 
