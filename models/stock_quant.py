from odoo import models, fields, api
from datetime import timedelta

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    @api.model
    def check_expiry_and_adjust_stock(self):
        products = self.env['product.template'].search([('expiry_date', '<=', fields.Date.today() + timedelta(days=30))])
        for product in products:
            quant = self.env['stock.quant'].search([('product_id', '=', product.id)], limit=1)
            if quant:
                # Create stock adjustment entry
                stock_adjustment = self.env['stock.inventory'].create({
                    'name': f'Expiry Adjustment for {product.name}',
                    'location_id': quant.location_id.id,
                    'state': 'draft',
                })
                # Write off the stock
                self.env['stock.inventory.line'].create({
                    'inventory_id': stock_adjustment.id,
                    'product_id': product.id,
                    'product_qty': quant.quantity,
                    'location_id': quant.location_id.id,
                })
                stock_adjustment.action_confirm()
                stock_adjustment.action_done()
