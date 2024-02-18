from odoo import models, fields

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
        if 'state' in vals and 'accepted' in vals['state']:

            # Obtenim els registres de les ofertes que es modificarà
            offers_to_write = self.filtered(lambda o: 'state' in vals and vals['state'] == 'accepted')
            
             # Truquem al mètode write del model EstatePropertyOffer
            res = super(EstatePropertyOffer, offers_to_write).write(vals)
            
            # Actualitzem el comprador i el preu de venda de la propietat corresponent
            for offer in offers_to_write:
                offer.property_id.write({
                    'state': 'sold', # Cambiamos el estado de la propiedad a 'offer_accepted
                    'buyer': offer.buyer_id.id,
                    'sale_price': offer.price
                })
        
        return res