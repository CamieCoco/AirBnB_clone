#!/usr/bin/python3

import unittest
import os
import pep8
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rev1 = Review()
        cls.rev1.place_id = "Raleigh"
        cls.rev1.user_id = "Greg"
        cls.rev1.text = "Grade A"

    @classmethod
    def tearDownClass(cls):
        del cls.rev1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.rev1._class_, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(Review._doc_)

    def test_has_attributes(self):
        self.assertTrue('id' in self.rev1._dict_)
        self.assertTrue('created_at' in self.rev1._dict_)
        self.assertTrue('updated_at' in self.rev1._dict_)
        self.assertTrue('place_id' in self.rev1._dict_)
        self.assertTrue('text' in self.rev1._dict_)
        self.assertTrue('user_id' in self.rev1._dict_)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.rev1.text), str)
        self.assertEqual(type(self.rev1.place_id), str)
        self.assertEqual(type(self.rev1.user_id), str)

    def test_save(self):
        self.rev1.save()
        self.assertNotEqual(self.rev1.created_at, self.rev1.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.rev1), True)


if _name_ == "_main_":
    unittest.main()
