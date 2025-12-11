# CodeAnalyzer

一个简单的代码分析工具库，提供代码统计、复杂度分析和质量检测功能。

## Features

- 代码行数统计（count_lines）- 统计总行数、代码行、空行和注释行
- 函数数量统计（count_functions）- 统计代码中的函数定义数量
- 导入分析（analyze_imports）- 提取 Python 代码中的导入模块
- 文件类型识别（is_code_file）- 判断文件是否为代码文件
- 复杂度计算（calculate_complexity）- 估算代码的圈复杂度

## Installation

### 从源码安装

```bash
git clone https://github.com/mcpmark-test-xjtu/CodeAnalyzer.git
cd CodeAnalyzer
pip install -e .
```

## Usage

### 示例 1：统计代码行数

```python
from codeanalyzer import count_lines

code = """
def hello():
    # This is a comment
    print("Hello")
"""

result = count_lines(code)
print(result)  # {'total': 5, 'code': 2, 'blank': 1, 'comment': 1}
```

### 示例 2：分析导入

```python
from codeanalyzer import analyze_imports

code = """
import os
from sys import path
import json
"""

imports = analyze_imports(code)
print(imports)  # ['json', 'os', 'sys']
```

### 示例 3：计算复杂度

```python
from codeanalyzer import calculate_complexity

code = """
def check(x):
    if x > 0:
        return True
    elif x < 0:
        return False
    else:
        return None
"""

complexity = calculate_complexity(code)
print(f"Complexity: {complexity}")
```

## API Reference

### count_lines(content)
统计源代码行数，返回包含总行数、代码行、空行和注释行的字典。

### count_functions(content, language="python")
统计函数定义数量，支持 Python 和 JavaScript。

### analyze_imports(content)
提取 Python 代码中的导入模块名称。

### is_code_file(filename)
判断文件是否为代码文件（根据扩展名）。

### calculate_complexity(content)
估算代码的圈复杂度。

## Contributing

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与项目。

## License

MIT License - 详见 [LICENSE](LICENSE) 文件

