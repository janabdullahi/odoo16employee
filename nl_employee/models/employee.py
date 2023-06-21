# -*- coding: utf-8 -*-

from odoo import models, fields, api


class employee(models.Model):
    _name = 'employee.employee'
    _description = 'Employee Details'

    name = fields.Char()
