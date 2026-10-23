# Questionário de árvores balanceadas

Resultados obtidos pela execução das seis sequências, sem bibliotecas externas.

Ambas as estruturas oferecem busca e inserção em O(log n). A AVL exige FB = altura(direita) − altura(esquerda) em {-1, 0, +1} em todos os nós, favorecendo buscas por seu balanceamento mais rígido. A Rubro-Negra usa restrições de cores e altura-negra, com balanceamento mais flexível, favorecendo cargas com muitas alterações. Essa orientação de escolha não garante menor tempo para toda sequência ou implementação.

A altura estrutural conta nós: árvore vazia = 0 e folha = 1; NIL não conta na altura estrutural. A altura-negra informada exclui a própria raiz e inclui NIL. Cada rotação simples conta uma unidade; uma dupla conta duas. Novos nós Rubro-Negros nascem rubros; a inicialização não é recoloração. Registram-se mudanças efetivas de cor, inclusive o ajuste final da raiz.

Na AVL, LL exige rotação à direita; RR à esquerda; LR à esquerda no filho seguida de direita no nó; RL à direita no filho seguida de esquerda no nó. Na Rubro-Negra, o caso 1 recolore pai e tio rubros e continua no avô; o caso 2 converte configuração interna em externa; o caso 3 recolore e rotaciona a configuração externa. Nos casos espelhados, trocam-se esquerda e direita.

As cinco propriedades verificadas são: cores válidas, raiz negra, folhas NIL negras, ausência de filhos rubros de pai rubro e igualdade da altura-negra nos caminhos descendentes. Também se verificam referências de pai, ordenação BST e igualdade do percurso em ordem com as chaves esperadas. Na AVL, a validação recalcula alturas independentemente e confere alturas armazenadas e FB. Execute sem -O, pois as verificações usam assert.

## Resultados

| Questão | Árvore | Altura | Rotações |
| --- | --- | --- | --- |
| 1 | AVL | 4 | 11 |
| 2 | Rubro-Negra | 5 | 5 |
| 3 | AVL | 4 | 0 |
| 4 | Rubro-Negra | 4 | 0 |
| 5 | AVL | 3 | 4 |
| 6 | Rubro-Negra | 4 | 0 |

## Questão 1 — Catálogo de produtos da loja

**Árvore escolhida:** AVL.

**Justificativa:** O catálogo é carregado pela manhã e recebe milhares de buscas por minuto, com raras inserções posteriores. O balanceamento rígido da AVL favorece as consultas; o custo de reorganização fica concentrado na carga inicial.

**Sequência de inserção:** 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150.

**Casos identificados:** Caso RR em 10; Caso RR em 30; Caso RR em 20; Caso RR em 50; Caso RR em 70; Caso RR em 60; Caso RR em 90; Caso RR em 40; Caso RR em 110; Caso RR em 100; Caso RR em 130.

**Rotações e recolorações por inserção, em ordem de execução:**

- Inserção de 10: sem rotação ou recoloração.
- Inserção de 20: sem rotação ou recoloração.
- Inserção de 30: Caso RR em 10; Rotação à esquerda em 10
- Inserção de 40: sem rotação ou recoloração.
- Inserção de 50: Caso RR em 30; Rotação à esquerda em 30
- Inserção de 60: Caso RR em 20; Rotação à esquerda em 20
- Inserção de 70: Caso RR em 50; Rotação à esquerda em 50
- Inserção de 80: sem rotação ou recoloração.
- Inserção de 90: Caso RR em 70; Rotação à esquerda em 70
- Inserção de 100: Caso RR em 60; Rotação à esquerda em 60
- Inserção de 110: Caso RR em 90; Rotação à esquerda em 90
- Inserção de 120: Caso RR em 40; Rotação à esquerda em 40
- Inserção de 130: Caso RR em 110; Rotação à esquerda em 110
- Inserção de 140: Caso RR em 100; Rotação à esquerda em 100
- Inserção de 150: Caso RR em 130; Rotação à esquerda em 130

**Estrutura final** (E = esquerda; D = direita):

