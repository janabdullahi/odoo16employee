# -*- coding: utf-8 -*-

from odoo import models, fields, api


class employee(models.Model):
    _name = 'employee.employee'
    _description = 'Employee Details'

    employee_id = fields.Many2one('hr.employee', string="Employee Name")
    department_id = fields.Many2one('hr.department', string="Department", related="employee_id.department_id")
    job_id = fields.Many2one('hr.job', string="Job Title", related="employee_id.job_id")
