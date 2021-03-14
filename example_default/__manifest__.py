    ##############################################################################
    #    Copyright (C) 2021 jeo Software  (http://www.jeosoft.com.ar)
    #    All Rights Reserved.
    ##############################################################################
{
    'name': 'example',
    'version': '13.0.1.0.0',
    'category': 'Tools',
    'summary': "Project example for v13 CE",
    'author': "jeo Software",
    'license': 'AGPL-3',
    'depends': [
        'sale_management',
        'crm'
    ],
    'installable': True,
    'application': False,

    'config': [],
    'port': '8069',

    'git-repos': [
        'https://github.com/jobiols/cl-example.git',
        'https://github.com/ingadhoc/odoo-argentina.git',
    ],

    'docker-images': [
        'odoo jobiols/odoo-jeo:13.0',
        'postgres postgres:10.1-alpine',
        'nginx nginx'
    ]
}
