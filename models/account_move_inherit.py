from odoo import models, fields, api


class StockMoveLine(models.Model):
    _inherit = 'account.move.line'

    product_dimension = fields.Char(string="Dimension")
