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
    date = fields.Datetime(string='Date', default=fields.Date.context_today, required=True)
    end_date = fields.Datetime(string='End Date')
    #tooth_number = fields.Char(string='Tooth Number')

    notes = fields.Text(string='Notes')
    # invoice_id = fields.Many2one('account.move', string='Invoice', readonly=True)
    interventions_ids = fields.Many2many('dental.intervention', string='Interventions')
    sales_order_id = fields.Many2one('sale.order', string='Sales Order', readonly=True)
    profile = fields.Selection([("Therapy", "Therapy"), ("Surgery", "Surgery"), ("Orthodontics", "Orthodontics")], string='Treatment Profile')


# hook the write method to create a sales order. Each intervention is a sale order line.
    def write(self, vals):
        res = super(DentalTreatment, self).write(vals)

        if 'interventions_ids' not in vals:
            return res

        # first check if sale order already exists
        if not self.sales_order_id:
            self.create_sale_order()

        sale_order = self.sales_order_id
        for intervention in vals.get('interventions_ids', []):
            try:
                action, intervention_id, data = intervention
            except ValueError:
                action, intervention_id = intervention
                data = None  # or some default value

            intervention_id = self.env['dental.intervention'].browse(intervention_id)
            if action == 4:  # add
                sale_order.order_line.create({
                    'product_id': intervention_id.product_id.id,
                    'product_uom_qty': 1,
                    'order_id': sale_order.id
                })
            elif action == 3:  # delete
                line_to_delete = sale_order.order_line.search([('product_id', '=', intervention_id.product_id.id)])
                if line_to_delete:
                    line_to_delete.unlink()

        return res

    def create_sale_order(self):
        sale_order = self.env['sale.order'].create({
            'partner_id': self.patient_id.id,
            'date_order': self.date,
            'user_id': self.env.user.id,
            'state': 'draft',
            'origin': self.name,
            'note': self.notes
        })
        self.sales_order_id = sale_order.id
        return sale_order

