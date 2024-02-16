from odoo import models, fields

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Property Offers'

    price = fields.Float(string='Price', digits=(10, 2))
    property_id = fields.Many2one('estate.property', string='Property')