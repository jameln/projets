# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Produit(models.Model):

    _name = 'tjara.produit'

    name = fields.Char(
        string='Appelation',
        required=True,
        index=True,
        help='Le nom du produit',
        size=50,
        default=lambda self: self.env['ir.sequence'].next_by_code('tjara.facture.seq')
    )

    code = fields.Char(
        string='Code',
        required=True,
        index=True,
        help='Le code du produit',
        size=50
    )

    lignefacture_id = fields.One2many(
        string='Ligne Facture',
        comodel_name='tjara.ligne_facture',
        inverse_name='produit',
    )

    qte = fields.Float(
        string='Quantite',
        required=True,
        default=1.0,
        digits=(16, 3)
    )
