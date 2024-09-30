# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.http import request

class OdooExpInterventions(models.Model):
    _name = 'dental.intervention'
    _description = 'Dental Intervention'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date desc'

    name = fields.Char(string='Intervention Name', required=True)
    date = fields.Date(string='Date', default=fields.Date.context_today, required=True)
    notes = fields.Text(string='Notes')
    # using product.product for Interventions and Treatments
    product_id = fields.Many2one('product.product', string='Intervention Product')
    tratement_id = fields.Many2one('dental.intervention', string='Intervention')