```text
Raiz: 80 (h=4, FB=0)
  E: 40 (h=3, FB=0)
    E: 20 (h=2, FB=0)
      E: 10 (h=1, FB=0)
        E: vazio
        D: vazio
      D: 30 (h=1, FB=0)
        E: vazio
        D: vazio
    D: 60 (h=2, FB=0)
      E: 50 (h=1, FB=0)
        E: vazio
        D: vazio
      D: 70 (h=1, FB=0)
        E: vazio
        D: vazio
  D: 120 (h=3, FB=0)
    E: 100 (h=2, FB=0)
      E: 90 (h=1, FB=0)
        E: vazio
        D: vazio
      D: 110 (h=1, FB=0)
        E: vazio
        D: vazio
    D: 140 (h=2, FB=0)
      E: 130 (h=1, FB=0)
        E: vazio
        D: vazio
      D: 150 (h=1, FB=0)
        E: vazio
        D: vazio
```

**Altura estrutural final:** 4.

**Total de rotações elementares:** 11. **Recolorações efetivas:** 0.

**Comprovação automática:** Ordenação BST, presença das chaves, percurso em ordem, FB e alturas armazenadas: válidos. Verificações executadas após cada inserção, incluindo a última.

**Percurso em ordem obtido:** 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150.

**Conclusão:** a AVL atende à carga descrita, preservando as propriedades verificadas e busca e inserção em O(log n).

## Questão 2 — Log de eventos do app Mumbuca

**Árvore escolhida:** Rubro-Negra.

**Justificativa:** Eventos chegam continuamente, enquanto relatórios ocorrem uma vez por dia. O balanceamento flexível da Rubro-Negra favorece alterações frequentes, com recolorações e no máximo duas rotações elementares por inserção.

**Sequência de inserção:** 5, 10, 15, 20, 25, 30, 35, 40, 45, 50.

**Casos identificados:** Caso 3 (espelhado) no avô 5; Caso 1 (espelhado) no avô 10; Caso 3 (espelhado) no avô 15; Caso 1 (espelhado) no avô 20; Caso 3 (espelhado) no avô 25; Caso 1 (espelhado) no avô 30; Caso 3 (espelhado) no avô 10; Caso 3 (espelhado) no avô 35; Caso 1 (espelhado) no avô 40.

**Rotações e recolorações por inserção, em ordem de execução:**

- Inserção de 5: Recoloração de 5: RUBRO → NEGRO
- Inserção de 10: sem rotação ou recoloração.
- Inserção de 15: Caso 3 (espelhado) no avô 5; Recoloração de 10: RUBRO → NEGRO; Recoloração de 5: NEGRO → RUBRO; Rotação à esquerda em 5
- Inserção de 20: Caso 1 (espelhado) no avô 10; Recoloração de 15: RUBRO → NEGRO; Recoloração de 5: RUBRO → NEGRO; Recoloração de 10: NEGRO → RUBRO; Recoloração de 10: RUBRO → NEGRO
- Inserção de 25: Caso 3 (espelhado) no avô 15; Recoloração de 20: RUBRO → NEGRO; Recoloração de 15: NEGRO → RUBRO; Rotação à esquerda em 15
- Inserção de 30: Caso 1 (espelhado) no avô 20; Recoloração de 25: RUBRO → NEGRO; Recoloração de 15: RUBRO → NEGRO; Recoloração de 20: NEGRO → RUBRO
- Inserção de 35: Caso 3 (espelhado) no avô 25; Recoloração de 30: RUBRO → NEGRO; Recoloração de 25: NEGRO → RUBRO; Rotação à esquerda em 25
- Inserção de 40: Caso 1 (espelhado) no avô 30; Recoloração de 35: RUBRO → NEGRO; Recoloração de 25: RUBRO → NEGRO; Recoloração de 30: NEGRO → RUBRO; Caso 3 (espelhado) no avô 10; Recoloração de 20: RUBRO → NEGRO; Recoloração de 10: NEGRO → RUBRO; Rotação à esquerda em 10
- Inserção de 45: Caso 3 (espelhado) no avô 35; Recoloração de 40: RUBRO → NEGRO; Recoloração de 35: NEGRO → RUBRO; Rotação à esquerda em 35
- Inserção de 50: Caso 1 (espelhado) no avô 40; Recoloração de 45: RUBRO → NEGRO; Recoloração de 35: RUBRO → NEGRO; Recoloração de 40: NEGRO → RUBRO; Caso 1 (espelhado) no avô 20; Recoloração de 30: RUBRO → NEGRO; Recoloração de 10: RUBRO → NEGRO; Recoloração de 20: NEGRO → RUBRO; Recoloração de 20: RUBRO → NEGRO

**Estrutura final** (E = esquerda; D = direita):

