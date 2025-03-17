from odoo import models, fields, api

class ProjectProject(models.Model):
    _inherit = 'project.project'

    project_type = fields.Selection([
        ('internal', 'Internal'),
        ('client', 'Client'),
        ('government', 'Government')
    ], string="Project Type")

    industry_type = fields.Selection([
        ('technology', 'Technology'),
        ('finance', 'Finance'),
        ('healthcare', 'Healthcare'),
        ('retail', 'Retail')
    ], string="Industry Type")

    client_priority = fields.Selection([
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low')
    ], string="Client Priority")

    risk_assessment = fields.Many2one('res.partner', string="Risk Assessment")

    expected_revenue = fields.Float(string="Expected Revenue")

    contract_signed = fields.Boolean(string="Contract Signed")
    contract_start_date = fields.Date(string="Contract Start Date")
    contract_end_date = fields.Date(string="Contract End Date")


    @api.onchange('project_type')
    def enable_industry_type(self):
        """Compute whether to show the Industry Type field."""
        if self.project_type == 'internal':
            self.industry_type = False


    @api.onchange('client_priority')
    def enable_risk_assessment(self):
        """Compute whether to show the Risk Assessment field."""
        if self.client_priority != 'high':
            self.risk_assessment = False