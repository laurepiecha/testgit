# -*- coding: utf-8 -*-

from odoo import models, fields


class wash_instruction(models.Model):
    _name = 'create_model.create_model'
    _description = "wash instruction"

    instruction_text = fields.Char(string='Instruction', required=True, translate=True)
    instruction_pict = fields.Binary(string='Instruction picture')