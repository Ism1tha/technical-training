from odoo import models, fields, api, _

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Property Offers'

    PRICE_STATES = [
        ('accepted', 'Acceptada'),
        ('rejected', 'Rebutjada'),
        ('processing', 'En tractament')
    ]

    price = fields.Float(string='Preu', digits=(10, 2))
    state = fields.Selection(string='Estat', selection=PRICE_STATES, default='processing')
    buyer_id = fields.Many2one('res.partner', string='Comprador', domain="[('is_company','=',False)]")
    comments = fields.Text(string='Comentaris')
    property_id = fields.Many2one('estate.property', string='Propietat')

    @api.model
    def create(self, vals):
        offer = super(EstatePropertyOffer, self).create(vals)
        if offer.property_id.state == 'new':
            offer.property_id.write({'state': 'offer_received'})
        return offer

    def write(self, vals):

        if 'state' in vals and vals['state'] == 'accepted':
            offers_to_write = self.filtered(lambda o: 'state' in vals and vals['state'] == 'accepted')
            for offer in offers_to_write:
                offer.property_id.write({
                    'buyer': offer.buyer_id.id,
                    'sale_price': offer.price,
                    'state': 'offer_accepted'
                })
            
        elif 'state' in vals and vals['state'] == 'processing':
            print('processing state')
            offers_to_write = self.filtered(lambda o: 'state' in vals and vals['state'] == 'processing')
            for offer in offers_to_write:
                offer.property_id.write({
                    'state': 'offer_received'
                })
        
        return super(EstatePropertyOffer, self).write(vals)