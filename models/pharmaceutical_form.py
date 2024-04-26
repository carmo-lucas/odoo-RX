from odoo import models, fields, api, _


class RxPharmaceuticalForm(models.Model):
    _name = "rx.pharmaceutical.form"
    _description = "Product Pharmaceutical Form"

    name = fields.Char(string="Pharmaceutical Form", size=128, required=True)
    description = fields.Text(string="Description")
    solid_state = fields.Selection(
        string="Physical State",
        selection=[
            ("solid", "Solid"),
            ("liquid", "Liquid"),
            ("semissolid", "Semissolid"),
            ("other", "Other"),
        ],
    )


#     FORMA_FARMACEUTICA = [
#     ("inj", "Injetável"),
#     ("cap", "Cápsula"),
#     ("com", "Comprimido"),
#     ("env", "Envelope"),
#     ("pas", "Pastilha"),
#     ("bis", "Biscoito"),
#     ("pat", "Patch"),
#     ("fil", "Filme"),
#     ("cre", "Creme"),
#     ("loc", "Loção"),
#     ("xpu", "Xampu"),
#     ("gel", "Gel"),
#     ("pmd", "Pomada"),
#     ("pst", "Pasta"),
#     ("xap", "Xarope"),
#     ("soo", "Solução Oral"),
#     ("sol", "Solução"),
#     ("hom", "Homeopatia"),
#     ("flo", "Floral"),
#     ("ovu", "Óvulo"),
# ]
