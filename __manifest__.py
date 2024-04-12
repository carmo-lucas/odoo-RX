{
    'name': 'Precriptions Rx',
    'version': '0.0.0900',
    'author':'Lucas Chagas Lima do Carmo',
    'category': 'Technical',
    'summary': 'Prescription Inclusion',
    'description': """Module for including medical prescriptions""",
    'depends': ['mail','product','uom','stock'],
    'sequence': 0,
    'data': [
        'views/prescriptions.xml',
        'data/sequence.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
