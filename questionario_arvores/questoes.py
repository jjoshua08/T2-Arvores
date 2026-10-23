"""Executa as seis questões e, com --relatorio, gera respostas.md."""
from pathlib import Path
import sys

try:
    from .avl import AVL
    from .rubro_negra import ArvoreRubroNegra
except ImportError:
    from avl import AVL
    from rubro_negra import ArvoreRubroNegra


QUESTOES = [
    ('Catálogo de produtos da loja', AVL, list(range(10, 151, 10)),
     'O catálogo é carregado pela manhã e recebe milhares de buscas por minuto, com raras inserções posteriores. O balanceamento rígido da AVL favorece as consultas; o custo de reorganização fica concentrado na carga inicial.'),
    ('Log de eventos do app Mumbuca', ArvoreRubroNegra, list(range(5, 51, 5)),
     'Eventos chegam continuamente, enquanto relatórios ocorrem uma vez por dia. O balanceamento flexível da Rubro-Negra favorece alterações frequentes, com recolorações e no máximo duas rotações elementares por inserção.'),
    ('Tabela de símbolos de um compilador', AVL, [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 55, 65],
     'Após a construção, as buscas para verificação de tipos e geração de código superam muito as inserções. A restrição de altura mais rígida da AVL favorece esse uso; a ordem imprevisível não é a razão da escolha.'),
    ('Índice de sessões ativas', ArvoreRubroNegra, [42, 17, 63, 9, 28, 55, 74, 3, 21, 38, 50, 70],
     'Entradas e saídas constantes tornam as alterações dominantes. O balanceamento flexível da Rubro-Negra favorece essa carga dinâmica. Remoções justificam a escolha no cenário, mas não são implementadas neste exercício.'),
    ('Importação de cadastro já ordenado', AVL, list(range(1, 8)),
     'A carga ordenada ocorre uma única vez e é seguida de consultas permanentes. A AVL evita a degeneração da BST comum e mantém balanceamento rígido para consultas. A Rubro-Negra também evitaria a degeneração; o predomínio posterior de buscas favorece a AVL.'),
    ('Fila de processos do escalonador', ArvoreRubroNegra, [40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45],
     'Inserções e reposicionamentos dominam o caminho crítico, com dezenas de milhares de alterações por segundo e poucas buscas específicas. A flexibilidade da Rubro-Negra favorece essa carga. São simuladas apenas as inserções solicitadas, sem remoção ou reposicionamento.'),
]


def resolver():
    secoes, resumo = [], []
    for numero, (titulo, classe, valores, justificativa) in enumerate(QUESTOES, 1):
        arvore = classe()
        historico = []
        for indice, valor in enumerate(valores):
            inicio = len(arvore.eventos)
            arvore.inserir(valor)
            resultado = arvore.validar(valores[:indice + 1])
            eventos = arvore.eventos[inicio:]
            historico.append(f'- Inserção de {valor}: ' + ('; '.join(eventos) if eventos else 'sem rotação ou recoloração.'))
        nome = 'AVL' if classe is AVL else 'Rubro-Negra'
        casos = list(dict.fromkeys(e for e in arvore.eventos if e.startswith('Caso')))
        recoloracoes = sum(e.startswith('Recoloração') for e in arvore.eventos)
        validacao = ('Ordenação BST, presença das chaves, percurso em ordem, FB e alturas armazenadas: válidos.'
                      if classe is AVL else
                      'Ordenação BST, presença das chaves, percurso em ordem, referências de pai e cinco propriedades Rubro-Negras: válidos. '
                      f'Altura-negra da raiz: {resultado["altura_negra"]} (exclui a raiz e inclui NIL).')
        secoes.append(f'''## Questão {numero} — {titulo}

**Árvore escolhida:** {nome}.

**Justificativa:** {justificativa}

**Sequência de inserção:** {', '.join(map(str, valores))}.

**Casos identificados:** {'; '.join(casos) if casos else 'nenhum; não houve necessidade de correção por casos'}.

**Rotações e recolorações por inserção, em ordem de execução:**

{chr(10).join(historico)}

**Estrutura final** (E = esquerda; D = direita):

```text
{arvore.estrutura()}
```

**Altura estrutural final:** {resultado['altura']}.

**Total de rotações elementares:** {arvore.rotacoes}. **Recolorações efetivas:** {recoloracoes}.

**Comprovação automática:** {validacao} Verificações executadas após cada inserção, incluindo a última.

**Percurso em ordem obtido:** {', '.join(map(str, resultado['em_ordem']))}.

**Conclusão:** a {nome} atende à carga descrita, preservando as propriedades verificadas e busca e inserção em O(log n).
''')
        resumo.append(f'| {numero} | {nome} | {resultado["altura"]} | {arvore.rotacoes} |')
    tabela = '| Questão | Árvore | Altura | Rotações |\n| --- | --- | --- | --- |\n' + '\n'.join(resumo)
    introducao = '''# Questionário de árvores balanceadas

Resultados obtidos pela execução das seis sequências, sem bibliotecas externas.

Ambas as estruturas oferecem busca e inserção em O(log n). A AVL exige FB = altura(direita) − altura(esquerda) em {-1, 0, +1} em todos os nós, favorecendo buscas por seu balanceamento mais rígido. A Rubro-Negra usa restrições de cores e altura-negra, com balanceamento mais flexível, favorecendo cargas com muitas alterações. Essa orientação de escolha não garante menor tempo para toda sequência ou implementação.

A altura estrutural conta nós: árvore vazia = 0 e folha = 1; NIL não conta na altura estrutural. A altura-negra informada exclui a própria raiz e inclui NIL. Cada rotação simples conta uma unidade; uma dupla conta duas. Novos nós Rubro-Negros nascem rubros; a inicialização não é recoloração. Registram-se mudanças efetivas de cor, inclusive o ajuste final da raiz.

Na AVL, LL exige rotação à direita; RR à esquerda; LR à esquerda no filho seguida de direita no nó; RL à direita no filho seguida de esquerda no nó. Na Rubro-Negra, o caso 1 recolore pai e tio rubros e continua no avô; o caso 2 converte configuração interna em externa; o caso 3 recolore e rotaciona a configuração externa. Nos casos espelhados, trocam-se esquerda e direita.

As cinco propriedades verificadas são: cores válidas, raiz negra, folhas NIL negras, ausência de filhos rubros de pai rubro e igualdade da altura-negra nos caminhos descendentes. Também se verificam referências de pai, ordenação BST e igualdade do percurso em ordem com as chaves esperadas. Na AVL, a validação recalcula alturas independentemente e confere alturas armazenadas e FB. Execute sem -O, pois as verificações usam assert.

## Resultados

'''
    return introducao + tabela + '\n\n' + '\n'.join(secoes) + '''
## Reprodução

Na pasta `questionario_arvores/`, execute `python3 questoes.py` (ou `python questoes.py` onde esse comando estiver disponível).
Para regenerar o relatório, execute `python3 questoes.py --relatorio`.
As sequências não precisam exercitar todos os casos implementados. Nenhuma rotação é necessária quando as propriedades já são satisfeitas.
'''


if __name__ == '__main__':
    relatorio = resolver()
    print(relatorio)
    if '--relatorio' in sys.argv[1:]:
        Path(__file__).with_name('respostas.md').write_text(relatorio, encoding='utf-8')
