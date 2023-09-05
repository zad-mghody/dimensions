from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_dimension = fields.Char(string='Dimension', store=True, readonly=False, tracking=True)
    dim_flag = fields.Boolean(related='order_id.dimension_flag')

    first_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')

    @api.onchange('product_id')
    def _on_change_dimension(self):
        self.product_dimension = self.product_template_id.dimension

    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        res['product_dimension'] = self.move_ids.mapped("product_dimension")[0]
        return res

    @api.constrains('first_date', 'end_date')
    def is_date_available(self):
        s_date = self.first_date
        e_date = self.end_date
        for rec in self:
            if s_date == rec.first_date and rec.end_date or e_date == rec.first_date and rec.end_date:
                raise ValidationError("Date used before!!!!")