```text
Raiz: 20 (NEGRO)
  E: 10 (NEGRO)
    E: 5 (NEGRO)
      E: NIL (NEGRO)
      D: NIL (NEGRO)
    D: 15 (NEGRO)
      E: NIL (NEGRO)
      D: NIL (NEGRO)
  D: 30 (NEGRO)
    E: 25 (NEGRO)
      E: NIL (NEGRO)
      D: NIL (NEGRO)
    D: 40 (RUBRO)
      E: 35 (NEGRO)
        E: NIL (NEGRO)
        D: NIL (NEGRO)
      D: 45 (NEGRO)
        E: NIL (NEGRO)
        D: 50 (RUBRO)
          E: NIL (NEGRO)
          D: NIL (NEGRO)
```

**Altura estrutural final:** 5.

**Total de rotações elementares:** 5. **Recolorações efetivas:** 28.

**Comprovação automática:** Ordenação BST, presença das chaves, percurso em ordem, referências de pai e cinco propriedades Rubro-Negras: válidos. Altura-negra da raiz: 3 (exclui a raiz e inclui NIL). Verificações executadas após cada inserção, incluindo a última.

**Percurso em ordem obtido:** 5, 10, 15, 20, 25, 30, 35, 40, 45, 50.

**Conclusão:** a Rubro-Negra atende à carga descrita, preservando as propriedades verificadas e busca e inserção em O(log n).

## Questão 3 — Tabela de símbolos de um compilador

**Árvore escolhida:** AVL.

**Justificativa:** Após a construção, as buscas para verificação de tipos e geração de código superam muito as inserções. A restrição de altura mais rígida da AVL favorece esse uso; a ordem imprevisível não é a razão da escolha.

**Sequência de inserção:** 50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 55, 65.

**Casos identificados:** nenhum; não houve necessidade de correção por casos.

**Rotações e recolorações por inserção, em ordem de execução:**

- Inserção de 50: sem rotação ou recoloração.
- Inserção de 30: sem rotação ou recoloração.
- Inserção de 70: sem rotação ou recoloração.
- Inserção de 20: sem rotação ou recoloração.
- Inserção de 40: sem rotação ou recoloração.
- Inserção de 60: sem rotação ou recoloração.
- Inserção de 80: sem rotação ou recoloração.
- Inserção de 10: sem rotação ou recoloração.
- Inserção de 25: sem rotação ou recoloração.
- Inserção de 35: sem rotação ou recoloração.
- Inserção de 55: sem rotação ou recoloração.
- Inserção de 65: sem rotação ou recoloração.

**Estrutura final** (E = esquerda; D = direita):

```text
Raiz: 50 (h=4, FB=0)
  E: 30 (h=3, FB=0)
    E: 20 (h=2, FB=0)
      E: 10 (h=1, FB=0)
        E: vazio
        D: vazio
      D: 25 (h=1, FB=0)
        E: vazio
        D: vazio
    D: 40 (h=2, FB=-1)
      E: 35 (h=1, FB=0)
        E: vazio
        D: vazio
      D: vazio
  D: 70 (h=3, FB=-1)
    E: 60 (h=2, FB=0)
      E: 55 (h=1, FB=0)
        E: vazio
        D: vazio
      D: 65 (h=1, FB=0)
        E: vazio
        D: vazio
    D: 80 (h=1, FB=0)
      E: vazio
      D: vazio
```

**Altura estrutural final:** 4.

**Total de rotações elementares:** 0. **Recolorações efetivas:** 0.

**Comprovação automática:** Ordenação BST, presença das chaves, percurso em ordem, FB e alturas armazenadas: válidos. Verificações executadas após cada inserção, incluindo a última.

**Percurso em ordem obtido:** 10, 20, 25, 30, 35, 40, 50, 55, 60, 65, 70, 80.

**Conclusão:** a AVL atende à carga descrita, preservando as propriedades verificadas e busca e inserção em O(log n).

## Questão 4 — Índice de sessões ativas

**Árvore escolhida:** Rubro-Negra.

**Justificativa:** Entradas e saídas constantes tornam as alterações dominantes. O balanceamento flexível da Rubro-Negra favorece essa carga dinâmica. Remoções justificam a escolha no cenário, mas não são implementadas neste exercício.

**Sequência de inserção:** 42, 17, 63, 9, 28, 55, 74, 3, 21, 38, 50, 70.

