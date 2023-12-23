# Supertrunfo

--------------------------------------------------------------------------------------------------------------------
# IMPORTANTE

Para iniciar o projeto, crie uma branch release a partir da main e trabalhe posteriormente em branchs auxiliares a essa. Não tente, sob nenhuma hipótese, mergear na main.

---------------------------------------------------------------------------------------------------------------------

<details>
  <summary><strong>🎲Regras do jogo🎲</strong></summary><br />

- Supertrunfo é um jogo de cartas com determinados atributos em que cada rodada consiste em comparar os atributos de duas cartas e ver quem é o vencedor da rodada. No final da partida, ganha quem fizer mais pontos ou achar a carta supertrunfo primeiro. Para determinar o vencedor pode haver diferentes interpretações da regra como maior quantidade de pontos, no caso de contagem crescente de pontos, ou quem fizer seu oponente chegar a zero primeiro, contagem decrescente de hp/vida/ponto.
Exemplos de jogos conhecidos no estilo supertrunfo: Yu-Gi-Oh!, Hearthstone, Pokemon entre outros.
</details>

Este é um projetin para treino de competencias básicas no python.

Aqui você poderá treinar algumas das habilidades básicas aprendidas no curso como: Utilização de git e github, criação e manipulação de classes, criação e manipulação de funções e seus parametros, callbacks, condicionais, loops, dicionarios, listas e mais o que quiser implementar.

Algumas dicas importantes:

- Procure ler e seguir todas as dicas 😉
- Antes de começar, leia todos os requisitos mas faça um por um em [babysteps](https://eufacoprogramas.com/baby-steps/)
- Faça, quando possível, o projeto em componentes diferentes.
- A estrutura de pastas é apenas sugestivo mas não obrigatório, sintam-se livres para utilizar sua própria organização
- Lembrem de utilizar os conceitos aprendidos em git e github para evitar e/ou resolver conflitos.
<strong>- Não dê comite na Main ou em branchs de outras pessoas.</strong> Crie uma branch release (nomeDoAsp-release) e a partir dela, crie outras branchs que serão mergeadas na sua release. Sua release será sua main.

<details>
  <summary>💡Alguns comandos importante💡</summary>
  
  - Para clonar este repositório: `git clone git@github.com:gabrielsfdev/supertrunfo.git`
  - Para criar e mudar de branch: `git checkout -b nome-da-nova-branch`
  - Para criar branch sem mudar para ela: `git branch nome-da-nova-branch`
  - Para mudar de branch sem criar uma nova: `git checkout nome-da-branch`
  - Para adicionar todas as alterações ao stage: `git add .`
  - Para fazer commit: `git commit -m "mensagem do commit`
  - Para dar push pela primeira vez: `git push -u origin nome-da-branch`
  - Para dar pull e receber as novas atualizações feitas: `git pull`

</details>

Este é mini projeto criado por @gabrielsfdev em fase alpha pode conter falhas de lógica, erros de estruturação e quaisquer outros contratempos, esteja ciente disso antes de iniciar.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

# Requisitos:

### 1. Implemente uma lógica que crie as cartas e adicione à um baralho customizado:

Dica: Utilize classes e dicionários.
<details>
  <summary>Exemplo de carta</summary>
  
  ```python
  {'Carta1': {'nome': 'Alumni', 'ataque': 99, 'defesa': 99, 'super_trunfo': True}}
  ```
  
</details>

### 2. Implemente uma lógica que adicione os jogadores e as informações necessárias, como as cartas disponíveis:

Dica: Utilize classes. EVITE utilizar o baralho pronto.

### 3. Crie uma lógica de forma que possa listar todas as cartas disponíveis em sua mão:

Dica: Utilize a classe já criada do player.

### 4. Crie a lógica do jogo:

Nesta lógica é importante que implemente as rodadas, adicione as cartas, determine quem ganha e quem perde em cada rodada.

Dica: Utilize funções, loops, condicionais e manipulação de classe.

### 5. Adicione a lógica para que ao final de cada rodada seja mostrado o placar do jogo:

Dica: Você pode (preferencialmente) usar uma callback.

### 6. Adicione a lógica para um menu interativo em que dê ao usuário a opção de utilizar um baralho pronto ou adicionar suas próprias cartas.

Dica: Você pode (preferencialmente) usar uma callback.

### 7. Adicione a lógica do super trunfo:

Dica: adicione essa lógica dentro da função principal das rodadas (feito no requisito 4)

## Bonus

### 8. Adicione o atributo raridade as cartas e crie filtros para raridade, nomes e para o super trunfo:

Adicione atributos à classe Carta, como `raridade`, e crie funções de filtro para nomes, raridades e conforme necessário.
