"""Inserção Rubro-Negra com sentinela e casos simétricos."""

RED = 0
BLACK = 1


class No:
    def __init__(self, chave, cor=RED):
        self.chave = chave
        self.cor = cor
        self.esq = self.dir = self.pai = None


class ArvoreRubroNegra:
    def __init__(self):
        self.NIL = No(None, BLACK)
        self.NIL.esq = self.NIL.dir = self.NIL.pai = self.NIL
        self.raiz = self.NIL
        self.rotacoes = 0
        self.eventos = []

    def _cor(self, no, cor):
        # Registra somente mudanças efetivas de cor.
        if no.cor != cor:
            nomes = {RED: 'RUBRO', BLACK: 'NEGRO'}
            self.eventos.append(f'Recoloração de {no.chave}: {nomes[no.cor]} → {nomes[cor]}')
            no.cor = cor

    def _rotacao_esquerda(self, x):
        y = x.dir
        x.dir = y.esq
        if y.esq is not self.NIL:
            y.esq.pai = x
        y.pai = x.pai
        if x.pai is self.NIL:
            self.raiz = y
        elif x is x.pai.esq:
            x.pai.esq = y
        else:
            x.pai.dir = y
        y.esq = x
        x.pai = y
        self.rotacoes += 1
        self.eventos.append(f'Rotação à esquerda em {x.chave}')

    def _rotacao_direita(self, x):
        y = x.esq
        x.esq = y.dir
        if y.dir is not self.NIL:
            y.dir.pai = x
        y.pai = x.pai
        if x.pai is self.NIL:
            self.raiz = y
        elif x is x.pai.dir:
            x.pai.dir = y
        else:
            x.pai.esq = y
        y.dir = x
        x.pai = y
        self.rotacoes += 1
        self.eventos.append(f'Rotação à direita em {x.chave}')

    def inserir(self, chave):
        pai = self.NIL
        atual = self.raiz
        while atual is not self.NIL:
            pai = atual
            if chave == atual.chave:
                return
            atual = atual.esq if chave < atual.chave else atual.dir
        no = No(chave)
        no.esq = no.dir = self.NIL
        no.pai = pai
        if pai is self.NIL:
            self.raiz = no
        elif chave < pai.chave:
            pai.esq = no
        else:
            pai.dir = no
        self._corrigir(no)

    def _corrigir(self, no):
        while no.pai.cor == RED:
            avo = no.pai.pai
            espelhado = no.pai is avo.dir
            tio = avo.esq if espelhado else avo.dir
            sufixo = ' (espelhado)' if espelhado else ''
            if tio.cor == RED:
                self.eventos.append(f'Caso 1{sufixo} no avô {avo.chave}')
                self._cor(no.pai, BLACK)
                self._cor(tio, BLACK)
                self._cor(avo, RED)
                no = avo
            else:
                interno = no is (no.pai.esq if espelhado else no.pai.dir)
                if interno:
                    self.eventos.append(f'Caso 2{sufixo} no avô {avo.chave}')
                    no = no.pai
                    if espelhado:
                        self._rotacao_direita(no)
                    else:
                        self._rotacao_esquerda(no)
                self.eventos.append(f'Caso 3{sufixo} no avô {no.pai.pai.chave}')
                self._cor(no.pai, BLACK)
                self._cor(no.pai.pai, RED)
                if espelhado:
                    self._rotacao_esquerda(no.pai.pai)
                else:
                    self._rotacao_direita(no.pai.pai)
        self._cor(self.raiz, BLACK)

    def validar(self, esperadas):
        assert self.NIL.cor == BLACK, 'NIL deve ser negro'
        assert self.raiz.cor == BLACK, 'Raiz deve ser negra'
        assert self.raiz.pai is self.NIL, 'Pai da raiz incorreto'
        ordem = []

        def visita(no, pai, minimo, maximo):
            if no is self.NIL:
                return 0, 1  # NIL contribui uma unidade à contagem negra.
            assert no.cor in (RED, BLACK), 'Cor inválida'
            assert no.pai is pai, 'Referência de pai incorreta'
            assert minimo < no.chave < maximo, 'Ordenação BST inválida'
            if no.cor == RED:
                assert no.esq.cor == no.dir.cor == BLACK, 'Rubro com filho rubro'
            he, be = visita(no.esq, no, minimo, no.chave)
            ordem.append(no.chave)
            hd, bd = visita(no.dir, no, no.chave, maximo)
            assert be == bd, 'Alturas-negras diferentes'
            return 1 + max(he, hd), be + (no.cor == BLACK)

        altura, negros = visita(self.raiz, self.NIL, float('-inf'), float('inf'))
        assert ordem == sorted(set(esperadas)), 'Chaves ou percurso incorretos'
        # Altura-negra da raiz exclui a própria raiz e inclui o NIL.
        return {'altura': altura, 'altura_negra': negros - (self.raiz is not self.NIL),
                'em_ordem': ordem}

    def estrutura(self):
        linhas = []

        def visita(no, prefixo, lado):
            if no is self.NIL:
                linhas.append(f'{prefixo}{lado}: NIL (NEGRO)')
                return
            cor = 'RUBRO' if no.cor == RED else 'NEGRO'
            linhas.append(f'{prefixo}{lado}: {no.chave} ({cor})')
            visita(no.esq, prefixo + '  ', 'E')
            visita(no.dir, prefixo + '  ', 'D')

        visita(self.raiz, '', 'Raiz')
        return '\n'.join(linhas)
