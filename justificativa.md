# Justificativa de Modelagem da AST


### Quais elementos da gramática foram representados diretamente como classes na AST?

Foram criadas as seguintes classes principais:

- **Program**: Representa o programa completo, contendo uma MainClass e uma lista de ClassDecl
- **MainClass**: Representa a classe principal com método main (simplificada, só armazena o nome)
- **ClassDecl**: Representa declarações de classes, incluindo herança, variáveis e métodos
- **VarDecl**: Representa declarações de variáveis com tipo e nome
- **MethodDecl**: Representa declarações de métodos com tipo de retorno, nome e parâmetros
- **Parameter**: Representa parâmetros de métodos
- **Type**: Representa tipos, incluindo arrays multidimensionais

### O que foi omitido na sua modelagem da AST e qual o motivo?

Foram omitidos alguns elementos que não agregam valor semântico adicional:

- **Símbolos terminais** como `{`, `}`, `;`, `(`, `)`. Pois são necessários apenas para parsing, que eu optei por não fazer
- **Palavras-chave** como `class`, `public`, `static`. A estrutura da AST já indica essas informações
- **Detalhes do método main**. Como é sempre igual, só armazenei o nome da classe principal
- **Corpo dos métodos**. A gramática fornecida só define métodos vazios e eu optei por não utilizar nenhum delimitador, então não há uma necessidade de definir o corpo.

### Como você representou listas e elementos opcionais?

- **Listas**: Utilizei `List[TipoElemento]` do módulo `typing` para representar coleções (ex: lista de classes, variáveis, métodos)
- **Elementos opcionais**: Utilizei `Optional[Tipo]` para elementos que podem não existir (ex: classe pai na herança)
- **Valores padrão**: Usei listas vazias como padrão quando não há elementos (`vars=[]`)

### Você utilizou herança entre classes da AST?

Sim, utilizei uma **classe base `ASTNode`** da qual todas as outras classes herdam. Para garantir:

- **Uniformidade**: Todos os nós da AST têm uma base comum
- **Extensibilidade**: Facilita adicionar funcionalidades comuns no futuro (ex: métodos de visitação)
- **Segurança de Tipo**: Permite usar `ASTNode` como tipo genérico para referências

### Houve dificuldades específicas ao tentar representar partes da gramática na AST?
Sim. Houve 4 dificuldades pontuais que me geraram dúvida inicialmente: 

1. **Na representação de Arrays**
A gramática permite arrays multidimensionais (`ArrayPart`).
Resolvi isso usando um campo `array_dimensions` na classe `Type`:
- `0` = tipo simples
- `1` = array unidimensional `[]`
- `2` = array bidimensional `[][]`, etc.

2. **Em diferenciar variáveis estáticas vs instância**
A gramática distingue variáveis estáticas das de instância. Criei campos separados na `ClassDecl`:
- `static_vars`: para variáveis estáticas
- `vars`: para variáveis de instância

3. **Se deixar de definir o corpo do método era prejudicial**
Como a gramática só define métodos vazios `{}`, posteriormente, optei por não representar o corpo dos métodos na AST atual, focando apenas na declaração com parâmetros.

4. **Se definia ou não o método principal**
O método main sempre tem a mesma definição, então simplifiquei a `MainClass` para armazenar apenas o nome da classe, sem repetir a estrutura do método.
