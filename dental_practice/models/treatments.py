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
    end_date = fields.Date(string='End Date')
    #tooth_number = fields.Char(string='Tooth Number')

    notes = fields.Text(string='Notes')
    # invoice_id = fields.Many2one('account.move', string='Invoice', readonly=True)
    interventions_ids = fields.Many2many('dental.intervention', string='Interventions')
    sales_order_id = fields.Many2one('sale.order', string='Sales Order', readonly=True)
    profile = fields.Selection([("Therapy", "Therapy"), ("Surgery", "Surgery"), ("Orthodontics", "Orthodontics")], string='Treatment Profile')
    teeth = fields.Many2many("dental.tooth", string='Teeth for treatment')



class Tooth(models.Model):
    _name = 'dental.tooth'
    _description = 'Tooth, according to the standard numeration'

    quarter = fields.Selection([("1", "1"), ("2", "2"), ("3", "3"), ("4", "4")], string='Quarter')
    position = fields.Selection([("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"), ("7", "7"), ("8", "8")], string='Position')
    name = fields.Integer(string='Tooth Number', compute='_compute_tooth_name')

    @api.depends('quarter', 'position')
    def _compute_tooth_name(self):
        for record in self:
            record.name = int(record.quarter) * 10 + int(record.position)
