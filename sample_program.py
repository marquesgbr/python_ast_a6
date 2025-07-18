"""
sample_program.py

Este arquivo deve conter a criação manual de uma instância da AST
para o programa MiniJava de exemplo fornecido no enunciado da atividade.

Programa exemplo:
class Main {
    public static void main(String[] a) {
        System.out.println();
    }
}

class Point {
    int x;
    int y;
}
"""

from astminijava import *

# Criando a AST para o programa exemplo
program = Program(
    main_class=MainClass("Main"),
    classes=[
        ClassDecl(
            name="Point",
            vars=[
                VarDecl(Type("int"), "x"),
                VarDecl(Type("int"), "y")
            ]
        )
    ]
)


def print_ast(node, indent=0):
    """função para visualizar a estrutura da AST"""
    prefix = "  " * indent
    
    if isinstance(node, Program):
        print(f"{prefix}Program:")
        print(f"{prefix}  MainClass:")
        print_ast(node.main_class, indent + 2)
        if node.classes:
            print(f"{prefix}  Classes:")
            for cls in node.classes:
                print_ast(cls, indent + 2)
    
    elif isinstance(node, MainClass):
        print(f"{prefix}MainClass(name='{node.name}')")
    
    elif isinstance(node, ClassDecl):
        print(f"{prefix}ClassDecl(name='{node.name}'")
        if node.parent_class:
            print(f"{prefix}  extends: {node.parent_class}")
        if node.static_vars:
            print(f"{prefix}  static_vars:")
            for var in node.static_vars:
                print_ast(var, indent + 2)
        if node.vars:
            print(f"{prefix}  vars:")
            for var in node.vars:
                print_ast(var, indent + 2)
        if node.methods:
            print(f"{prefix}  methods:")
            for method in node.methods:
                print_ast(method, indent + 2)
        print(f"{prefix})")
    
    elif isinstance(node, VarDecl):
        print(f"{prefix}VarDecl(type={node.type}, name='{node.name}')")
    
    elif isinstance(node, MethodDecl):
        print(f"{prefix}MethodDecl(return_type={node.return_type}, name='{node.name}'")
        if node.parameters:
            print(f"{prefix}  parameters:")
            for param in node.parameters:
                print_ast(param, indent + 2)
        print(f"{prefix})")
    
    elif isinstance(node, Parameter):
        print(f"{prefix}Parameter(type={node.type}, name='{node.name}')")
    
    elif isinstance(node, Type):
        print(f"{prefix}Type('{node}')")


# Teste imprimindo a AST
print_ast(program)