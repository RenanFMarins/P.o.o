# Programação Orientada a objetos<br>
- O que é Polimorfismo e um exemplo de código usando polimorfismo
- O que é Herança e um exemplo de código usando herança
- O que é encapsulamento e um exemplo de código usando encapsulament

Os exemplos dos códigos deverão ser feitos na linguagem de programação python.
OBS: crie um README.md com o propósito do trabalho, com a explicação dos três tópicos.
Em seguida, crie um arquivo em python para cada exemplo. Lembre de comentar o código 
para saber qual conceito está sendo tratada ali.<br>

# Encapsulamento
Encapsulament é a técnica que faz com que detalhes internos do funcionamento dos
métodos de uma classe permaneçam ocultos para os objetos. Por conta dessa técnica,
o conhecimento a respeito da implementação interna da classe é desnecessário do ponto
de vista do objeto, uma vez que isso passa a ser responsabilidade dos métodos internos da
classe.<br>
Assim que uma classe é criada, seu código e seus dados, os quais são chamados de
membros da classe, são determinados. Esses dados recebem o nome de variáveis
membro ou variáveis de instância. Já o código tem outra função de formar os métodos, os
quais também podem ser denominados como métodos membro.<br>
Os métodos presentes em um programa desenvolvido em C# são responsáveis por
determinar a maneira como serão utilizadas as variáveis membro, o que indica que os
métodos cuja função é operar sobre os dados de instância de uma classe determinam qual
será a interface e o comportamento apresentados por ela.<br>
Tendo em mente que os métodos e as variáveis de uma classe podem ser definidos como
públicos ou privados, temos a seguinte situação:
- Tudo o que o usuário externo precisa conhecer a respeito de uma classe encontra-
se em propriedades ou métodos declarados como públicos (public).<br>
- Somente os códigos membros da classe são capazes de acessar seus métodos e
variáveis privados. Isso garante que não ocorrerão ações inadequadas, mas exige
que a interface pública seja planejada com cautela para que o funcionamento interno
da classe não seja muito exposto.<br>

Dito tudo isto, podemos concluir que a única forma de conhecer ou alterar os atributos de
um objeto é por meio de seus métodos. Abaixo cito quatro vantagens do encapsulamento:
- O objeto é disponibilizado ao usuário com toda a sua funcionalidade, sem a
necessidade de conhecermos seu funcionamento ou armazenamento interno;
- É possível modificar um objeto internamente, acrescentando métodos, sem que isto
afete os outros componentes do sistema que utilizam o objeto modificado;
- O processo de desenvolvimento de sistemas é acelerado e simplificado, já que os
usuários dos objetos não precisam necessariamente saber como eles são
constituídos internamente;<br>
- A implementação de um comportamento pode ser modificada radicalmente sem que
haja impacto no resto do programa. Isto é possível porque o código que utiliza o
objeto não depende da maneira que ele é implementado.<br>

# Herança <br>

