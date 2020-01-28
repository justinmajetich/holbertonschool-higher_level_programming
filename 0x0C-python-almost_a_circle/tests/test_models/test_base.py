#!/usr/bin/python3
"""This module contains unittests for the class Base"""


import unittest
import json
from os import path, remove
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseID(unittest.TestCase):
    """Class contains test of Base class's ID attribute."""

    def setUp(self):
        """Build test state"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Wipe test state"""

    def test_int_arg(self):
        """id init when int is passed"""
        obj = Base(9)
        self.assertTrue(obj.id is 9)

    def test_optional_arg(self):
        """Initialization value when no arg passed"""
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_id_type_none(self):
        """None passed as id"""
        obj = Base(None)
        self.assertTrue(obj.id is 1)

    def test_non_int_arg(self):
        """id init with str arg (improper but does not raise exception)"""
        obj = Base('id')
        self.assertTrue(obj.id is 'id')

    def test_nb_onjects_counter(self):
        """Counter doesn't increment when id given"""
        obj0 = Base()
        obj1 = Base(666)
        obj2 = Base()
        self.assertTrue(obj2.id is 2)

    def test_float_overflow(self):
        """Float overflow"""
        obj = Base(float('inf'))
        self.assertEqual(obj.id, float('inf'))

    def test_object_del(self):
        """obj counter preserved after deletion"""
        obj0 = Base()
        del obj0
        obj1 = Base()
        self.assertEqual(obj1.id, 2)

    def test_private_attr(self):
        """Private instance counter is present"""
        obj = Base()
        self.assertTrue('_Base__nb_objects' in Base.__dict__)


class TestBaseJSONToString(unittest.TestCase):
    """This class contains test of Base's JSON methods"""

    def setUp(self):
        """Build test state"""
        self.obj = Base()
        self.valid_ld = [{'id': 1, 'name': 'justin'}, {'id': 9, 'age': 9}]

    def tearDown(self):
        """Wipe test state"""
        del self.obj

    def test_valid_ld(self):
        """Method returns valid json string representation"""
        self.assertEqual(self.obj.to_json_string(self.valid_ld),
                         json.dumps(self.valid_ld))

    def test_return_type(self):
        """Method returns a string"""
        self.assertEqual(type(self.obj.to_json_string(self.valid_ld)), str)

    def test_non_list_of_dicts_arg(self):
        """Converts non-dictionary lists to JSON string"""
        self.assertEqual(self.obj.to_json_string(666), '666')

    def test_empty_list_of_dict_arg(self):
        """Converts list of empty dicts to JSON string"""
        self.assertEqual(self.obj.to_json_string([{}, {}]), '[{}, {}]')

    def test_none(self):
        """Prints an empty list for None"""
        self.assertEqual(self.obj.to_json_string(None), '[]')

    def test_empty_list(self):
        """Prints an empty list"""
        self.assertEqual(self.obj.to_json_string([]), '[]')

    def test_missing_arg(self):
        """Raises TypeError"""
        with self.assertRaises(TypeError):
            self.obj.to_json_string()


class TestBaseJSONToFile(unittest.TestCase):
    """This class contains test for Base's save_to_file method"""

    def setUp(self):
        """Build test state"""
        self.r0 = Rectangle(2, 3, 0, 0)
        self.r1 = Rectangle(4, 6)
        self.s0 = Square(9)
        self.s1 = Square(3, 1, 1)

    def test_file_created(self):
        """File is created"""
        Square.save_to_file([self.r0, self.r1])
        self.assertTrue(path.exists('Square.json'))

    def test_valid_file_name(self):
        """File has valid name"""
        Base.save_to_file([self.r0, self.s1])
        self.assertTrue(path.exists('Base.json'))

    def test_arg_is_none(self):
        """Empty list is written to file"""
        self.s0.save_to_file(None)
        with open('Square.json', mode='r', encoding='utf-8') as f:
            read = f.read()
        self.assertEqual(read, '[]')

    def test_list_of_one_obj(self):
        """Saves a simple obj representation to file"""
        with self.assertRaises(TypeError):
            self.s1.save_to_file(self.r1)

    def test_list_of_non_subclass_objs(self):
        """Saving non-subclass objects raises AttributeError"""
        with self.assertRaises(AttributeError):
            self.s1.save_to_file([88, 99])

    def test_missing_arg(self):
        """Missing argument raises TypeError"""
        with self.assertRaises(TypeError):
            self.r1.save_to_file()


