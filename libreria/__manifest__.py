{
    'name': 'Libreria',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Gestión de libros y autores',
    'description': 'Un módulo básico para gestionar libros y autores.',
    'author': 'Anthony',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv', 
        'views/libreria_view.xml',       
    ],
    'installable': True,
    'application': True,
}
