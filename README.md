# BattleCard

--------------------------------------------------------------------------------------------------------------------
# IMPORTANTE

Para iniciar o projeto, crie uma branch release a partir da main e trabalhe posteriormente em branchs auxiliares a essa. Não tente, sob nenhuma hipótese, mergear na main.

---------------------------------------------------------------------------------------------------------------------

<details>
  <summary><strong>🎲Regras do jogo🎲</strong></summary><br />

- BattleCard é um jogo de cartas onde as rodadas envolvem a comparação de atributos. O objetivo é fazer o oponente chegar a zero de HP para vencer, usando diferentes interpretações, como pontuação crescente ou zerar o HP do oponente.

- Durante um ataque, há 3 situações:
  1. Ataque maior que defesa: O perdedor perde HP igual ao valor do ataque.
  2. Ataque menor que defesa: Nada acontece com o HP, ou opcionalmente, o perdedor perde 50% do valor de ataque.
  3. Ataque igual à defesa: Nada acontece.

- Exemplos de jogos semelhantes são Yu-Gi-Oh!, Hearthstone e Pokemon. O jogo termina quando alguém atinge zero ou menos de HP.
</details>

Este é um projetin para treino de competencias básicas no python.

Aqui você poderá treinar algumas das habilidades básicas aprendidas no curso como: Utilização de git e github, criação e manipulação de classes, criação e manipulação de funções e seus parametros, callbacks, condicionais, loops, dicionarios, listas e mais o que quiser implementar.

<details>
  <summary><strong>💡Algumas dicas importantes💡</strong></summary><br />

- Procure ler e seguir todas as dicas 😉
- Antes de começar, leia todos os requisitos mas faça um por um em [babysteps](https://eufacoprogramas.com/baby-steps/)
- Faça, quando possível, o projeto em componentes diferentes.
- A estrutura de pastas é apenas sugestivo mas não obrigatório, sintam-se livres para utilizar sua própria organização
- Lembrem de utilizar os conceitos aprendidos em git e github para evitar e/ou resolver conflitos.
- <strong> Não dê commit na main ou em branchs de outras pessoas.</strong> Crie uma branch release (nomeDoAsp-release) e a partir dela, crie outras branchs que serão mergeadas na sua release. Sua release será sua main.

</details>

<details>
  <summary>🧑‍💻Alguns comandos importante🧑‍💻</summary>
  
  - Para clonar este repositório: `git clone git@github.com:gabrielsfdev/battlecard.git`
  - Para criar e mudar de branch: `git checkout -b nome-da-nova-branch`
  - Para criar branch sem mudar para ela: `git branch nome-da-nova-branch`
  - Para mudar de branch sem criar uma nova: `git checkout nome-da-branch`
  - Para adicionar todas as alterações ao stage: `git add .`
  - Para fazer commit: `git commit -m "mensagem do commit`
  - Para dar push pela primeira vez: `git push -u origin nome-da-branch`
  - Para dar pull e receber as novas atualizações feitas: `git pull`
  - Para acessar módulos que não estão no mesmo nível `sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))` onde `"../"` é um nível acima, `"../../"` são dois níveis...
  - Para utilizar um timer, para que uma determinada ação ocorra, pode usar importar o [time](https://docs.python.org/3/library/time.html) e usar o `time.sleep()`
  - Para obter números aleatórios, pode utilizar a função [random](https://www.w3schools.com/python/module_random.asp)

</details>

<details>
  <summary>❓Começou antes da mudança de nome ? Dê uma olhada aqui❓</summary>
  - Atualize a URL do repositório remoto: `git remote set-url origin nova_url`
  - Após isso já pode dar git add, commit e push

</details>

Este é mini projeto criado por @gabrielsfdev em fase alpha pode conter falhas de lógica, erros de estruturação e quaisquer outros contratempos, esteja ciente disso antes de iniciar.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

# Requisitos:

### 1. Implemente uma lógica que crie as cartas e adicione à um baralho:

Dica: Utilize classes e dicionários.
<details>
  <summary>Exemplo de carta</summary>
  
  ```python
  {'Carta1': {'nome': 'Alumni', 'ataque': 99, 'defesa': 99, 'super_card': True}}
  ```
  
</details>

### 2. Implemente uma lógica que adicione os jogadores e as informações necessárias, como as cartas disponíveis:

Dica: Utilize classes. Pode utilizar o baralho defaul na pasta data/cartas_exemplo.

### 3. Crie uma lógica de forma que possa listar todas as cartas disponíveis em sua mão. Limite para apenas 5 cartas em sua mão:

Dica: Utilize a classe já criada do player. Você pode randomizar as cartas do deck em sua mão utilizando o módulo [random](https://www.w3schools.com/python/module_random.asp)

### 4. Crie a lógica do jogo:

Nesta lógica é importante que implemente as rodadas, adicione as cartas, determine quem ganha e quem perde em cada rodada. Retire as cartas utilizadas da sua mão e coloque uma carta nova do baralho. Não esqueça de tratar possiveis erros com uso de [try/except](https://www.w3schools.com/python/python_try_except.asp)

Dica: Utilize funções, loops, condicionais, manipulação de classe, raise e try/except.

### 5. Adicione a lógica para que ao final de cada rodada seja mostrado o placar do jogo:

Dica: Você pode utilizar da classe player já criada.

### 6. Adicione a lógica para um menu interativo em que dê ao usuário a opção de utilizar um baralho pronto ou adicionar suas próprias cartas.

Dica: Você pode (preferencialmente) usar uma callback.

### 7. Adicione a lógica do super card:

Dica: <strong>A carta supercard não pode ser encontrada antes da 5ª rodada.</strong> O supercard deve garantir que o primeiro a encontra-lo, vencerá a partida. Adicione essa lógica dentro da função principal das rodadas (feito no requisito 4)

## Bonus

### 8. Adicione o atributo raridade as cartas e crie filtros para raridade, nomes e para o super card:

Adicione atributos à classe Carta, como `raridade`, e crie funções de filtro para nomes, raridades e conforme necessário.

### 9. Dê a opção de salvar o deck personalizado e salve em um arquivo .txt ou .md

Dica: será útil padronizar o nome e diretório dos decks salvos. Você pode utilizar a função [open()](https://www.w3schools.com/python/python_file_handling.asp)

### 10. Ao inicio da rodada, forneça a opção de escolher um deck personalizado já criado.

Dica: Utilize a função [open()](https://www.w3schools.com/python/python_file_handling.asp) novamente com o nome já padronizado. Faça isso no menu criado no req 6.

## Para finalizar

### Embeleze seu projeto (opcional):

- Você pode criar mais opções no menu, colocar os textos com tabulações padrões (\t).
- Considere o uso de [f-strings com alinhamento](https://cienciaprogramada.com.br/2022/03/formatacao-strings-python/#Alinhamento-2) se necessário.
- Considere o uso do módulo `time` para visualização por etapas por parte do usuário.
- Considere o uso da seguinte linha de código `os.system('cls' if os.name == 'nt' else 'clear')` para limpar o terminal antes de alguma determinada ação.

### Um projeto no seu portifólio para chamar de seu (opcional):

Clique em fork, desmarque a opção para dar fork apenas na main e coloque o nome que desejar.

Vá em `settings`, depois em `default branch` e click em `switch to another branch`. Escolha a branch em que você trabalhou e então clique em `update`.

Pronto, você tem um projeto para chamar de seu. Sinta-se livre para modificar o que quiser, inclusive o readme.

(opcional) Vá em branchs e apague as outras branchs.

# Por favor, se gostou do projeto, dê uma star ⭐ e deixe os créditos no projeto.