# -*- coding: utf-8 -*-
# from odoo import http


# class CreateModel(http.Controller):
#     @http.route('/create_model/create_model/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/create_model/create_model/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('create_model.listing', {
#             'root': '/create_model/create_model',
#             'objects': http.request.env['create_model.create_model'].search([]),
#         })

#     @http.route('/create_model/create_model/objects/<model("create_model.create_model"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('create_model.object', {
#             'object': obj
#         })
