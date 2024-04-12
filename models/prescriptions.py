from odoo import models, fields, api, _

TIPO_USO = [
    ("i", "Interno"),
    ("e", "Externo"),
    ("t", "Topico"),
    ("a", "Intraretal"),
    ("o", "Ocular"),
    ("n", "Nasal"),
]

FORMA_FARMACEUTICA = [
    ("cap", "Cápsula"),
    ("com", "Comprimido"),
    ("env", "Envelope"),
    ("pas", "Pastilha"),
    ("bis", "Biscoito"),
    ("pat", "Patch"),
    ("fil", "Filme"),
    ("cre", "Creme"),
    ("loc", "Loção"),
    ("xpu", "Xampu"),
    ("gel", "Gel"),
    ("pmd", "Pomada"),
    ("pst", "Pasta"),
    ("xap", "Xarope"),
    ("soo", "Solução Oral"),
    ("sol", "Solução"),
    ("hom", "Homeopatia"),
    ("flo", "Floral"),
    ("inj", "Injetável"),
]


class RxPrescription(models.Model):
    _name = "rx.prescription"
    _description = "Professional Prescription"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    ref = fields.Char(string="Reference", default=lambda self: _("New"))
    status = fields.Selection(
        string="Status",
        selection=(
            [
                ("sol", "Solicitado"),
                ("val", "Validado"),
                ("rep", "Reprovado"),
            ]
        ),
        tracking=True,
    )
    issuedDate = fields.Date(string="Issued Date", required=True, tracking=True)
    patient_id = fields.Many2one(
        string="Patient", comodel_name="res.partner", required=True
    )
    client_id = fields.Many2one(
        string="Client", comodel_name="res.partner", required=True
    )
    prescriber_id = fields.Many2one(
        string="Prescriber", comodel_name="res.partner", required=True
    )
    quantidadeFormula = fields.Integer(string="Quantity Expected")
    observation = fields.Html(
        string="Observations", help="Observations for this prescription"
    )
    unidadeMedida_id = fields.Many2one(string="Units", comodel_name="uom.uom")

    tipoUso = fields.Selection(
        string="Product Use",
        required=True,
        selection=TIPO_USO,
    )
    formaFarmaceutica = fields.Selection(
        string="Farmaceutical Form", required=True, selection=FORMA_FARMACEUTICA
    )

    prescription_line_ids = fields.One2many(
        "rx.prescription.lines",
        "prescription_id",
        string="Prescription Components",
    )

    @api.onchange("formaFarmaceutica")
    def _onchange_formaFarmaceutica(self):
        if self.formaFarmaceutica == "cap":
            self.tipoUso = "i"

    # Generates reference code for the prescription
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals["ref"] = self.env["ir.sequence"].next_by_code("rx.prescription")
        return super(RxPrescription, self).create(vals_list)


class RxPrescriptionLines(models.Model):
    _name = "rx.prescription.lines"
    _description = "Prescription Components"

    product_id = fields.Many2one(string="Product", comodel_name="product.product")
    dose = fields.Float(string="Dose", digits=(10, 2))
    unidadeMedida_id = fields.Many2one(string="Unit", comodel_name="uom.uom")
    prescription_id = fields.Many2one(
        string="Prescription", comodel_name="rx.prescription"
    )
