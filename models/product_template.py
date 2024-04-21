from odoo import models, fields, api, _


class ProductTemplateInherit(models.Model):
    _inherit = "product.template"

    fator_diluicao_numerador = fields.Integer(string="Parte")
    fator_diluicao_denominador = fields.Integer(string="Todo")
    lista_344 = fields.Selection(
        string="Lista",
        selection=[
            ("a1", "A1 - Entorpecentes"),
            ("a2", "A2 - Entorpecentes"),
            ("a3", "A3 - Psicotrópicas"),
            ("b1", "B1 - Psicotrópicas"),
            ("b2", "B2 - Anorexígenas"),
            ("c1", "C1 - Outras"),
            ("c2", "C2 - Retinóicas"),
            ("c3", "C3 - Imunossupressoras"),
            ("c4", "C4 - Anti-retrovirais"),
            ("c5", "C5 - Anabolizantes"),
        ],
    )
    classificacao_regulatoria = fields.Selection(
        string="Entidades Reguladoras",
        help="Ao selecionar as entidades será possível gerar relatórios no formato especificado pelas respectivas plataformas das entidades.",
        selection=[
            ("pf", "Polícia Federal (MAPAS)"),
            ("pc", "Polícia Civíl"),
            ("ex", "Exército"),
            ("ms", "SNGPC"),
        ],
    )

    dcb = fields.Char(string="Denominação Comum Brasileira", size=20, trim=False)
    cas = fields.Char(string="CAS", size=12, trim=False)
    classe_terapeutica = fields.Selection(
        string="Classe Terapêutica",
        selection=[("1", "Controle Especial"), ("2", "Antimicrobiano")],
    )
