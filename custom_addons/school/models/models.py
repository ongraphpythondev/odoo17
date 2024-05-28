from odoo import models, fields,api

# class Admin(models.Model):
#     _name = 'admin.management'
#     _description = 'Admin Management'

#     name = fields.Char(string='Name', required=True)
#     email = fields.Char(string='Email', required=True)
#     admin_id = fields.Char(string='Admin ID', compute='_compute_admin_id')

#     @api.depends('name')
#     def _compute_admin_id(self):
#         for admin in self:
#             admin.admin_id = 'ADMIN-' + str(admin.id)

class School(models.Model):
    _name = 'school.name'
    _description = 'School description'
    
    name = fields.Char(string='Name', required=True)
    address = fields.Text(string='Address')

# class Teacher(models.Model):
#     _name = 'teacher.management'
#     _description = 'Teacher Management'

#     name = fields.Char(string='Name', required=True)
#     email = fields.Char(string='Email', required=True)

class Student(models.Model):
    _name='student.name'
    _description = 'Student description'
    name = fields.Char(string='Name')
    address_student=fields.Text(string='Address Student')
    age=fields.Char(string='Age')
    roll_number = fields.Char(string='Roll Number')
    school_id = fields.Many2one('school.name', string='School')
    
    
    @api.model
    # For get all records
    # def read(self,fields,load):
    #     students = self.env['student.name'].search([('age', '=', 20)])
    #     print(students,"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    #     if students:
    #         for student in students:
    #             print("Name:", student.name)
    #             print("Address:", student.address_student)
    #             print("Age:", student.age)
    #             print("Roll Number:", student.roll_number)
    #             print("School:", student.school_id.name)
    #     else:
    #         print("No student found with age 20")
    #     return super().read(fields,load)
    
    
    # For get records by using id
    def read(self, fields,load):
        student = self.env['student.name'].browse(1)
        # student = self.browse(1)
        return super().read(fields,load)
    
    
    # @api.model
    def create(self, data_list):
        data_list=({
            'name': 'vkj',
            'address_student': 'meerut',
            'age': 23,
            'roll_number': 3,
            'school_id': 1
        })
        return super(Student, self).create([data_list])