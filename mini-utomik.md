# Utomik Backend Assignment

## Introduction

As you probably can imagine, the Utomik web services contain a lot of functionality which is used by any of our customers. Functionality differs from getting a simple list of available game genres to a call which returns a list of recommended games for a specific user.

## Assignment

Lets create a mUtomik ("mini" Utomik), which only provides the bare essentials needed to play a game. In the mUtomik service a user can register an account, request a list of games and create a playsession (which is used to check how often a specific game is played).

### Functional requirements

If we look at the functionality we need, the following services are required:

- A person must be able to register
  - at least, an email, password, username and birthdate must be provided
  - email and password must be validated
  - a person must be 18 years or older to register
- Staff must be able to request all users
  - Staff should be able to request a list of all users
  - Staff should be able to request a list of all users and their last played game
- A list of games and a specific game must be able to be requested by anyone
  - a game must at least contain a name and a genre (separate model)
- A registered user must be able to create a playsession for a game
  - a playsession must at least store the combination of the user id plus the game id and should also store the time of creation
  - creating a playsession must be restricted to registered users only
- A registered user must be able to log in and make authenticated requests

### Technical requirements

The following endpoints must be available:

- POST /users (create a user) [open to everyone]
- GET /users (list of users) [restricted to staff]
- GET /users/lastplayed (list of users and their last played game) [restricted to staff]
- GET /games (get a listing of games) [open to everyone]
- GET /games/{id} (get a specific game by its id) [open to everyone]
- POST /playsessions (create a playsession) [restricted to authenticated registered users only]

Authentication & Authorization:

- For authentication and authorization, [JWT](https://jwt.io/) must be used
- Endpoints needed for this must be added

Development environment:

- The project should be setup inside a [vagrant](https://www.vagrantup.com/) environment.
- The project should use the latest version of [Python](https://www.python.org/)
- The project should use [Django](https://docs.djangoproject.com/en/3.0/) and [Django Rest Framework](https://www.django-rest-framework.org/)

Furthermore:

- Your application must use correct [HTTP codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes), for both successful and unsuccessful requests.
- The data must be stored in an [SQLite](https://www.sqlite.org/) database and must use proper keys/indexes where needed.
- Input and Output should be in [JSON format](http://json.org/example.html). Do *NOT* use Django [templates](https://docs.djangoproject.com/en/3.0/topics/templates/) or Django Rest Framework [browsable api](https://www.django-rest-framework.org/topics/browsable-api/).

BONUS:

- Avatar: Add support for users to upload an avatar
- Tests: Functionality needs to be covered in tests

## Other requirements

- The requirements marked with "BONUS" are optional and not *required* but implementing them might be beneficial.
- You need to write a README file, explaining how to use the application
- The assignment needs to be done and delivered within a week of receiving it, but we believe that the assignment should be finishable within a couple of days, depending on familiarity and skill level.
- The project needs to delivered in a .zip file.
- If you need a time extension, or the deadline isn't convenient for you, let us know *before* the deadline passes.
- Feel free to add or extend functionality where you think this may be beneficial.
