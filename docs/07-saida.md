# 07 — Saída VGA e máscara da imagem

O resultado da operação passa por uma última porta **AND** com `IMG_MASK`, gerando o bit `PIXEL`. O esquema distribui essa mesma informação para cada bit dos canais `VGA_R[3:0]`, `VGA_G[3:0]` e `VGA_B[3:0]`.

Portanto, quando `PIXEL=1`, os três canais recebem o valor binário `1111` (branco). Quando `PIXEL=0`, os três recebem `0000` (preto). A saída foi projetada para visualização **monocromática binária**, mesmo utilizando três canais RGB.

## Janela de imagem

Os limites de comparador definem uma região horizontal de **H=144..399** e vertical de **V=35..162**, totalizando 256 × 128 pixels. Fora dela, `IMG_MASK=0` faz `PIXEL=0`.

## Pinos do projeto

| Sinal | Pino |
|---|---|
| `CLOCK_50` | L1 |
| `KEY[0]` | R22 |
| `SW[0]`, `SW[1]`, `SW[2]` | L22, L21, M22 |
| `VGA_R[0..3]` | D9, C9, A7, B7 |
| `VGA_G[0..3]` | B8, C10, B9, A8 |
| `VGA_B[0..3]` | A9, D11, A10, B10 |
| `VGA_HS`, `VGA_VS` | A11, B11 |

Os endereços dos pinos provêm de [`DE1_Filtro.qsf`](../projeto/DE1_Filtro.qsf). A ligação física e a compatibilidade das atribuições devem ser conferidas no Pin Planner antes de gravar a placa.

---
[Anterior](06-filtros.md) · [Índice](../README.md#repositório-e-tutorial) · [Próximo: reprodução](08-reproducao.md)
