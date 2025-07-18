"""
astminijava.py

Este arquivo deve conter a definição das classes que representam a Árvore de Sintaxe Abstrata (AST)
para o subconjunto da linguagem MiniJava definido na Atividade da disciplina IF688.
"""

from typing import List, Optional

class ASTNode:
    """classe base para todos os nós da AST"""
    pass

class Program(ASTNode):
    """representa um programa completo: MainClass + Classes adicionais"""
    def __init__(self, main_class: 'MainClass', classes: List['ClassDecl']):
        self.main_class = main_class
        self.classes = classes

class MainClass(ASTNode):
    """representa a classe principal com método main"""
    def __init__(self, name: str):
        self.name = name

class ClassDecl(ASTNode):
    """representa uma declaração de classe"""
    def __init__(self, name: str, parent_class: Optional[str] = None, 
                 vars: List['VarDecl'] = None, methods: List['MethodDecl'] = None,
                 static_vars: List['VarDecl'] = None):
        self.name = name
        self.parent_class = parent_class  # para herança 
        self.vars = vars or []  # variáveis de instância
        self.static_vars = static_vars or []  # variáveis estáticas
        self.methods = methods or []  # métodos da classe

class VarDecl(ASTNode):
    """representa uma declaração de variável"""
    def __init__(self, type: 'Type', name: str):
        self.type = type
        self.name = name

class MethodDecl(ASTNode):
    """representa uma declaração de método"""
    def __init__(self, return_type: 'Type', name: str, parameters: List['Parameter'] = None):
        self.return_type = return_type
        self.name = name
        self.parameters = parameters or []

class Parameter(ASTNode):
    """representa um parâmetro de método"""
    def __init__(self, type: 'Type', name: str):
        self.type = type
        self.name = name

class Type(ASTNode):
    """representa um tipo (primitivo ou array)"""
    def __init__(self, base_type: str, array_dimensions: int = 0):
        self.base_type = base_type  # "int", "boolean", "float", ou nome de classe
        self.array_dimensions = array_dimensions  # 0 = não é array, 1 = [], 2 = [][], etc.
    
    def __str__(self):
        if self.array_dimensions == 0:
            return self.base_type
        else:
            return self.base_type + "[]" * self.array_dimensions
