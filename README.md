# Filtros de imagem em FPGA

Projeto da disciplina de Sistemas Digitais, do curso de Engenharia de Computação da Universidade Federal de São Carlos (UFSCar).

O circuito foi desenvolvido para a placa **Terasic DE1**, com FPGA **Cyclone II EP2C20F484C7**. A imagem binária é lida de uma ROM, passa por circuitos de filtragem e é apresentada em um monitor VGA. A lógica principal está no esquemático `filtroimagem.bdf`, com blocos auxiliares do Quartus descritos em Verilog e VHDL.

## Arquivos do projeto

- `filtroimagem.7z`: pacote integral do projeto, incluindo os registros de compilação.
- `projeto/filtroimagem.qpf`: projeto Quartus.
- `projeto/filtroimagem.qsf`: dispositivo, arquivos associados e atribuições de pinos.
- `projeto/filtroimagem.bdf`: circuito principal.
- `projeto/Imagem_Ruidosa.mif`: conteúdo da memória de imagem binária.
- `projeto/ROM.*`, `projeto/shiftreg.*`, `projeto/add_sub.*` e `projeto/sub.*`: blocos auxiliares e símbolos.
- `projeto/VGA_SYNC.*` e `projeto/Video_PLL.vhd`: temporização de vídeo e geração do clock de pixel.

Os arquivos da pasta `projeto/` foram retirados do pacote principal, sem alterações no circuito.

## Funcionamento

O módulo `VGA_SYNC` recebe o clock de 50 MHz e utiliza a PLL para fornecer um clock de pixel de 25 MHz. Os contadores de vídeo seguem uma temporização de referência de 640 × 480 pixels, com 800 contagens horizontais e 525 verticais por quadro. A região da imagem é endereçada por 15 bits, reunindo sete bits da linha e oito da coluna. O arquivo MIF declara **32.767 posições de um bit**.

Um conjunto de atrasos de linha (`ALTSHIFT_TAPS`, com distância de 256 posições) e registradores (`shiftreg`) disponibiliza os dados em janelas 3 × 3. Nas operações lógicas de máximo e mínimo, as portas `OR8` e `AND8` utilizam os **oito vizinhos do pixel central**. A posição central não entra nessas duas reduções.

As chaves `SW[2..0]` controlam o multiplexador de cinco entradas:

| SW[2..0] | Saída selecionada | Descrição |
|:--:|---|---|
| `000` | Imagem original | Bit lido da ROM |
| `001` | Filtro de máximo | OR dos oito vizinhos |
| `010` | Filtro de mínimo | AND dos oito vizinhos |
| `011` | Composição de filtros | Máximo aplicado após mínimo e máximo |
| `100` | Detector de bordas | XOR entre máximo e mínimo calculados sobre a saída da composição |

As combinações `101`, `110` e `111` não correspondem a entradas definidas do multiplexador de cinco posições. O bit de saída passa por uma condição de habilitação e é entregue aos canais VGA de maneira monocromática.

## Abrir e compilar

1. Utilizar o **Quartus II 13.0 SP1** para o dispositivo Cyclone II indicado.
2. Abrir `projeto/filtroimagem.qpf` e manter os arquivos associados na mesma pasta.
3. Conferir as atribuições em `filtroimagem.qsf`, especialmente a entrada `clock_50Mhz`.
4. Executar **Processing > Start Compilation** e consultar os avisos apresentados.
5. Para utilizar a placa, revisar a configuração do Programmer e os pinos antes da gravação.

O pacote contém um relatório de compilação **concluída com sucesso em 16/11/2026**, realizado no Quartus II 13.0 SP1. O relatório informa 186 elementos lógicos, 120 registradores, 34.800 bits de memória e uma PLL. Também registra a ausência de um arquivo `.sdc` para restrições temporais e um aviso sobre atribuição exata de pino. Por isso, o término da compilação não deve ser confundido com validação completa de temporização ou funcionamento físico na placa.

## Referência

Os arquivos de projeto e os relatórios de compilação estão reunidos em `filtroimagem.7z`, que constitui a referência para esta implementação.
