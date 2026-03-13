from dataclasses import dataclass


@dataclass
class NfItem:
    codigo_produto: str
    descricao: str
    ncm_sh: str
    cst: str
    cfop: str
    unidade: str
    quantidade: str
    valor_unitario: str
    valor_total: str
    bc_icms: str
    valor_icms: str
    valor_ipi: str
    aliquota_icms: str
    aliquota_ipi: str
    numero_nf: str

    def to_row(self) -> list[str]:
        return [
            self.codigo_produto,
            self.descricao,
            self.ncm_sh,
            self.cst,
            self.cfop,
            self.unidade,
            self.quantidade,
            self.valor_unitario,
            self.valor_total,
            self.bc_icms,
            self.valor_icms,
            self.valor_ipi,
            self.aliquota_icms,
            self.aliquota_ipi,
            self.numero_nf,
        ]