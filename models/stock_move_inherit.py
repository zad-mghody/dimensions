from odoo import models, fields, api


class StockMove(models.Model):
    _inherit = 'stock.move'

    product_dimension = fields.Char(string="Dimension", compute='_compute_dimension', store=True)

    @api.depends('sale_line_id.product_dimension')
    def _compute_dimension(self):
        for rec in self:
            for line in rec.sale_line_id:
                rec.product_dimension = line.product_dimension
