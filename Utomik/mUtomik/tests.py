from django.test import TestCase
from .models import Game, PlaySession, User
from .serializer import *
import unittest
from django.test import Client
import json


class UserTestCase(TestCase):
    def test_users(self):
        invalid_user = UserSerializer(data={"username": "omendra"})
        self.assertEqual(invalid_user.is_valid(), False)
        valid_user = UserSerializer(data={"username": "omendra", "birth_date": "1990-10-10", "password": "adgjmp", "email": "m@gmail.com" })
        self.assertEqual(valid_user.is_valid(), True)
        

class ApiTest(TestCase):
    def test_games(self):
        print("Fetch games")
        client = Client()
        response = client.get('/games/')
        self.assertEqual(response.status_code, 200)

    def test_user_create(self):
        print("Create User")
        user = {
            "username": "xyz",
            "password": "adgjmp",
            "email": "m@email.com",
            "birth_date": "1990-10-10",
            "is_staff": True
        }
        client  = Client()
        response = client.post(
            '/users/', 
            json.dumps(user),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)

    def test_user_fetch(self):
        print("Fetch users test")
        client  = Client()
        response = client.get(
            '/users/',
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 401)

    def test_user_fetch_non_staff(self):
        print("Fetch users Test with Auth")
        client  = Client()
        user = {
            "username": "xyz",
            "password": "adgjmp",
            "email": "m@email.com",
            "birth_date": "1990-10-10"
        }
        client  = Client()
        client.post(
            '/users/', 
            json.dumps(user),
            content_type="application/json"
        )

        print("Get Token")
        response = client.post(
            '/login/',
            json.dumps(user),
            content_type="application/json"
        )
        token = response.data['access']
        fetchuser = client.get(
            '/users/',
            content_type="application/json",
            HTTP_AUTHORIZATION='Bearer ' + token
        )
        
        self.assertEqual(fetchuser.status_code, 403)
        self.assertEqual(fetchuser.data['detail'].code, 'permission_denied')
        print("Permission Denied")
    
    def test_user_fetch_staff(self):
        print("Fetch users Test with Staff Auth")
        client  = Client()
        user = User.objects.create_user(username='om', email='e@e.com', birth_date='1990-10-10')
        user.is_staff=True 
        user.set_password('adgjmp')
        user.save()
        client  = Client()
        response = client.post(
            '/login/',
            json.dumps({
                "username":"om",
                "password" : "adgjmp"
            }),
            content_type="application/json"
        )
        token = response.data['access']
        fetchuser = client.get(
            '/users/',
            content_type="application/json",
            HTTP_AUTHORIZATION='Bearer ' + token
        )
        self.assertEqual(fetchuser.status_code, 200)

    def test_playsession(self):
        print("create play session")
        client  = Client()
        user = User.objects.create_user(username='om', email='e@e.com', birth_date='1990-10-10')
        user.set_password('adgjmp')
        user.save()
        
        client  = Client()
        response = client.post(
            '/login/',
            json.dumps({
                "username":"om",
                "password" : "adgjmp"
            }),
            content_type="application/json"
        )
        token = response.data['access']
        playsession = client.post(
            '/playsessions/',
            json.dumps({
                "game":1
            }),
            content_type="application/json",
            HTTP_AUTHORIZATION='Bearer ' + token
        )
        self.assertEqual(playsession.status_code, 201)
        print(playsession.status_code)

    def test_last_game_fetch_staff(self):
        client  = Client()
        user = User.objects.create_user(username='om', email='e@e.com', birth_date='1990-10-10')
        user.is_staff=True 
        user.set_password('adgjmp')
        user.save()
        
        client  = Client()
        response = client.post(
            '/login/',
            json.dumps({
                "username":"om",
                "password" : "adgjmp"
            }),
            content_type="application/json"
        )
        token = response.data['access']
        fetchuser = client.get(
            '/users/lastplayed',
            content_type="application/json",
            HTTP_AUTHORIZATION='Bearer ' + token
        )
        self.assertEqual(fetchuser.status_code, 200)
        print("Fetch users Last Game : ", fetchuser.status_code)

    def test_last_game_non_staff(self):
        client  = Client()
        user = User.objects.create_user(username='om', email='e@e.com', birth_date='1990-10-10')
        user.set_password('adgjmp')
        user.save()
        
        client  = Client()
        response = client.post(
            '/login/',
            json.dumps({
                "username":"om",
                "password" : "adgjmp"
            }),
            content_type="application/json"
        )
        token = response.data['access']
        fetchuser = client.get(
            '/users/lastplayed',
            content_type="application/json",
            HTTP_AUTHORIZATION='Bearer ' + token
        )
        self.assertEqual(fetchuser.status_code, 403)
        print("Fetch users Last Game : ", fetchuser.status_code)

    def test_avatar(self):
        
        client  = Client()
        user = User.objects.create_user(username='om', email='e@e.com', birth_date='1990-10-10')
        user.set_password('adgjmp')
        user.save()
        
        client  = Client()
        response = client.post(
            '/login/',
            json.dumps({
                "username":"om",
                "password" : "adgjmp"
            }),
            content_type="application/json"
        )
        token = response.data['access']

        fetch_avtar = client.get('/users/avatar/',
            content_type="application/json",
            HTTP_AUTHORIZATION='Bearer ' + token
        )
        
        self.assertEqual(fetch_avtar.status_code, 400)
        print("Fetch Non existent Avtar : ", fetch_avtar.status_code)