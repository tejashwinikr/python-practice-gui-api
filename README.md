# My Python Project

This is a simple Python project.

## Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment
4. Install dependencies: `pip install -r requirements.txt`

## Usage

Run the main script:

```sh
python src/main.py

<html>

<head>
    <title>Tejaswini</title>

</head>

<body>
    <style>
        h1 {
            display: inline;
            align-self: center;
        }

        #content {
            display: block;
            color: orange;
            align-items: center;
        }

        .bio {
            color: blue;
            display: flex;
            flex-direction: column;
            background-color: beige;
            align-items: center;
        }

        .my-pic{
            height: 50%;
        }

        .personal-details {
            background-color: bisque;
            /* Set display to flex */
            display: flex;
            /* Center content horizontally */
            justify-content: center;
            /* Center content vertically */
            align-items: center;
            width: 100%;
        }

        .personal-details-table table {
            border-collapse: collapse;
            width: 100%;
        }

        .personal-details-table th {
            border: 1px solid black;
            background-color: brown;
            padding: 4px;
        }

        .personal-details-table td {
            border: 1px solid black;
            color: blueviolet;
            padding: 4px;
        }

        .form-container {
            align-self: center;
            padding: 10px;
            margin: 10px;
        }
    </style>

    <script>
        function changeContent() {
            document.getElementById("content").innerHTML = "Paragraph changed."
        }

        function loginbutton() {
            const usernameField = document.querySelector('input[type="text"]');
            const passwordField = document.querySelector('input[type="password"]');

            // Get the values of the username and password fields.
            const username = usernameField.value;
            const password = passwordField.value;
            alert("login clicked", username, password)
        }
    </script>

    <h1 id="content">Thejashwini K R</h1>
    <!-- <button onclick="changeContent()"> click me </button>
<div classname="form-container">
    <form>
        <label> Username </label>
        <br>
        <input type="text"></input>
        <br>
        <label> password </label>
        <br>
        <input type="password"></input>

        <br>
        <button onclick="loginbutton()">Login</button>
        <br>
        <button>Signup</button>
        </form>
</div> -->

    <div class="bio">
        <span>Ambivert</span>
        <span>Live and let Live</span>
        <span>We all die one day!!!</span>
    </div>

    <div class="personal-details">
        <div  class="my-pic">
            <img src=""
            alt="my_pic"/>
        </div>
       
        <table class="personal-details-table">
            <tr>
                <th>About </th>
                <th>Info</th>
            </tr>
            <tr>
                <td>DOB </td>
                <td>Dec 22,2000</td>
            </tr>
            <tr>
                <td>Education </td>
                <td>B.E</td>
            </tr>
            <tr>
                <td>Occupation </td>
                <td>Software Engineer</td>
            </tr>
            <tr>
                <td>Salary Range</td>
                <td>5L -6L</td>
            </tr>
            <tr>
                <td>Zodiac and star</td>
                <td>Thula(Libra) and vishaka</td>
            </tr>
        </table>
    </div>

    <div>

    </div>
   
</body>

</html>
