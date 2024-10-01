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
    treatment_id = fields.Many2many('dental.treatment', string='Intervention')
    teeth = fields.Many2many("dental.tooth", string='Teeth for treatment')

class Tooth(models.Model):
    _name = 'dental.tooth'
    _description = 'Tooth, according to the standard numeration'

    quarter = fields.Selection([("1", "1"), ("2", "2"), ("3", "3"), ("4", "4")], string='Quarter')
    position = fields.Selection([("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"), ("7", "7"), ("8", "8")], string='Position')
    name = fields.Char(string='Tooth Number', compute='_compute_tooth_name')

    @api.depends('quarter', 'position')
    def _compute_tooth_name(self):
        for record in self:
            record.name = f'{record.quarter}{record.position}'