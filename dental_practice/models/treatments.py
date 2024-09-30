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
    treatment_type = fields.Selection([
        ('filling', 'Filling'),
        ('root_canal', 'Root Canal'),
        ('extraction', 'Extraction'),
        ('crown', 'Crown'),
        # Add more types as needed
    ], string='Treatment Type', required=True)
    tooth_number = fields.Char(string='Tooth Number')
    cost = fields.Float(string='Cost', required=True)
    notes = fields.Text(string='Notes')
    invoice_id = fields.Many2one('account.move', string='Invoice', readonly=True)
    product_id = fields.Many2one('product.product', string='Treatment Product')
    appointment_id = fields.Many2one('calendar.event', string='Appointment')
