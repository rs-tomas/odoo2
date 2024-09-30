# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.http import request

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
    # Add a computed field to calculate the age of the patient
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    # inverse field for the patiend_id of interventions and treatments
    treatment_ids = fields.One2many('dental.treatment', 'patient_id', string='Treatments')


    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                record.age = fields.Date.from_string(fields.Date.today()).year - fields.Date.from_string(record.birth_date).year
            else:
                record.age = 0
