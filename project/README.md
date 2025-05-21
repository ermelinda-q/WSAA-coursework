# README - WSAA Project

### Author: E.Qejvani


## Title: Concert Flute Database

This is my web application for managing a database of concert flutes. Built with Flask (Python), HTML/CSS/JavaScript/AJAX, and MySQL. This app allows users to view, add, delete, and manage flute records via a web interface.

---

## Features

- Index file - main file
- View all flutes stored in the database
- Add new flutes with detailed information
- Delete flutes by ID
- Find flutes by ID
- Update information (based on flute ID)
- RESTful API endpoints for backend communication

---

## Technologies Used

- **Backend:** Flask (Python), MySQL
- **Frontend:** HTML, CSS, jQuery (AJAX)
- **Hosting:** PythonAnywhere

---

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

1. From data folder run

### Local:

1. Clone the Repository

    ``` https://github.com/ermelinda-q/WSAA-coursework/tree/main/project ```

2. Create a Virtual Environment




## References:

- [HTML - Using Cards](https://www.w3schools.com/howto/howto_css_cards.asp)
- [CSS & HTML](https://www.freecodecamp.org/news/how-to-link-css-to-html/)
- [Flask render_template](https://www.geeksforgeeks.org/flask-rendering-templates/)
- 
