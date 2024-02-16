{
    "name": "Propietats immobiliàries.",
    "images": ["static/description/icon.png"],
    "summary": "Manage properties",
    "author": "Ismael Semmar Galvez",
    "website": "https://github.com/Ism1tha/technical-training",
    "version": "16.0.0",
    "application": True,
    "depends": ["base"],
    "data": [ 
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        'views/estate_menus.xml',
    ],
    "installable": True,
    'license': 'LGPL-3',
}
