from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    dimension_flag = fields.Boolean(string='Dimension Flag')

    @api.constrains('user_id')
    def check_current_user(self):
        flag = self.env.user.id == self.user_id.id
        self.dimension_flag = flag
