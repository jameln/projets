from odoo import api, models

class ParticularReport(models.AbstractModel):
    _name = 'report.tjara_facture.report_facture'
    @api.model
    def render_html(self, docids, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('t-jara.report_facture')
        docargs = {
            'doc_ids': docids,
            'doc_model': 't-jara.facture',
            'docs': self,
        }
        return report_obj.render('t-jara.report_facture', docargs)