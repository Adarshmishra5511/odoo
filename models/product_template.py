from odoo import models, fields

class ProductTemplate(models.Model):
    _name = 'product.template'

    batch_number = fields.Char('Batch Number')
    expiry_date = fields.Date('Expiry Date')
