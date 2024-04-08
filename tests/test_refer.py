import unittest
from unittest.mock import Mock, patch
from sqlalchemy.exc import SQLAlchemyError
import fastapi as _fastapi

import os
import sys

directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(directory)

import refers 

class TestReferModule(unittest.TestCase):
    @patch('refers.Session')
    def test_get_user_info(self, mock_session):
        mock_user = Mock()
        mock_user.email = 'nitesh342@gmail.com'
        mock_session.query().filter().first.return_value = mock_user

        result = refers.get_user_info('nitesh342@gmail.com')

        self.assertEqual(result, mock_user)

    @patch('refers.Session')
    def test_get_user_info_not_found(self, mock_session):
        mock_session.query().filter().first.return_value = None

        with self.assertRaises(_fastapi.HTTPException):
            refers.get_user_info('nitesh342@gmail.com')

    @patch('refers.get_user_info')
    @patch('refers.Session')
    def test_get_refer_info(self, mock_session, mock_get_user_info):
        mock_user = Mock()
        mock_user.referral_id = 'HEWnBSTq'
        mock_get_user_info.return_value = mock_user
        mock_session.query().filter().all.return_value = [mock_user]

        result = refers.get_refer_info('nitesh342@gmail.com')

        self.assertEqual(result, [mock_user])

if __name__ == '__main__':
    unittest.main()
