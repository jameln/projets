# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LigneFacture(models.Model):

    _name = 'tjara.ligne_facture'

    quantite = fields.Float(
        string='Quantite',
        required=True,
        default=1.0,
        digits=(16, 3)
    )

    produit = fields.Many2one(
        string='Produit',
        required=True,
        index=True,
        comodel_name='tjara.produit',
        ondelete='set null'
    )

    facture_id = fields.Many2one(
        required=True,
        index=True,
        comodel_name='tjara.facture',
        ondelete='cascade'
    )

    prix_total = fields.Float(
        string='Prix TTC',
        compute="prixtot",
        digits=(16, 3)
    )
    
    @api.depends("quantite")
    def prixtot(self):
        for lf in self:
            lf.prix_total = lf.quantite * 1000
