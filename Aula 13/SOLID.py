Identifique no Projeto do Grupo situações onde os
princípios SOLID poderiam ser (ou foram) aplicados.

--- Single Responsibility Principle ---
O princípio da responsabilidade única é focado na discussão entre as classes de um sistema
e nas suas responsabilidades. Uma responsabilidade é uma tarefa ou ação que a classe deve
realizar, e para que o sistema possa estar de acordo com esse princípio, cada classe deve
possuir apenas uma única responsabilidade.
* Como exemplo para o projeto do segundo bimestre, a classe de usuários era única responsável
por salvar os dados de cada aluno (nome, sobrenome, login, senha, email, curso, matérias).
Mesmo que fosse possivel inserir nessa mesma classe uma validação desses dados, o uso do princípio
de single responsibility foi aplicado, deixando-a apenas com a responsabilidade de agrupar e salvar
as seguintes informações.

--- Open Closed Principle (OCP) ---
Fechado para modificações, aberto para expansão
Desenvolvimento de software em camadas. Estando uma camada bem escrita e definida, as classes derivadas
serão funcionais. As classes derivadas na prática podem apenas usar os novos métodos fechados e acrescentar
novos comportamentos ao sistema conforme novas necessidades forem surgindo.
* Como no caso da classe citada acima (cadastro de usuários), é uma classe fechada tal que a classe de
validação de usuários é sobreposta como derivada.

--- Liskov Substitution Principle ---
Caso você possua uma classe qualquer, você pode substituir suas chamadas por chamadas de quaisquer
classes que herdem dela. Isso evita que haja muita desordem nas relações de herança em todo o sistema.
* Não houve implementação do deste príncipio citado.
 
--- Interface Segregation Principle (ISP) ---
O princípio de segregação de interface diz o seguinte: se uma interface começa a engordar,
devemos parti-la em diversas novas interfaces de tal modo que cada cliente só conheça aquilo
que de fato lhe diz respeito.
* A interface "notas" foi devidamente separada da interface "usuários". Por mais que cada usuário
tenha um conjunto de notas referente, a segregação foi feita de modo a seguir o princípio de ISP.

--- Dependency Inversion Principle (DIP) ---
– Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações;
– Abstrações não devem depender de detalhes. Detalhes devem depender de abstrações.
* Não houve implementação do deste príncipio citado.
