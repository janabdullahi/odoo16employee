# -*- coding: utf-8 -*-

from odoo import models, fields, api


class employee(models.Model):
    _name = 'employee.employee'
    _description = 'Employee Details'
    _rec_name = 'employee_id'

    employee_id = fields.Many2one('hr.employee', string="Employee Name")
    department_id = fields.Many2one('hr.department', string="Department", related="employee_id.department_id")
    job_id = fields.Many2one('hr.job', string="Job Title", related="employee_id.job_id")
    parent_id = fields.Many2one('hr.employee', string="Manager", related="employee_id.parent_id")
    category_ids = fields.Many2many('employee.category')
    mobile_phone = fields.Char(related='employee_id.mobile_phone', readonly=False, related_sudo=False)
    employee_phone = fields.Char(related='employee_id.phone', readonly=False, related_sudo=False)
    work_email = fields.Char(related='employee_id.work_email', readonly=False, related_sudo=False)
    coach_id = fields.Many2one(related='employee_id.coach_id', readonly=False, related_sudo=False)
    company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company)