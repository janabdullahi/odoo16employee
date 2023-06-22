from random import randint

from odoo import models, fields, api

class employee(models.Model):
    _name = 'employee.category'
    _description = 'Employee Category'

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char(string="Tag Name", required=True)
    color = fields.Integer(string='Color Index', default=_get_default_color)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]
