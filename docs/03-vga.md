# 03 — Temporização e janela VGA

## Geração de clock

O flip-flop `inst4` recebe em `D` o inverso da própria saída `CLK25`, sendo acionado na borda de `CLOCK_50` (50 MHz). Dessa forma, o período de `CLK25` é aproximadamente 40 ns, ou **25 MHz**. Aqui há um sinal de clock dividido, diferentemente de um circuito que use apenas habilitação de clock.

## Varredura

Os contadores `LPM_COUNTER` de 10 bits possuem módulo **800** para `H` e **525** para `V`. O contador vertical avança quando `H_LAST` indica o último valor da linha (`H=799`).

| Comparação lógica | Efeito |
|---|---|
| `H < 96` | `H_SYNC_PULSE`, invertido em `VGA_HS` |
| `V < 2` | `V_SYNC_PULSE`, invertido em `VGA_VS` |
| `144 ≤ H ≤ 399` | Máscara horizontal `VISIBLE_X` de 256 pixels |
| `35 ≤ V ≤ 162` | Máscara vertical `VISIBLE_Y` de 128 pixels |
| `VISIBLE_X AND VISIBLE_Y` | Máscara final `IMG_MASK` |

O quadro completo contém 800 × 525 contagens. A taxa nominal de atualização é **25 MHz / (800 × 525) ≈ 59,52 Hz**. Apenas uma região de 256 × 128 é utilizada para a imagem; o restante depende do valor de saída mascarado.

## Reset

`KEY[0]` é ativo em zero. Um inversor gera `RESET` para o `aclr` dos contadores; o botão também é ligado à limpeza assíncrona dos flip-flops e dos atrasos.

Os parâmetros de sincronismo são os que constam no BDF. Não há arquivo de simulação VGA ou registro de teste físico incluído no projeto original.

---
[Anterior](02-arquitetura.md) · [Índice](../README.md#repositório-e-tutorial) · [Próximo: ROM](04-memoria.md)
