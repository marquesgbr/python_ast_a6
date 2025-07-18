"""
astminijava.py

Este arquivo deve conter a definição das classes que representam a Árvore de Sintaxe Abstrata (AST)
para o subconjunto da linguagem MiniJava definido na Atividade da disciplina IF688.
"""

from typing import List, Optional

class ASTNode:
    pass

# Exemplo de início de modelagem:
class Program(ASTNode):
    def __init__(self, main_class, classes: List['ClassDecl']):
        self.main_class = main_class
        self.classes = classes

class MainClass(ASTNode):
    def __init__(self, name: str):
        self.name = name

# Continue a modelagem com outras classes da gramática...
