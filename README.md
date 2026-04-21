# Árvore Binária de Busca (BST) - Estrutura Hierárquica 🌳

Este repositório contém uma implementação robusta de uma **Árvore Binária de Busca** em Python. Diferente das listas lineares, a BST organiza os dados de forma que cada busca divida o espaço de trabalho pela metade, proporcionando alta performance em grandes volumes de dados.

## 🚀 Funcionalidades

A classe `Arvore` inclui operações fundamentais e avançadas:

- **`add(value)`**: Insere um valor na árvore mantendo a regra: valores menores à esquerda, maiores ou iguais à direita.
- **`get(value)`**: Busca um valor específico com complexidade média $O(\log n)$.
- **`remove(value)`**: Remove um nó da árvore tratando os três cenários clássicos:
  1. Nó folha (sem filhos).
  2. Nó com apenas um filho.
  3. Nó com dois filhos (substituição pelo sucessor em ordem).
- **`get_nivel_no(value)`**: Calcula a profundidade/nível de um nó específico na hierarquia.

## 🔄 Métodos de Travessia (Percursos)

Implementação de diferentes formas de visitar os nós usando **recursividade**:
1. **Em Ordem (`print_ordem`)**: Visita a subárvore esquerda, o nó atual e a subárvore direita (resulta em valores ordenados).
2. **Pré-Ordem (`print_pre_ordem`)**: Visita o nó atual antes de seus filhos.
3. **Pós-Ordem (`print_pos_ordem`)**: Visita os filhos antes do nó pai.

## 📊 Por que usar uma Árvore Binária?

Enquanto em uma lista comum você pode precisar olhar todos os itens ($O(n)$) para achar o que procura, na Árvore Binária de Busca, o caminho é reduzido drasticamente:



| Operação | Lista Encadeada | Árvore Binária (BST) |
| :--- | :--- | :--- |
| **Busca** | $O(n)$ | $O(\log n)$ |
| **Inserção** | $O(1)$ | $O(\log n)$ |
| **Remoção** | $O(n)$ | $O(\log n)$ |

## 📝 Aprendizados de AED
- **Recursividade:** Aplicada nos algoritmos de percurso para navegar pela estrutura.
- **Lógica de Sucessor:** Entendimento de como manter a integridade da árvore após a remoção de nós internos.
- **Hierarquia de Dados:** Diferença fundamental entre estruturas lineares (Listas) e não lineares (Árvores).

---
Desenvolvido por [Dowglas Hademar](https://github.com/Dowglas-Hademar)
