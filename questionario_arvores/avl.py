"""AVL didática; FB = altura da direita - altura da esquerda."""


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1


class AVL:
    def __init__(self):
        self.raiz = None
        self.rotacoes = 0
        self.eventos = []

    def _h(self, no):
        return no.altura if no else 0

    def _fb(self, no):
        return self._h(no.direita) - self._h(no.esquerda)

    def _atualiza_altura(self, no):
        no.altura = 1 + max(self._h(no.esquerda), self._h(no.direita))

    def _rotacao_direita(self, no):
        self.eventos.append(f'Rotação à direita em {no.valor}')
        self.rotacoes += 1
        novo = no.esquerda
        no.esquerda = novo.direita
        novo.direita = no
        self._atualiza_altura(no)
        self._atualiza_altura(novo)
        return novo

    def _rotacao_esquerda(self, no):
        self.eventos.append(f'Rotação à esquerda em {no.valor}')
        self.rotacoes += 1
        novo = no.direita
        no.direita = novo.esquerda
        novo.esquerda = no
        self._atualiza_altura(no)
        self._atualiza_altura(novo)
        return novo

    def inserir(self, valor):
        self.raiz = self._inserir(self.raiz, valor)

    def _inserir(self, no, valor):
        if no is None:
            return No(valor)
        if valor < no.valor:
            no.esquerda = self._inserir(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._inserir(no.direita, valor)
        else:
            return no  # Chaves repetidas não alteram o conjunto.
        self._atualiza_altura(no)
        fb = self._fb(no)
        if fb < -1:
            caso = 'LR' if self._fb(no.esquerda) > 0 else 'LL'
            self.eventos.append(f'Caso {caso} em {no.valor}')
            if caso == 'LR':
                no.esquerda = self._rotacao_esquerda(no.esquerda)
            return self._rotacao_direita(no)
        if fb > 1:
            caso = 'RL' if self._fb(no.direita) < 0 else 'RR'
            self.eventos.append(f'Caso {caso} em {no.valor}')
            if caso == 'RL':
                no.direita = self._rotacao_direita(no.direita)
            return self._rotacao_esquerda(no)
        return no

    def validar(self, esperadas):
        ordem = []

        def visita(no, minimo, maximo):
            if no is None:
                return 0
            assert minimo < no.valor < maximo, 'Ordenação BST inválida'
            he = visita(no.esquerda, minimo, no.valor)
            ordem.append(no.valor)
            hd = visita(no.direita, no.valor, maximo)
            assert abs(hd - he) <= 1, 'Fator de balanceamento inválido'
            assert no.altura == 1 + max(he, hd), 'Altura armazenada incorreta'
            return 1 + max(he, hd)

        altura = visita(self.raiz, float('-inf'), float('inf'))
        assert ordem == sorted(set(esperadas)), 'Chaves ou percurso incorretos'
        return {'altura': altura, 'em_ordem': ordem}

    def estrutura(self):
        linhas = []

        def visita(no, prefixo, lado):
            if no is None:
                linhas.append(f'{prefixo}{lado}: vazio')
                return
            linhas.append(f'{prefixo}{lado}: {no.valor} (h={no.altura}, FB={self._fb(no)})')
            visita(no.esquerda, prefixo + '  ', 'E')
            visita(no.direita, prefixo + '  ', 'D')

        visita(self.raiz, '', 'Raiz')
        return '\n'.join(linhas)
