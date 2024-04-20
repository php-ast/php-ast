from php_ast import php_ast

php=php_ast()
ast=php.get_ast(b"<?php7 echo 'Hello World';")
print(ast)
ast=php.get_ast(b"<?php7 echo 'Hello World';")
print(ast)