**Casos identificados:** Caso 1 no avô 42; Caso 1 no avô 17; Caso 1 no avô 63.

**Rotações e recolorações por inserção, em ordem de execução:**

- Inserção de 42: Recoloração de 42: RUBRO → NEGRO
- Inserção de 17: sem rotação ou recoloração.
- Inserção de 63: sem rotação ou recoloração.
- Inserção de 9: Caso 1 no avô 42; Recoloração de 17: RUBRO → NEGRO; Recoloração de 63: RUBRO → NEGRO; Recoloração de 42: NEGRO → RUBRO; Recoloração de 42: RUBRO → NEGRO
- Inserção de 28: sem rotação ou recoloração.
- Inserção de 55: sem rotação ou recoloração.
- Inserção de 74: sem rotação ou recoloração.
- Inserção de 3: Caso 1 no avô 17; Recoloração de 9: RUBRO → NEGRO; Recoloração de 28: RUBRO → NEGRO; Recoloração de 17: NEGRO → RUBRO
- Inserção de 21: sem rotação ou recoloração.
- Inserção de 38: sem rotação ou recoloração.
- Inserção de 50: Caso 1 no avô 63; Recoloração de 55: RUBRO → NEGRO; Recoloração de 74: RUBRO → NEGRO; Recoloração de 63: NEGRO → RUBRO
- Inserção de 70: sem rotação ou recoloração.

**Estrutura final** (E = esquerda; D = direita):

```text
Raiz: 42 (NEGRO)
  E: 17 (RUBRO)
    E: 9 (NEGRO)
      E: 3 (RUBRO)
        E: NIL (NEGRO)
        D: NIL (NEGRO)
      D: NIL (NEGRO)
    D: 28 (NEGRO)
      E: 21 (RUBRO)
        E: NIL (NEGRO)
        D: NIL (NEGRO)
      D: 38 (RUBRO)
        E: NIL (NEGRO)
        D: NIL (NEGRO)
  D: 63 (RUBRO)
    E: 55 (NEGRO)
      E: 50 (RUBRO)
        E: NIL (NEGRO)
        D: NIL (NEGRO)
      D: NIL (NEGRO)
    D: 74 (NEGRO)
      E: 70 (RUBRO)
        E: NIL (NEGRO)
        D: NIL (NEGRO)
      D: NIL (NEGRO)
```

**Altura estrutural final:** 4.

**Total de rotações elementares:** 0. **Recolorações efetivas:** 11.

**Comprovação automática:** Ordenação BST, presença das chaves, percurso em ordem, referências de pai e cinco propriedades Rubro-Negras: válidos. Altura-negra da raiz: 2 (exclui a raiz e inclui NIL). Verificações executadas após cada inserção, incluindo a última.

**Percurso em ordem obtido:** 3, 9, 17, 21, 28, 38, 42, 50, 55, 63, 70, 74.

**Conclusão:** a Rubro-Negra atende à carga descrita, preservando as propriedades verificadas e busca e inserção em O(log n).

## Questão 5 — Importação de cadastro já ordenado

**Árvore escolhida:** AVL.

**Justificativa:** A carga ordenada ocorre uma única vez e é seguida de consultas permanentes. A AVL evita a degeneração da BST comum e mantém balanceamento rígido para consultas. A Rubro-Negra também evitaria a degeneração; o predomínio posterior de buscas favorece a AVL.

**Sequência de inserção:** 1, 2, 3, 4, 5, 6, 7.

**Casos identificados:** Caso RR em 1; Caso RR em 3; Caso RR em 2; Caso RR em 5.

**Rotações e recolorações por inserção, em ordem de execução:**

- Inserção de 1: sem rotação ou recoloração.
- Inserção de 2: sem rotação ou recoloração.
- Inserção de 3: Caso RR em 1; Rotação à esquerda em 1
- Inserção de 4: sem rotação ou recoloração.
- Inserção de 5: Caso RR em 3; Rotação à esquerda em 3
- Inserção de 6: Caso RR em 2; Rotação à esquerda em 2
- Inserção de 7: Caso RR em 5; Rotação à esquerda em 5

**Estrutura final** (E = esquerda; D = direita):

```text
Raiz: 4 (h=3, FB=0)
  E: 2 (h=2, FB=0)
    E: 1 (h=1, FB=0)
      E: vazio
      D: vazio
    D: 3 (h=1, FB=0)
      E: vazio
      D: vazio
  D: 6 (h=2, FB=0)
    E: 5 (h=1, FB=0)
      E: vazio
      D: vazio
    D: 7 (h=1, FB=0)
      E: vazio
      D: vazio
```

