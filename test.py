from unittest import TestCase
from app import app, boggle_game
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):
    def setUp(self):
        with app.test_client() as client:
            client.get('/')
    # def tearDown(self):
    #     with app.test_client() as client:
    #         session.clear()
        
    def test_home_page_load(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)
        
            self.assertEqual(res.status_code, 200)
            self.assertIn('<button id="begin-btn">Begin Game</button>', html)
            self.assertIsInstance(boggle_game, Boggle)
            
    def test_session_board_set(self):
        with app.test_client() as client:
            res = client.get('/')
            self.assertIn('current_board', session)
            self.assertTrue(session['current_board'])
            self.assertIsInstance(session['current_board'], list)
            
    def test_word_post_request(self):                               
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['current_board'] = [['D', 'O', 'G', 'P', 'Z'], ['I', 'R', 'V', 'S', 'N'], ['F', 'E', 'U', 'V', 'L'], ['Z', 'H', 'X', 'V', 'H'], ['M', 'N', 'P', 'J', 'M']]
                res = client.post('/word', json = {'guess': 'dog'})
                data = res.get_json
                self.assertEqual(res.status_code,200)
                # ⁉️ in server i am receiving 200 code but in test i'm receiving 415
                self.assertEqual(data['result'], 'ok')
                
                res = client.post('/word', json = {'guess': 'alert'})
                self.assertEqual(data['result'], 'not-on-board')
                
                res = client.post('/word', json = {'guess': 'abcde'})
                self.assertEqual(data['result'], 'not-word')
                 # ⁉️ confused why test is failing bc it works in application.  i saw in response body in js console, content header type is json so i'm using json in test
                 
  