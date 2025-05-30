# Concert Flute Database - A WSAA Project

### Author: E. Qejvani

***
This README has been written with [GitHub's documentation on READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) in mind.
You should refer to that documentation for more information on writing an appropriate README for visitors to your repository.
You can find out more about [writing in MarkDown in GitHub's documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

***
## About this Repository

This git sub-repository (WSAA-coursework/project) holds all the project files of Web Services and Applications module, as part of my [Hdip in Computer Science in Data Analytics](https://www.atu.ie/courses/higher-diploma-in-science-data-analytics#:~:text=You%20are%20a%20Level%208,topics%20in%20your%20original%20degree) in [ATU](https://www.atu.ie/).

In this project a web application is designed to manage a database of concert flutes. Developed using Flask (Python) with a frontend built in HTML, CSS, JavaScript, and AJAX, it provides a user-friendly interface to view, add, delete, and manage flute records efficiently.

You can access the web app at https://ermelinda.pythonanywhere.com/

***

## Features

- RESTful API endpoints for backend communication
- Built with Flask (Python)
- Uses HTML, CSS, JavaScript, and AJAX for the frontend
- Allows users to view, add, delete, and manage a database records via a web interface

***

## Technologies Used

- **Backend:** Flask (Python), MySQL
- **Frontend:** HTML, CSS, jQuery (AJAX)
- **Hosting:** PythonAnywhere
- **Photo Editor** Microsoft Designer

***

## Project Structure

```flute_app/
│
├── data/                           # Directory for database-related scripts and data.
│ ├── create_db.py                  # Script to create and database and 'flute' table.
│ ├── populate_table.py             # Script to populate the 'flute' table with data from 'flute_data.csv'.
│ ├── flute_data.csv                # CSV file containing initial flute records to load into the database.
│ └── WSAA Project Description      # This project's description.
│
├── static/                         # Static files used in the web app (CSS and images).
│ │
│ └── images/                       # Directory holding images used in HTML pages.
│   ├── flute-image.jpg             # Flute image displayed on the index page.
│   └── music.jpg                   # Background image.
│ │
│ ├── main.css                      # Main stylesheet for global layout.
│ └── style.css                     # Additional styles for specific elements.
│
├── templates/                      # Contains HTML templates rendered by Flask.
│ ├── index.html                    # Homepage of the flute database web application.
│ ├── delete_flute.html             # Page to delete a flute record by ID.
│ ├── create_flute.html             # Form to input and create a new flute record.
│ ├── find_flute.html               # Page to search for a flute based on flute's ID.
│ ├── update_flute.html             # Form to update existing flute record details.
│ └── view_all.html                 # Displays all flute records in a table format.
│
├── fluteDAO.py                     # Data Access Object file containing functions to interact with the database (CRUD operations).
├── dbconfig.py                     # Database configuration file (path, name, connection settings).
├── server.py                       # Main Flask server application that handles routing, logic, and rendering of templates.
├── requirements.txt                # List of Python packages required to run the application.
└── README.md                       # Project README file - this file.
```
***

## Set up Instructions

***

### Setting up the Database

To set up the flute database, you'll need these files: 
- create_db.py
- populate_table.py
- flute_data.csv. 

**Step 1. Install Required Python Module**

Make sure mysql-connector-python is installed by running the command:

```pip install mysql-connector-python```

**Step 2: Make username and password changes**

Type your MySQL username and password in the password section of the code in both the create_db.py and populate_table.py files.

**Step 3: Create the Database and Table**

Run the script to create the database and flute table:

```python create_db.py```

**Step 4: Populate the Table with Data**

Run the script to import data from the CSV file into the database:

```python populate_table.py```

After these steps, your database will be populated and ready to use with your web application.

***
### Running the App Locally:

**Step 1. Clone the Repository**

```https://github.com/ermelinda-q/WSAA-coursework/tree/main/project```

**Step 2: Make changes to 'dbconfit.py'**

Enter your MySQL username and password in the dbconfig.py file so the app can connect to the database properly.

**Step 3. Create and Activate a Virtual Environment**

- ```python -m venv venv```

- ```venv/bin/activate ```

**Step 4. Install the required packages**

```pip install -r requirements.txt```

**Step 5. Run the Flask App**

```python server.py```

**Step 6 - Final Step**

 Navigate to http://127.0.0.1:5000/ in your browser to access the app.

***
### Running the App on PythonAnywhere:

***

**Step 1: Create a PythonAnywhere Account**

- Create a free account in https://www.pythonanywhere.com 

**Step 2: Clone Your GitHub Project Directory on PythonAnywhere**

- Start a Bash console.
- Clone your project from GitHub:

```git clone 'name of your github directory'```

**Step 3: Set Up a MySQL Database on PythonAnywhere**

- Open the "Databases" tab.
- Create a new MySQL database.
- Don't forget to write down: Username, Database name and Password

**Step 4: Update dbconfig.py with PythonAnywhere Credentials**

- In the files directory double click 'dbconfig.py'
- Update the file with your data
- Save and exit.

**Step 5: Create and Populate the MySQL Database**

- On the Bash console, run:

    - ```python data/create_db.py```
    - ```python populate_table.py```

- The above will:
    - Create the flute table in the database.
    - Load data from flute_data.csv in the new created table.

**Step 6: Set up the Web App on Pythonanywhere**

- Go the the 'Web' tab of you account.
- Click 'Add a new web app'.
- Set the source code path to: /home/yourusername/project folder.

**Step 7: Other changes to not forget**

- Click the WSGI file link in the Web tab.
- Set the path to your project file.
- Do the same for 'Source directory' section.
- Update the jQuery AJAX section in the HTML file by removing the localhost address from the URL, changing it from url: 'http://127.0.0.1:5000/flutes' to url: '/flutes' so it correctly points to the route on PythonAnywhere.

**Step 8: Reload the App**

- In the Web tab, click the "Reload" button.
- Your app is now live.
***
## Notes About the Project

***

1. During this project, I tried both the Fetch API and jQuery’s AJAX to send data to the Flask backend. Both worked fine, but in the end, I switched all pages to use `$.ajax` to fit the project requirements. To make AJAX work, I added the jQuery CDN link in the `<head>` part of the HTML. Besides meeting the requirement, `$.ajax` also makes things easier with built-in JSON parsing and flexible error handling.

2. Since my project was stored in a directory within the wsaa-coursework repository, I found it easier to use a separate repository called deploypythonanywhere to download the project files to the PythonAnywhere website.

3. While working with files on PythonAnywhere, I found it easier to make changes directly on the website by double-clicking a file in the 'Files' tab and saving the edits afterward. This section of the site also provided a convenient way to upload individual files.

***
## References:

***
- [HTML - Using Cards](https://www.w3schools.com/howto/howto_css_cards.asp)
- [CSS & HTML](https://www.freecodecamp.org/news/how-to-link-css-to-html/)
- [Flask render_template](https://www.geeksforgeeks.org/flask-rendering-templates/)
- [Difference Between AJAX And Fetch API](https://www.geeksforgeeks.org/difference-between-ajax-and-fetch-api/)
- [ChatGPT](https://chatgpt.com/)

***
## _End_