**Altura estrutural final:** 3.

**Total de rotações elementares:** 4. **Recolorações efetivas:** 0.

**Comprovação automática:** Ordenação BST, presença das chaves, percurso em ordem, FB e alturas armazenadas: válidos. Verificações executadas após cada inserção, incluindo a última.

**Percurso em ordem obtido:** 1, 2, 3, 4, 5, 6, 7.

**Conclusão:** a AVL atende à carga descrita, preservando as propriedades verificadas e busca e inserção em O(log n).

## Questão 6 — Fila de processos do escalonador

**Árvore escolhida:** Rubro-Negra.

**Justificativa:** Inserções e reposicionamentos dominam o caminho crítico, com dezenas de milhares de alterações por segundo e poucas buscas específicas. A flexibilidade da Rubro-Negra favorece essa carga. São simuladas apenas as inserções solicitadas, sem remoção ou reposicionamento.

**Sequência de inserção:** 40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45.

**Casos identificados:** Caso 1 no avô 40; Caso 1 no avô 20; Caso 1 no avô 60.

**Rotações e recolorações por inserção, em ordem de execução:**

- Inserção de 40: Recoloração de 40: RUBRO → NEGRO
- Inserção de 20: sem rotação ou recoloração.
- Inserção de 60: sem rotação ou recoloração.
- Inserção de 10: Caso 1 no avô 40; Recoloração de 20: RUBRO → NEGRO; Recoloração de 60: RUBRO → NEGRO; Recoloração de 40: NEGRO → RUBRO; Recoloração de 40: RUBRO → NEGRO
- Inserção de 30: sem rotação ou recoloração.
- Inserção de 50: sem rotação ou recoloração.
- Inserção de 70: sem rotação ou recoloração.
- Inserção de 5: Caso 1 no avô 20; Recoloração de 10: RUBRO → NEGRO; Recoloração de 30: RUBRO → NEGRO; Recoloração de 20: NEGRO → RUBRO
- Inserção de 15: sem rotação ou recoloração.
- Inserção de 25: sem rotação ou recoloração.
- Inserção de 35: sem rotação ou recoloração.
- Inserção de 45: Caso 1 no avô 60; Recoloração de 50: RUBRO → NEGRO; Recoloração de 70: RUBRO → NEGRO; Recoloração de 60: NEGRO → RUBRO

**Estrutura final** (E = esquerda; D = direita):

```text
Raiz: 40 (NEGRO)
  E: 20 (RUBRO)
    E: 10 (NEGRO)
      E: 5 (RUBRO)
        E: NIL (NEGRO)
        D: NIL (NEGRO)
      D: 15 (RUBRO)
        E: NIL (NEGRO)
        D: NIL (NEGRO)
    D: 30 (NEGRO)
      E: 25 (RUBRO)
        E: NIL (NEGRO)
        D: NIL (NEGRO)
      D: 35 (RUBRO)
        E: NIL (NEGRO)
        D: NIL (NEGRO)
  D: 60 (RUBRO)
    E: 50 (NEGRO)
      E: 45 (RUBRO)
        E: NIL (NEGRO)
        D: NIL (NEGRO)
      D: NIL (NEGRO)
    D: 70 (NEGRO)
      E: NIL (NEGRO)
      D: NIL (NEGRO)
```

**Altura estrutural final:** 4.

**Total de rotações elementares:** 0. **Recolorações efetivas:** 11.

**Comprovação automática:** Ordenação BST, presença das chaves, percurso em ordem, referências de pai e cinco propriedades Rubro-Negras: válidos. Altura-negra da raiz: 2 (exclui a raiz e inclui NIL). Verificações executadas após cada inserção, incluindo a última.

**Percurso em ordem obtido:** 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70.

**Conclusão:** a Rubro-Negra atende à carga descrita, preservando as propriedades verificadas e busca e inserção em O(log n).

## Reprodução

Na pasta `questionario_arvores/`, execute `python3 questoes.py` (ou `python questoes.py` onde esse comando estiver disponível).
Para regenerar o relatório, execute `python3 questoes.py --relatorio`.
As sequências não precisam exercitar todos os casos implementados. Nenhuma rotação é necessária quando as propriedades já são satisfeitas.
