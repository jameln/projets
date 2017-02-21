# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.exceptions import ValidationError
from odoo import api, fields, models


class Facture(models.Model):


    _name = 'tjara.facture'

    name = fields.Char(
        string='N° facture',
        required=True,
        index=True,
        size=50,
        default=lambda self: self.env['ir.sequence'].next_by_code('tjara.facture.seq')
    )
    

    dateFact = fields.Datetime(
        string='Date facture',
        required=True,
        default=fields.datetime.now(),
        help='La date de création de la facture'
    )

    description = fields.Text(
        string='Commentaire',
        required=False,
        help='Champ libre pour la saisie de commentaires'
    )

    lignes_id = fields.One2many(
        string='Lignes Facture',
        comodel_name='tjara.ligne_facture',
        inverse_name='facture_id',
    )

    state = fields.Selection(
        string='Etat',
        default='sa',
        selection=[
            ('sa', 'Saisie'),
            ('br', 'Brouillon'),
            ('va', 'Validee'),
            ('pa', 'Payee'),
            ('an', 'Annulee')
        ]
    )

    valid = fields.Boolean(
        string='Ne pas annuler',
        default=False
    )
    client_id=fields.Many2one('res.partner',string="Client",ondelete='restrict')
    
    attachment=fields.One2many(         
        'ir.attachment','facture_rel',string='Pièce jointe',
        )
    
    _sql_constraints = [
        ('facture_uniq', 'unique (name)', 'The code of the invoice must be unique per company !')
    ]    

    def write(self, values):
        print values
        if values.has_key('state'):
            if values.get('state') == 'sa':
                values['state'] = 'br'
        result = super(Facture, self).write(values)
        return result

    @api.multi
    def afficher(self):
        print "afficher()"
        raise ValidationError('id facture : ' + str(self.id))
        return True

    def fct_brouillon(self):
        self.write({'state': 'br'})
        return True

    @api.one
    def fct_valider(self):
        
#         values = {}
#         company_pool= self.env['res.company'] #societe
#         mail_server_pool = self.env['ir.mail_server'] # smtp
#         email_temp_pool = self.env['mail.template'] #template
#         mail_mail_pool = self.env['mail.mail'] # envoie
#         pcejointe_pool = self.env['ir.attachment'] # pce jointe
#          
#          
#         company=self.env.user.company_id  
#          
#                
#         file_name= self.name
#         email_to=self.client_id.email
#         email_cc=company.email
#         mail_server_id = mail_server_pool.search([],limit=1,order='sequence')
#         print 'self.client_id',self.client_id
#         
#         template_ids= email_temp_pool.search([('name','=','tjara_facture_temp')])
#         if template_ids:
#            values = email_temp_pool.with_context(client=self.client_id.name).generate_email( template_ids)
#            if email_cc:
#                        values['email_cc']=email_cc
#                        values['email_to'] = email_to
#                        values['email_from'] = mail_server_pool.browse(mail_server_id[0]).smtp_user
#                        values['res_id'] = False
#                        values['subject'] = file_name
#                        msg_id = mail_mail_pool.sudo().create(values)
#                        if msg_id :
#                            pce_jointe = []    
#                            if attachment.pcejointes_ids:
#                                for pce in attachment.pcejointes_ids: 
#                                    pce_jointe.append(pce.id)
#                                 
#                            if pce_jointe:
#                                mail_mail_pool.sudo().write(msg_id, {'attachment_ids': [(6, 0, pce_jointe)]})
#                            mail_mail_pool.sudo().send([msg_id])
                           
        self.write({
            'state': 'va',
            'description': 'facture valide le: ' +
                           fields.datetime.now().strftime('%d/%m/%Y %H:%M')
        })
        return True

    def fct_payer(self):
        self.write({'state': 'pa'})
        return True

    def fct_annuler(self):
        if self.valid:
            raise ValidationError("Cette facture est verouillee!")
        self.write({'state': 'an'})
        return True


class FactureTemp(models.Model):
    _name = "tjara.facturetemp"

    def valider(self):
        for facture_id in self.env.context.get('active_ids'):
            print facture_id
        print self.create_uid.name
        return True
    
class Attachment(models.Model):

    _inherit = 'ir.attachment'
    _name = 'ir.attachment'
    
    facture_rel = fields.Many2one(
        'tjara.facture',
        string="Facture"
    )     
