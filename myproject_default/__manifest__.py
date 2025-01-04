##########################################################################
#    Copyright (C) 2024 jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
##########################################################################

{
    'name': 'myproject',
    'version': '17.0.1.0.0',
    'category': 'Tools',
    'summary': "Project example for v17 CE",
    'author': "jeo Software",
    'license': 'AGPL-3',
    'depends': [],
    'installable': True,
    'application': False,

    'env-ver': '2',
    'config': [
                'workers = 4',
                'max_cron_threads = 1',
                'admin_passwd = k0923%098',
                'proxy_mode = True',
                'list_db = False',
              ],
    'config-local': ['admin_passwd = admin'],
    'git-repos': [
        'https://github.com/jobiols/cl-myproject.git',
        'https://github.com/ingadhoc/odoo-argentina.git',
    ],

    'docker-images': [
        'odoo jobiols/odoo-jeo:17.0',
        'postgres postgres:14.13-alpine',
        'nginx nginx'
    ]
}
