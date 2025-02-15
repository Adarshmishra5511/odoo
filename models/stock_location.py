from odoo import models, fields

class StockLocation(models.Model):
    _name = 'stock.location'

    auto_adjust_stock = fields.Boolean('Auto Adjust Stock', default=False)
