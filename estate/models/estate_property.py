from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"
    name = fields.Char('Propietat Inmobiliaria', required=True)
    description = fields.Text('Descripció')
    postcode = fields.Char('Codi Postal')
    date_availability = fields.Date('Data Disponibilitat')
    selling_price = fields.Float('Preu de Venda')
    bedrooms = fields.Integer('Habitacions')