class TestBaseJSONToDict(unittest.TestCase):
    """This class contains test for Base's from_json_string method"""

    def setUp(self):
        """Build test state"""
        self.d = [{'id': 99, 'name': 'joe'}, {'date': '042891'}]
        self.r0 = Rectangle(2, 3, 0, 0)
        self.s0 = Square(3, 1, 1)
        self.string = self.r0.to_json_string(self.d)

    def test_return_value(self):
        """Method returns correct values"""
        self.assertEqual(self.r0.from_json_string(self.string), self.d)

    def test_return_type(self):
        """Method returns correct type"""
        self.assertEqual(type(self.s0.from_json_string(self.string)), list)

    def test_non_list_arg(self):
        """Raises TypeError"""
        with self.assertRaises(TypeError):
            self.r0.from_json_string(666)

    def test_list_of_non_dicts(self):
        """"""
        with self.assertRaises(ValueError):
            self.s0.from_json_string('[66, \'66\']')

    def test_none_arg(self):
        """Returns empty list"""
        self.assertEqual(self.r0.from_json_string(None), [])

    def test_missing_arg(self):
        """Raises TypeError"""
        with self.assertRaises(TypeError):
            self.r0.from_json_string()


class TestBaseJSONFromFile(unittest.TestCase):
    """This class contains test for Base's load_from_file method"""

    def setUp(self):
        """Build test state"""
        Base._Base__nb_objects = 0
        self.r0 = Rectangle(2, 3, 0, 0)
        self.r1 = Rectangle(4, 6)
        self.s0 = Square(9)
        self.s1 = Square(3, 1, 1)

    def test_good_load(self):
        """Loads list of instances from file"""
        self.r0.save_to_file([self.r0, self.r1])
        objs = self.r0.load_from_file()
        self.assertEqual(str(objs[0]), '[Rectangle] (1) 0/0 - 2/3')
        self.assertEqual(str(objs[1]), '[Rectangle] (2) 0/0 - 4/6')

    def test_non_existent_file(self):
        """Returns an empty list"""
        remove('Rectangle.json')
        self.assertEqual(self.r1.load_from_file(), [])

    def test_type_of_loaded_sq_objs(self):
        """Loads file data into Square(s)"""
        self.s0.save_to_file([self.r0])
        objs = self.s1.load_from_file()
        self.assertEqual(type(objs[0]), Square)

    def test_type_of_loaded_rect_objs(self):
        """Loads file data into Rectangle(s)"""
        self.r0.save_to_file([self.s0, self.r1])
        objs = self.r1.load_from_file()
        self.assertEqual(type(objs[1]), Rectangle)

    def test_empty_file(self):
        """Empty file returns empty list"""
        with open('Rectangle.json', mode='w', encoding='utf-8') as f:
            f.write('')
        self.assertEqual(self.r1.load_from_file(), [])


class TestBaseCreate(unittest.TestCase):
    """This class contains tests for Base's create method"""

    def setUp(self):
        """Build test state"""
        Base._Base__nb_objects = 0
        self.r0 = Rectangle(2, 3, 0, 0)
        self.r1 = Rectangle(4, 6)
        self.s0 = Square(9)
        self.s1 = Square(3, 1, 1)

    def test_create_rectangle(self):
        """Returns initialized Rectangle instance"""
        d = self.r1.to_dictionary()
        r3 = Rectangle.create(**d)
        self.assertEqual(str(r3), str(self.r1))

    def test_create_square(self):
        """Returns initialized Square instance"""
        d = self.s1.to_dictionary()
        s3 = Square.create(**d)
        self.assertEqual(str(s3), str(self.s1))

    def test_missing_args(self):
        """Creates instance with dummy attributes"""
        s = Square.create()
        self.assertEqual(str(s), '[Square] (5) 0/0 - 1')

    def test_invalid_arg(self):
        """Raises TypeError"""
        with self.assertRaises(TypeError):
            s = Square.create(666)
