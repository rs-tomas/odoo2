# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.http import request

class DentalTreatment(models.Model):
    _name = 'dental.treatment'
    _description = 'Dental Treatment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date desc'

    name = fields.Char(string='Treatment Name', required=True)
    patient_id = fields.Many2one('res.partner', string='Patient', required=True, domain=[('is_patient', '=', True)])
    date = fields.Date(string='Date', default=fields.Date.context_today, required=True)
    #tooth_number = fields.Char(string='Tooth Number')

    notes = fields.Text(string='Notes')
    invoice_id = fields.Many2one('account.move', string='Invoice', readonly=True)
    interventions_ids = fields.Many2many('dental.intervention', string='Interventions')
