import re


RE_NF = re.compile(r"\bN[ºo°]\.?\s*(\d+)\b", re.IGNORECASE)
RE_DADOS_TABELA = re.compile(r"DADOS\s+DOS\s+PRODUTOS", re.IGNORECASE)
RE_STOP_SECTION = re.compile(
    r"C[ÁA]LCULO\s+DO\s+IMPOSTO|C[ÁA]LCULO\s+DO\s+ISSQN|DADOS\s+ADICIONAIS",
    re.IGNORECASE,
)

IGNORAR_LINHAS_PREFIX = ("DADOS DOS PRODUTOS", "CÓD. PROD.")