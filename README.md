# REBBIT

## Rebbits gives you the best of the internet in one place. Get a constantly updating feed of breaking news, fun stories, pics, memes, and videos just for you.

### March 11th, 2019

#### By **[Mugo Ndungu](https://github.com/mugo-ndungu)**

## Description

Rebbits gives you the best of the internet in one place. Get a constantly updating feed of breaking news, fun stories, pics, memes, and videos just for you to visit the site Click [here](https://) to see the live site

## Setup and installation

- Clone the Repo uding the following command:
  `git clone https://github.com/Mugo-Ndungu/rebbits.git
- Activate virtual environment using python3.6 as default handler by running
  `python3.6 -m venv virtual` then enter the virtual environment using `source virtual/bin/activate`
- Download the latest version of pip in the virtual environment: `$ curl https://bootstrap.pypa.io/get-pip.py | python`

- Install all application dependancies
  `pip install -r requirements.txt`

- Create the Database
  -On the terminal,run `psql`

  - Create a database by typing
    `CREATE DATABASE awards;` for example.

- Create a .env file and add the following:

  - SECRET_KEY = `<Secret_key>`
  - DB_NAME = `awards`
  - DB_USER = `<Username>`
  - DB_PASSWORD = `your db password`
  - DEBUG = `True`

- Run Initial Migration
  `python3.6 manage.py makemigrations <name of the app>`
  `python3.6 manage.py migrate`

- Run the app
  `python3.6 manage.py runserver`
  `Open terminal on localhost:8000`

## User Stories

The application user is able to:

- Create an account and confirm through email verification.
- Sign in to the application to start using.
- Post a project to be rated/reviewed
- View their profile with all their uploaded pictures.
- View posted projects and their details.
- Rate/ review other users' projects
- Search for projects
- View projects overall score
- View my profile page.

## Admin

The application admin is able to:

- Regulate images uploaded deleting them from the admin dashboard.
- Close a users account.

## Specifications

| Behavior                  | Input                          | Output                                 |
| ------------------------- | ------------------------------ | -------------------------------------- |
| Signup                    | string text                    | Creates user account                   |
| Login                     | string text                    | logs in to user account                |
| Submit new project post   | upload project                   | new project post from user               |
| Add comment to project post | String text                    | New comment to project post selected     |
| View posted project post    | Click on project post  | Display project posts in that    |
| View user project post      | Click on user profile          | Display project posts posted by the user |

## Technologies Used

- Python 3.6.6(Django Framework)
- HTML5
- CSS3
- Bootstrap4
- Postgresql
- Heroku(Deployment)
- Visual Studio Code text editor

## Known Bugs

No known bugs so far.Contact me if you come across any.

## Support and contact details

Contact me on [Email](twinnymugo@gmail.com) for any comments, reviews or advice.

### License

Copyright (c) **Mugo Ndungu**
