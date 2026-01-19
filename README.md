# Gestor de Transportadora – Caminhoneiros

Programa em Python para localizar caminhões pelo código.

## Funcionalidade
- Busca caminhão pelo identificador (ex: A1, B2).
- Exibe a localização atual.
- Loop contínuo até o usuário sair.

## Estrutura de dados
- Lista de dicionários:
  - `nome`
  - `caminhao`
  - `localização`

## Uso
1. Execute o script.
2. Escolha:
   - `1` para procurar caminhão.
   - `2` para sair.
3. Informe o código do caminhão.

## Requisitos
- Python 3.11

## Observações
- Entrada do caminhão é convertida para maiúsculas.
- Retorna “Não encontrado” se o código não existir.
