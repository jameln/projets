from odoo import api, fields, models

class tjara_produit_cron(models.Model):
    
    _name= 'tjara.produit.cron'
    
    
    def create_product(self):
        print '==================cron'
        self.env['tjara.produit'].create({
            'code' : '123456'
            })
        return True