from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

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

    def write(self, vals):

        if any(offer.state == 'accepted' for offer in self):
            raise ValidationError(_('No es poden modificar ofertes de una propietat si ja s\'ha acceptat una oferta.'))

        if 'state' in vals and vals['state'] == 'accepted':
            offers_to_write = self.filtered(lambda o: 'state' in vals and vals['state'] == 'accepted')
            for offer in offers_to_write:
                offer.property_id.write({
                    'buyer': offer.buyer_id.id,
                    'sale_price': offer.price,
                    'state': 'offer_accepted'
                })
            
        if 'state' in vals and vals['state'] == 'processing':
            offers_to_write = self.filtered(lambda o: 'state' in vals and vals['state'] == 'processing')
            for offer in offers_to_write:
                offer.property_id.write({
                    'state': 'offer_received'
                })
            
        return super(EstatePropertyOffer, self).write(vals)