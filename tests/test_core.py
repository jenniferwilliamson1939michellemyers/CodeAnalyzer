"""
Tests for core code analysis functions
"""

import unittest
from codeanalyzer import (
    count_lines,
    count_functions,
    analyze_imports,
    get_file_extension,
    is_code_file,
    calculate_complexity
)


class TestCountLines(unittest.TestCase):
    def test_simple_code(self):
        result = count_lines("x = 1\ny = 2")
        self.assertEqual(result['total'], 2)
        self.assertEqual(result['code'], 2)
    
    def test_with_blanks(self):
        result = count_lines("x = 1\n\ny = 2")
        self.assertEqual(result['blank'], 1)
    
    def test_with_comments(self):
        result = count_lines("# comment\nx = 1")
        self.assertEqual(result['comment'], 1)


class TestCountFunctions(unittest.TestCase):
    def test_python_functions(self):
        code = "def foo():\n    pass\ndef bar():\n    pass"
        self.assertEqual(count_functions(code), 2)
    
    def test_no_functions(self):
        code = "x = 1\ny = 2"
        self.assertEqual(count_functions(code), 0)


class TestAnalyzeImports(unittest.TestCase):
    def test_import_statement(self):
        result = analyze_imports("import os")
        self.assertIn('os', result)
    
    def test_from_import(self):
        result = analyze_imports("from sys import path")
        self.assertIn('sys', result)


class TestGetFileExtension(unittest.TestCase):
    def test_python_file(self):
        self.assertEqual(get_file_extension("test.py"), "py")
    
    def test_no_extension(self):
        self.assertEqual(get_file_extension("Makefile"), "")


class TestIsCodeFile(unittest.TestCase):
    def test_python_file(self):
        self.assertTrue(is_code_file("main.py"))
    
    def test_text_file(self):
        self.assertFalse(is_code_file("readme.txt"))


class TestCalculateComplexity(unittest.TestCase):
    def test_simple_code(self):
        result = calculate_complexity("x = 1")
        self.assertEqual(result, 1)
    
    def test_with_if(self):
        result = calculate_complexity("if x:\n    pass")
        self.assertGreater(result, 1)


if __name__ == "__main__":
    unittest.main()

