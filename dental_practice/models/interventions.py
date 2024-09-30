# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.http import request

class OdooExpInterventions(models.Model):
    _name = 'dental.intervention'
    _description = 'Dental Intervention'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date desc'

    name = fields.Char(string='Intervention Name', required=True)
    patient_id = fields.Many2one('res.partner', string='Patient', required=True, domain=[('is_patient', '=', True)])
    date = fields.Date(string='Date', default=fields.Date.context_today, required=True)
    intervention_type = fields.Selection([
        ('cleaning', 'Cleaning'),
        ('sealant', 'Sealant'),
        ('fluoride', 'Fluoride Treatment'),
    ], string='Intervention Type', required=True)
    tooth_number = fields.Char(string='Tooth Number')
    notes = fields.Text(string='Notes')
    # using product.product for Interventions and Treatments
    product_id = fields.Many2one('product.product', string='Intervention Product')
    appointment_id = fields.Many2one('calendar.event', string='Appointment')
