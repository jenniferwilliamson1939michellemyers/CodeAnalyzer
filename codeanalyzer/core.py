"""
Core code analysis functions
"""

import re
from typing import Dict, List, Tuple


def count_lines(content: str) -> Dict[str, int]:
    """
    Count lines in source code.
    
    Args:
        content: Source code content
        
    Returns:
        Dictionary with total, code, blank, and comment line counts
        
    Example:
        >>> count_lines("x = 1\\n\\n# comment\\ny = 2")
        {'total': 4, 'code': 2, 'blank': 1, 'comment': 1}
    """
    lines = content.split('\n')
    total = len(lines)
    blank = sum(1 for line in lines if not line.strip())
    comment = sum(1 for line in lines if line.strip().startswith('#'))
    code = total - blank - comment
    
    return {
        'total': total,
        'code': code,
        'blank': blank,
        'comment': comment
    }


def count_functions(content: str, language: str = "python") -> int:
    """
    Count function definitions in source code.
    
    Args:
        content: Source code content
        language: Programming language (python, javascript)
        
    Returns:
        Number of function definitions
        
    Example:
        >>> count_functions("def foo():\\n    pass\\ndef bar():\\n    pass")
        2
    """
    if language == "python":
        pattern = r'^\s*def\s+\w+\s*\('
    elif language == "javascript":
        pattern = r'function\s+\w+\s*\(|^\s*\w+\s*[=:]\s*(?:async\s+)?function|\w+\s*=\s*\([^)]*\)\s*=>'
    else:
        pattern = r'^\s*def\s+\w+\s*\('
    
    return len(re.findall(pattern, content, re.MULTILINE))


def analyze_imports(content: str) -> List[str]:
    """
    Extract import statements from Python code.
    
    Args:
        content: Python source code
        
    Returns:
        List of imported module names
        
    Example:
        >>> analyze_imports("import os\\nfrom sys import path")
        ['os', 'sys']
    """
    imports = set()
    
    # Match 'import xxx'
    for match in re.finditer(r'^import\s+([\w.]+)', content, re.MULTILINE):
        imports.add(match.group(1).split('.')[0])
    
    # Match 'from xxx import'
    for match in re.finditer(r'^from\s+([\w.]+)\s+import', content, re.MULTILINE):
        imports.add(match.group(1).split('.')[0])
    
    return sorted(list(imports))


def get_file_extension(filename: str) -> str:
    """
    Get file extension from filename.
    
    Args:
        filename: File name or path
        
    Returns:
        File extension (without dot), empty string if none
        
    Example:
        >>> get_file_extension("test.py")
        'py'
    """
    if '.' in filename:
        return filename.rsplit('.', 1)[-1].lower()
    return ''


def is_code_file(filename: str) -> bool:
    """
    Check if file is a source code file.
    
    Args:
        filename: File name or path
        
    Returns:
        True if it's a code file
        
    Example:
        >>> is_code_file("main.py")
        True
        >>> is_code_file("readme.txt")
        False
    """
    code_extensions = {'py', 'js', 'ts', 'java', 'c', 'cpp', 'go', 'rs', 'rb'}
    ext = get_file_extension(filename)
    return ext in code_extensions


def calculate_complexity(content: str) -> int:
    """
    Calculate cyclomatic complexity estimate.
    
    Args:
        content: Source code content
        
    Returns:
        Complexity score (higher = more complex)
        
    Example:
        >>> calculate_complexity("if x:\\n    pass")
        2
    """
    # Base complexity
    complexity = 1
    
    # Count decision points
    decision_keywords = ['if', 'elif', 'else', 'for', 'while', 'except', 'with', 'and', 'or']
    for keyword in decision_keywords:
        pattern = r'\b' + keyword + r'\b'
        complexity += len(re.findall(pattern, content))
    
    return complexity

