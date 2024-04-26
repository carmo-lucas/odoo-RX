from odoo import models, fields

class RxRegulatoryClassification(models.Model):
    _name="rx.regulatory.classification"
    _description="Regulatory Organizations"

    name = fields.Char(string="Name", required=True, size = 64)
    abbreviation = fields.Char(string="Abbreviation", required=True, size=12)