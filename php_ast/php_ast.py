# coding: utf-8
# github: https://github.com/php-ast/php-ast
# author: php_ast
# version: 1.0
# time 2024-04-20

from ctypes import cdll, c_int, POINTER, c_void_p
import os, io
import time, sys, json

stdin_r, stdin_w = os.pipe()
stdout_r, stdout_w = os.pipe()

class php_ast:
    __is_init = False
    def php_init(self,version="7"):
        '''初始化PHP运行时环境'''
        #获取当前的目录
        current_path = os.path.dirname(os.path.abspath(__file__))
        if version =="5" or version == "7":
            self.lib = cdll.LoadLibrary(current_path+"/libphp7.so")
        elif version == "8":
            self.lib = cdll.LoadLibrary(current_path+"/libphp8.so")
        else:
            raise Exception("Cannot find the php7 version")
        self.lib.init.argtypes = [c_void_p, c_void_p]
        self.lib.init.restype = c_int
        self.lib.execute.argtypes = []
        self.lib.execute.restype = c_int
        result = self.lib.init(stdin_r, stdout_w)
        if result != 0:
            raise Exception("Cannot initialize PHP runtime")
        result = self.lib.execute()
        if result != 0:
            raise Exception("Cannot start PHP runtime")


    def get_ast(self, src,version="7"):
        if not self.__is_init:
            self.php_init(version)
            self.__is_init = True
        '''通过管道与PHP运行时通信'''
        os.write(stdin_w, f"{len(src)}\n".encode())
        os.write(stdin_w, src)
        # 读取响应长度
        data_len_bytes = b""
        while not data_len_bytes.endswith(b"\n"):
            chunk = os.read(stdout_r, 1)  # 逐字节读取
            if not chunk:
                break  # 如果读到 EOF，则退出
            data_len_bytes += chunk
        data_len_str = data_len_bytes.decode().strip()

        if not data_len_str.isdigit():
            return {"status": "success", "ast": {}}  # 返回空的AST
        data_len = int(data_len_str)
        data_bytes = os.read(stdout_r, data_len)
        data_str = data_bytes.decode().strip()
        try:
            data = json.loads(data_str)
        except:
            data = {"status": "success", "ast": {}}
        return data

    def get_file_ast(self, file_path):
        '''通过文件获取AST'''
        with open(file_path, 'rb') as f:
            src = f.read()
        return self.get_ast(src)

    # 追踪AST
    def trace_ast(self, ast):
        '''追踪AST'''
        if ast is None:
            return
        if type(ast) is not dict:
            return
        if 'kind' in ast:
            print("kind:", ast['kind'])

        for k, v in ast.items():
            if k == 'children' and type(v) is dict:
                for i in v:
                    self.trace_ast(v[i])
            elif k == 'children' and type(v) is list:
                for i in v:
                    self.trace_ast(i)
            else:
                self.trace_ast(v)
