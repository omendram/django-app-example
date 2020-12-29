
## Setting up mUtomik Server

- `Vagrantfile` contains the details and exposes the application at "127.0.0.1:8080"
- `vagrant reload` to migrate and install all the necessary pre-requisites
- `vagrant provision` to migrate and install all the necessary pre-requisites (Adds migration and initial data)


## About mUtomik

- `User.json` and `Game.json` contains the initial load_data

### Default Staff User

- `username`: `admin` and `password`: `1234`
Note: They are differentiated by `is_staff`: `True`  property.

### Default Regustered User

- `username`: `omendram` and `password`: `adgjmp`

### APIS

#### Login and get Token
    POST 'login/' 
    POST 'login/refresh'

### Register New User
    POST 'users/'

### Get Users (only Staff)
    GET 'users/'

### Get Last Played (only Staff)
    GET 'users/lastplayed'

### Get games
    GET 'games/'
    GET 'games/<id>'
### Create play session (authenticated registered users only)
    POST 'playsessions/'

### Upload Avatar (authenticated registered users only)
    GET 'users/avatar/'
    POST 'users/avatar/'

## Log-in

- Get JWT token
POST /login/  {username: , password: }

- Use token response from above call to make authenticated requests
GET /url {Authorization: Bearer <token>}

## Tests

The tests are mentioned at: `app/tests.py`