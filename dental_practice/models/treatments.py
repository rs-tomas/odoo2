# -*- coding: utf-8 -*-
from odoo import api, fields, models, api
from odoo.http import request

class OdooExpTreatment(models.Model):
    _name = 'sale.order'
    _description = 'empty model for odooexp.treatments'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'sale.order']
    _order = 'id desc'

    name = fields.Char(string='Name')
    patient_id = fields.Many2one('odooexp.patients', string='Patient')
    patient_claims = fields.Text(string='Patient Claims')
    # treatment_date = fields.Date(string='Treatment Date')
    treatment_duration = fields.Integer(string='Treatment Duration')
    treatment_profile = fields.Many2one('odooexp.treatment_profile', string='Treatment Profile')
    treatment_cost = fields.Float(string='Treatment Cost') # Replace with calculated field, after adding interventions
    # treatment_interventions = fields.One2many('odooexp.treatment_interventions', 'treatment_id', string='Interventions') # Add this after adding interventions
    teeth = fields.Many2many("odooexp.tooth", string='Teeth for treatment')


class TreatmentProfile(models.Model):
    _name = 'odooexp.treatment_profile'
    _description = 'Treatment profile'

    name = fields.Selection([("Therapy", "Therapy"), ("Surgery", "Surgery"), ("Orthodontics", "Orthodontics")], string='Treatment Profile')
    description = fields.Text(string='Description')


class Tooth(models.Model):
    _name = 'odooexp.tooth'
    _description = 'Tooth, according to the standard numeration'

    quarter = fields.Selection([("1", "1"), ("2", "2"), ("3", "3"), ("4", "4")], string='Quarter')
    tooth = fields.Selection([("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"), ("7", "7"), ("8", "8")])
    tooth_number = fields.Integer(string='Tooth Number', compute='_compute_tooth_number')

    @api.depends('quarter', 'tooth')
    def _compute_tooth_number(self):
        for record in self:
            record.tooth_number = int(record.quarter) * 10 + int(record.tooth)
