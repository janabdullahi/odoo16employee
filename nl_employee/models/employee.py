# -*- coding: utf-8 -*-

from odoo import models, fields, api


class employee(models.Model):
    _name = 'employee.employee'
    _description = 'Employee Details'

    employee_id = fields.Many2one('hr.employee', string="Employee Name")
