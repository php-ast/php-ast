<h1 align="center">Python Get PHP-AST </h1>

<div align="center">

[![PHP-AST](https://img.shields.io/badge/php-ast-blue)](https://github.com/php-ast/php_ast)
[![PHP](https://img.shields.io/badge/python_module-blue)](https://github.com/php-ast/php_ast)
[![version](https://img.shields.io/github/v/release/php-ast/php_ast.svg?color=blue)](https://github.com/php-ast/php_ast)
[![social](https://img.shields.io/github/stars/php-ast/php_ast?style=social)](https://github.com/php-ast/php_ast)
</div>
<p align="center">
</p>

## Install 
```bash
pip install  php-ast
```
- [php-ast](https://pypi.org/project/php-ast/)



## exapme 
```Python
# get bytes php code ast
from php_ast import php_ast
php_ast=php_ast()
php_ast.get_ast(b"<?php phpinfo();?>")
{'status': 'successed', 'ast': {'kind': 'AST_STMT_LIST', 'flags': 0, 'lineno': 1, 'children': [{'kind': 'AST_CALL', 'flags': 0, 'lineno': 1, 'children': {'expr': {'kind': 'AST_NAME', 'flags': 1, 'lineno': 1, 'children': {'name': 'phpinfo'}}, 'args': {'kind': 'AST_ARG_LIST', 'flags': 0, 'lineno': 1, 'children': []}}}]}}



# get php file ast
from php_ast import php_ast
php_ast=php_ast()
php_ast.get_file_ast("/home/11.php")
{'status': 'successed', 'ast': {'kind': 'AST_STMT_LIST', 'flags': 0, 'lineno': 1, 'children': [{'kind': 'AST_CALL', 'flags': 0, 'lineno': 1, 'children': {'expr': {'kind': 'AST_NAME', 'flags': 1, 'lineno': 1, 'children': {'name': 'phpinfo'}}, 'args': {'kind': 'AST_ARG_LIST', 'flags': 0, 'lineno': 1, 'children': []}}}]}}

```

## 说明
- 本项目是基于php-ast扩展的python模块，用于获取php代码的ast树
- 暂时只支持Linux 系统 


## 参考:
- [php-ast](https://github.com/nikic/php-ast)




