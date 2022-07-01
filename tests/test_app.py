import unittest
import os

os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_home(self):
        # homepage tests
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        assert "<link rel='icon' href='./static/img/favicon.ico' type='image/x-icon' />" in html

    def test_timeline(self):
        # GET and POST requests tests
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        response = self.client.post('/api/timeline_post', 
            data = {
                "name":"Peter Griffin", 
                "email":"test@gmail.com",
                "content": "Test content"    
            }
        )

        assert response.status_code == 200
        assert response.is_json

        json = response.get_json()
        assert json["name"] == "Peter Griffin"

        response = self.client.get('/api/timeline_post')
        json = response.get_json()
        assert "Peter Griffin" == json["timeline_posts"][0]["name"]

        #additional timeline page tests
        response = self.client.get("/timeline")
        response_text  = response.get_data(as_text=True)
        assert "<form id=\"form\">" in response_text 

    def test_malformed_timeline_post(self):
        # Invalid Posts tests
        response = self.client.post('/api/timeline_post',
            data= {
                "email":"john@example.com", 
                "content":"Hello world, I'm John"
            }
        )
        
        assert response.status_code == 400
        response_text  = response.get_data(as_text=True)
        assert "Invalid name" in response_text 

        response = self.client.post('/api/timeline_post',
            data= {
                "name":"John Doe",
                "email":"john@example.com",
                "content": "" 
            }
        )

        assert response.status_code == 400
        response_text  = response.get_data(as_text=True)
        assert "Invalid content" in response_text 

        response = self.client.post('/api/timeline_post',
            data= {
                "name":"John Doe",
                "email":"not-an-email",
                "content":"Hello world, I'm John"
            }
        )

        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html