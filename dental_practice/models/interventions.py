# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.http import request

class OdooExpInterventions(models.Model):
    _name = 'odooexp.interventions'
    _description = 'empty model for odooexp.interventions'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    name = fields.Char(string='Name')
