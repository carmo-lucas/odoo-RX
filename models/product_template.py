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

    classificacao_regulatoria_ids = fields.Many2many(
        comodel_name="rx.regulatory.classification",
        string="Entidades Reguladoras",
        help="Ao selecionar as entidades será possível gerar relatórios no formato especificado pelas respectivas plataformas das entidades.",
    )

    dcb = fields.Char(string="Denominação Comum Brasileira", size=20, trim=False)
    cas = fields.Char(string="CAS", size=12, trim=False)
    classe_SNGPC = fields.Selection(
        string="Classe SNGPC",
        selection=[("1", "Controle Especial"), ("2", "Antimicrobiano")],
    )
