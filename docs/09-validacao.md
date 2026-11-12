# 09 — Verificações e limitações

## O que foi conferido

- O arquivo compactado original permanece em [`Projeto_DE1_Somente_Esquematico.zip`](../Projeto_DE1_Somente_Esquematico.zip).
- A estrutura foi extraída em [`projeto/`](../projeto/), com [inventário de SHA-256](../INVENTARIO_EXTRACAO.md).
- O QSF seleciona `EP2C20F484C7`, topo `DE1_Filtro`, dois arquivos BDF e o arquivo MIF.
- O MIF declara `WIDTH=1`, `DEPTH=32768`; há 32768 entradas com 10737 bits ativos.
- Os dois contadores de VGA possuem módulo 800 e 525.
- Há três instâncias `LPM_ROM` utilizando a mesma imagem e seis registros para deslocamento de amostras.
- A escolha de filtros é dada diretamente pelos blocos AND/OR/NOT e por `SW[0..2]`.

## Registros no monitor

As [quatro fotografias da saída VGA](../resultados_vga/README.md) mostram a imagem original e alterações compatíveis com erosão, dilatação e gradiente morfológico. A identificação de cada filtro é baseada no aspecto observado; as chaves não aparecem nas fotografias.

## Validação automatizada

O script [`scripts/validar_projeto.py`](../scripts/validar_projeto.py) realiza checagens estruturais de arquivos e parâmetros. O [workflow](../.github/workflows/validar-arquivos.yml) executa esse script usando Python. Esse procedimento **não utiliza Quartus e não demonstra que a lógica é sintetizável**.

## O que ainda não está demonstrado

- Síntese e roteamento bem-sucedidos no Quartus II 13.0 SP1.
- Fechamento de temporização física, uso de recursos e arquivo SOF.
- Verificação de todos os pixels e das bordas da vizinhança 3×3.
- Verificação independente das posições das chaves durante cada fotografia e das condições de todas as bordas.
- Diagramas de ondas de simulação funcional.

## Arquivos preservados

O projeto original não foi alterado para criar o tutorial. O arquivo [`LEIA-ME.txt`](../projeto/LEIA-ME.txt) continua documentando a preparação do pacote. Os dados e os exemplos apresentados nos capítulos anteriores são verificáveis nos BDF e no MIF.

---
[Anterior](08-reproducao.md) · [Índice](../README.md#repositório-e-tutorial)
