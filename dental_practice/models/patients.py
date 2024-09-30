# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.http import request

class OdooExpPatients(models.Model):
    _name = 'odooexp.patients'
    _description = 'empty model for odooexp.patients'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    name = fields.Char(string='Name')
    medical_history = fields.Text(string='Medical History')
    intervention_ids = fields.One2many('odooexp.intervention', 'patient_id', string='Interventions')
    treatment_ids = fields.One2many('odooexp.treatment', 'patient_id', string='Treatments')

class OdooExpPatient(models.Model):
    _inherit = 'res.partner'  # Inherit from the existing 'res.partner' model

    is_patient = fields.Boolean(string="Is a Patient", default=False)  # New field to identify patients
    birth_date = fields.Date(string='Birth Date')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    medical_history = fields.Text(string="Medical History")
    intervention_ids = fields.One2many('odooexp.intervention', 'patient_id', string='Interventions')
    treatment_ids = fields.One2many('odooexp.treatment', 'patient_id', string='Treatments')



# class OdooExpPatient(models.Model):
#     _name = 'odooexp.patient'
#     _description = 'Patient Information'
#     _inherit = ['mail.thread', 'mail.activity.mixin']
#     _order = 'id desc'

#     name = fields.Char(string='Full Name', required=True)
#     birth_date = fields.Date(string='Birth Date')
#     gender = fields.Selection([
#         ('male', 'Male'),
#         ('female', 'Female'),
#         ('other', 'Other'),
#     ], string='Gender')
#     phone = fields.Char(string='Phone')
#     email = fields.Char(string='Email')
#     address = fields.Char(string='Address')
#     medical_history = fields.Text(string='Medical History')
#     intervention_ids = fields.One2many('odooexp.intervention', 'patient_id', string='Interventions')
#     treatment_ids = fields.One2many('odooexp.treatment', 'patient_id', string='Treatments')


