    ##############################################################################
    #    Copyright (C) 2021 jeo Software  (http://www.jeosoft.com.ar)
    #    All Rights Reserved.
    ##############################################################################
{
    'name': 'myproject',
    'version': '13.0.1.0.0',
    'category': 'Tools',
    'summary': "Project example for v13 CE",
    'author': "jeo Software",
    'license': 'AGPL-3',
    'depends': [],
    'installable': True,
    'application': False,

    'env-ver': '2',

    'git-repos': [
        'https://github.com/jobiols/cl-myproject.git',
        'https://github.com/ingadhoc/odoo-argentina.git',
    ],

    'docker-images': [
        'odoo jobiols/odoo-jeo:13.0',
        'postgres postgres:10.1-alpine',
        'nginx nginx'
    ]
}
