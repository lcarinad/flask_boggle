from unittest import TestCase
from app import app, boggle_game
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

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
            
    