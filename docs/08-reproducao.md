# 08 — Abrir, compilar e executar no Quartus II

## Pré-requisitos

Recomenda-se usar o ambiente original indicado no pacote: **Quartus II 13.0 SP1**, compatível com o dispositivo **Cyclone II EP2C20F484C7** da placa DE1 clássica. O projeto não é para DE10-Standard, e Quartus Prime mais novo pode não oferecer suporte a essa FPGA.

## Passo a passo

1. Clonar ou baixar este repositório completo.
2. Abrir `projeto/DE1_Filtro.qpf` em **File → Open Project**.
3. Conferir a revisão/topo `DE1_Filtro` e o dispositivo `EP2C20F484C7`.
4. Abrir [`DE1_Filtro.bdf`](../projeto/DE1_Filtro.bdf) e verificar os blocos `LPM_COUNTER`, `LPM_ROM`, `LPM_ADD_SUB`, `LPM_COMPARE`, `DFF` e portas lógicas.
5. Conferir o arquivo ROM `Imagem_Ruidosa_DE1.mif` na mesma pasta e os dois BDF adicionados em **Assignments → Settings → Files**.
6. Revisar os pinos via **Assignments → Pin Planner**, tomando [`DE1_Filtro.qsf`](../projeto/DE1_Filtro.qsf) como referência.
7. Executar inicialmente **Processing → Start Analysis & Synthesis** e verificar a janela de mensagens.
8. Se não houver erro, executar **Processing → Start Compilation**. Conferir relatório do Fitter, Timing Analyzer e arquivo `.sof` gerado.
9. Conectar a DE1 ao monitor VGA e USB-Blaster. Programar o `.sof` pela ferramenta **Programmer**, modo **JTAG**.
10. Acionar `KEY0` para reinicializar e escolher os filtros pelas chaves `SW0..SW2`.

## Sobre o `LEIA-ME.txt`

O pacote contém uma explicação de ajustes já realizados nos pinos do editor esquemático e em conexões que se sobrepunham. Esse registro **não é prova de compilação**; indica que os arquivos foram preparados para nova verificação no Quartus.

## Registros disponíveis

As [fotografias da saída VGA](../resultados_vga/README.md) documentam os efeitos visuais observados no monitor. Os arquivos disponibilizados não incluem diagramas de ondas nem relatórios completos de uma compilação comprovadamente bem-sucedida. Os resultados fotografados não substituem a verificação dos detalhes temporais no Quartus.

---
[Anterior](07-saida.md) · [Índice](../README.md#repositório-e-tutorial) · [Próximo: validação](09-validacao.md)