A Herança possibilita que as classes compartilhem seus atributos, métodos e outros<br>
membros da classe entre si. Para a ligação entre as classes, a herança adota um<br>
relacionamento esquematizado hierarquicamente.<br>
Na Herança temos dois tipos principais de classe:<br>
- Classe Base: A classe que concede as características a uma outra classe.<br>
- Classe Derivada: A classe que herda as características da classe base.<br>
O fato de as classes derivadas herdarem atributos das classes bases assegura que<br>
programas orientados a objetos cresçam de forma linear e não geometricamente em<br>
complexidade. Cada nova classe derivada não possui interações imprevisíveis em relação<br>
ao restante do código do sistema.<br>
Com o uso da herança, uma classe derivada geralmente é uma implementação especifica<br>
de um caso mais geral. A classe derivada deve apenas definir as características que a<br>
tornam única.<br>
Por exemplo: uma classe base que serviria como um modelo genérico pode ser a classe<br>
Pessoa com os campos Nome e Idade. Já uma classe derivada poderia ser Funcionário<br>
com os campos Nome e Idade herdados da classe Pessoa, acrescido do campo Cargo.<br>
De maneira natural, as pessoas visualizam o mundo sendo formado de objetos relacionados<br>
entre si hierarquicamente.<br>
Mais um exemplo: vamos analisar a relação entre animais, mamíferos e cachorros. Os<br>
animais, sob uma descrição abstrata, apresentam atributos, tais como tamanho, inteligência<br>
e estrutura óssea. Apresentam também aspectos comportamentais como mover-se, dormir,<br>
comer, respirar, etc. Esses atributos e aspectos comportamentais definem a classe dos<br>
animais.<br>
Analisando os mamíferos, que são filhos da classe animais, veremos atributos detalhados e<br>
específicos a ele, como por exemplo, tipo de dente, pelos e glândulas mamárias.<br>
Assim, podemos afirmar que os mamíferos são classificados como uma classe derivada dos<br>
animais, que por sua vez, são uma classe base dos mamíferos.<br>
Pela chamada hierárquica de classes, a classe derivada mamíferos recebe todos os<br>
atributos de animais, partindo do princípio que uma classe derivada recebe por herança<br>
todos os atributos de seus ancestrais.<br>

# Polimorfismo <br>
Definimos Polimorfismo como um princípio a partir do qual as classes derivadas de<br>
uma única classe base são capazes de invocar os métodos que, embora apresentem a <br>
mesma assinatura, comportam-se de maneira diferente para cada uma das classes<br>
derivadas.<br>
O Polimorfismo é um mecanismo por meio do qual selecionamos as funcionalidades<br>
utilizadas de forma dinâmica por um programa no decorrer de sua execução. Com<br> 
o Polimorfismo, os mesmos atributos e objetos podem ser utilizados em objetos<br>
distintos, porém, com implementações lógicas diferentes.<br>
Por exemplo: <br>
podemos assumir que uma bola de futebol e uma camisa da seleção brasileira são<br>
artigos esportivos, mas que o cálculo deles em uma venda é calculado de formas<br>
diferentes.<br>
Outro exemplo:<br> 
podemos dizer que uma classe chamada Vendedor e outra chamada Diretor podem ter<br>
como base uma classe chamada Pessoa, com um método chamado CalcularVendas. Se<br>
este método (definido na classe base) se comportar de maneira diferente para as<br>
chamadas feitas a partir de uma instância de Vendedor e para as chamadas feitas<br>
a partir de uma instância de Diretor, ele será considerado um método polimórfico,<br>
ou seja, um método de várias formas. Definimos Polimorfismo como um princípio a<br>
partir do qual as classes derivadas de uma única classe base são capazes de <br>
invocar os métodos que, embora apresentem a mesma assinatura, comportam-se de <br>
maneira diferente para cada uma das classes derivadas.<br>
O Polimorfismo é um mecanismo por meio do qual selecionamos as funcionalidades<br>
utilizadas de forma dinâmica por um programa no decorrer de sua execução.<br>
Com o Polimorfismo, os mesmos atributos e objetos podem ser utilizados em objetos<br>
distintos, porém, com implementações lógicas diferentes.<br>

Por exemplo: podemos assumir que uma bola de futebol e uma camisa da seleção brasileira
são artigos esportivos, mais que o cálculo deles em uma venda é calculado de formas
diferentes.<br>
Outro exemplo: podemos dizer que uma classe chamada Vendedor e outra chamada Diretor
podem ter como base uma classe chamada Pessoa, com um método chamado CalcularVendas.
Se este método (definido na classe base) se comportar de maneira diferente para as 
chamadas feitas a partir de uma instância de Vendedor e para as chamadas feitas a partir
de uma instância de Diretor, ele será considerado um método polimórfico, ou seja, um
método de várias formas.<br>
