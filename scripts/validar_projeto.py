#!/usr/bin/env python3
"""Validação ESTÁTICA de inventário e parâmetros; não substitui o Quartus."""
from pathlib import Path
import re
BASE = Path(__file__).resolve().parents[1] / 'projeto'
required = ['DE1_Filtro.qpf', 'DE1_Filtro.qsf', 'DE1_Filtro.bdf', 'Filtro3x3_Referencia.bdf', 'Imagem_Ruidosa_DE1.mif', 'LEIA-ME.txt']
for name in required:
    assert (BASE / name).is_file(), f'Arquivo ausente: {name}'
qsf = (BASE / 'DE1_Filtro.qsf').read_text(encoding='utf-8')
bdf = (BASE / 'DE1_Filtro.bdf').read_text(encoding='utf-8')
mif = (BASE / 'Imagem_Ruidosa_DE1.mif').read_text(encoding='utf-8')
for term in ['EP2C20F484C7','TOP_LEVEL_ENTITY DE1_Filtro','BDF_FILE DE1_Filtro.bdf','BDF_FILE Filtro3x3_Referencia.bdf','MIF_FILE Imagem_Ruidosa_DE1.mif']:
    assert term in qsf, f'QSF não contém: {term}'
for term in ['LPM_COUNTER','LPM_ROM','LPM_ADD_SUB','LPM_COMPARE','DFF','MAX9','MIN9','GRADIENT','SELECTED','IMG_MASK']:
    assert term in bdf, f'Esquemático não contém: {term}'
assert bdf.count('(text "LPM_ROM"') == 3, 'Esperadas 3 ROMs'
assert '"800"' in bdf and '"525"' in bdf, 'Modulos de VGA ausentes'
assert re.search(r'\bWIDTH=1;',mif)
assert re.search(r'\bDEPTH=32768;',mif)
rows = re.findall(r'^([0-9A-Fa-f]{4}):([01]);\s*$', mif, re.M)
assert len(rows) == 32768, f'Quantidade incorreta de pixels: {len(rows)}'
assert len({int(a,16) for a,b in rows}) == 32768, 'Endereços repetidos'
assert all(int(a,16)==i for i,(a,b) in enumerate(rows)), 'Endereços não sequenciais'
ones = sum(int(bit) for _,bit in rows)
print(f'OK - Arquivos e parâmetros estruturais coerentes. MIF: {len(rows)} bits, {ones} em 1; {len(rows)-ones} em 0.')
print('AVISO: compilação Quartus, simulação HDL e teste VGA NÃO foram executados.')
