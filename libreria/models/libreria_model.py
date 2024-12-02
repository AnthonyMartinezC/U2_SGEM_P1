from odoo import models, fields

class Libreria(models.Model):
    _name = 'libreria.libro'  
    _description = 'Librería para gestionar libros'

    titulo = fields.Char(string='Título del Libro') 
    paginas = fields.Integer(string='Número de Páginas')  
    autor = fields.Char(string='Autor') 
    editorial = fields.Char(string='Editorial') 
