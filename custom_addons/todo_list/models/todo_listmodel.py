# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TodoList(models.Model):
    _name = 'todolist.todolist'
    _description = 'Todo List App'

    name = fields.Char(string="Task Name")
    completed=fields.Boolean()
    color=fields.Char()
   