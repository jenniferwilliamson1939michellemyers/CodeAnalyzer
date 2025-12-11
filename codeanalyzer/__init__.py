"""
CodeAnalyzer - 代码分析工具库

提供代码统计、复杂度分析和质量检测功能
"""

__version__ = "0.1.0"
__author__ = "CodeAnalyzer Team"

from .core import (
    count_lines,
    count_functions,
    analyze_imports,
    get_file_extension,
    is_code_file,
    calculate_complexity
)

__all__ = [
    "count_lines",
    "count_functions",
    "analyze_imports",
    "get_file_extension",
    "is_code_file",
    "calculate_complexity"
]

