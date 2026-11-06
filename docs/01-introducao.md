# 01 — Introdução

O experimento integra processamento digital de imagens e sistemas digitais reconfiguráveis por meio de uma **imagem binária armazenada em memória ROM**. Em vez de código em linguagem HDL, toda a topologia foi montada com componentes gráficos do Quartus II.

A FPGA é uma Terasic **DE1**, equipada com Cyclone II `EP2C20F484C7`. O arquivo de projeto indica `DE1_Filtro` como top-level e informa as ligações de `CLOCK_50`, `KEY[0]`, `SW[0..2]` e VGA.

## Fundamentos

Uma imagem binária associa um bit a cada posição `(x,y)`: zero ou um. A morfologia matemática avalia padrões de vizinhança e produz novos pixels a partir de operações lógicas. A dilatação e a erosão são operações fundamentais, e sua diferença lógica pode destacar contornos.

O projeto usa a mesma matriz de 256 × 128 posições em três instâncias de ROM, portas AND/OR para combinar os nove pixels e uma seleção de operações controlada pelas chaves.

**Escopo de validação:** arquivos `.bdf`, `.qsf` e `.mif` permitem comprovar a arquitetura e os parâmetros declarados; sem a compilação no Quartus e sem fotos do monitor não é possível garantir o resultado físico.

---
[Índice](../README.md#repositório-e-tutorial) · [Próximo: arquitetura](02-arquitetura.md)
