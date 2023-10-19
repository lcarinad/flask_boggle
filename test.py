from unittest import TestCase
from app import app, boggle_game
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):
    
    def setUp(self):
        with app.test_client() as client:
            self.client = app.test_client()
            app.config['TESTING'] = True
        
    def test_home_page(self):
        """makesure homePage loads and current game is an instance of the Boggle Game class"""
        with self.client as client:
            res = client.get("/")
            html = res.get_data(as_text=True)
    
            self.assertEqual(res.status_code, 200)
            self.assertIn('<button id="begin-btn">Begin Game</button>', html)
            self.assertIsInstance(boggle_game, Boggle)
            
    def test_session_board_set(self):
        """Test current board is saving in session"""
        with self.client() as client:
            res = client.get('/')
            self.assertIn('current_board', session)
            self.assertTrue(session['current_board'])
            self.assertIsInstance(session['current_board'], list)
            
    def test_word_validity(self):  
        """Test is word is valid by changing board session"""                             
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['board'] = [['D', 'O', 'G', 'P', 'Z'], ['I', 'R', 'V', 'S', 'N'], ['F', 'E', 'U', 'V', 'L'], ['Z', 'H', 'X', 'V', 'H'], ['M', 'N', 'P', 'J', 'M']]
                res = self.client.post('/word', json={'guess':'DOG'})
                data = res.get_json
                # self.assertEqual(res.status_code,200)
    #             # ⁉️ in server i am receiving 200 code but in test i'm receiving 415
                self.assertEqual(data.result, 'ok')
                
                res = client.post('/word', json = {'guess': 'alert'})
                self.assertEqual(data['result'], 'not-on-board')
                
                res = client.post('/word', json = {'guess': 'abcde'})
                self.assertEqual(data['result'], 'not-word')
                 # ⁉️ confused why test is failing bc it works in application.  i saw in response body in js console, content header type is json so i'm using json in test
                 
    def test_end_of_game(self):
        with app.test_client() as client:
            res  = client.post('/end', data = "score")
            self.assertIn('player_scores', session)
            
    def test_redirection(self):
        with app.test_client() as client:
            res = client.post('/redirect-me')
            self.assertEqual(res.status_code, 302)