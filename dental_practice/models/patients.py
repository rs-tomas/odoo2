# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.http import request

class OdooExpPatients(models.Model):
    _name = 'odooexp.patients'
    _description = 'empty model for odooexp.patients'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    name = fields.Char(string='Name')
