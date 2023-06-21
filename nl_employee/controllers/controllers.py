# -*- coding: utf-8 -*-
# from odoo import http


# class NlEmployee(http.Controller):
#     @http.route('/nl_employee/nl_employee', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nl_employee/nl_employee/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nl_employee.listing', {
#             'root': '/nl_employee/nl_employee',
#             'objects': http.request.env['nl_employee.nl_employee'].search([]),
#         })

#     @http.route('/nl_employee/nl_employee/objects/<model("nl_employee.nl_employee"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nl_employee.object', {
#             'object': obj
#         })
