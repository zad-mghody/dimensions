from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    dimension = fields.Char(string="Dimension", default="2cm * 4cm")


