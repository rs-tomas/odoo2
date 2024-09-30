{
    'name': 'Dental Practice',
    'version': '0.1',
    'summary': 'A dental practice management',
    'description': '',
    'sequence': 1,
    'author': 'Odoo S.A.',
    'website': 'http://www.odoo.com',
    'depends': ['base', 'mail', 'contacts', 'calendar', 'account', 'sale_management', 'website'],
    'data': [
        'views/dental.xml',
        'security/ir.model.access.csv',
        'views/interventions/interventions_form_view.xml',
        'views/interventions/interventions_tree_view.xml',
        #'views/patients/patients_form_view.xml',
        #'views/patients/patients_tree_view.xml',
        'views/treatments/treatments_form_view.xml',
        'views/treatments/treatments_tree_view.xml',
        'views/treatments/treatments_calendar_view.xml'
        'data/dental_data.xml',
        'views/extends/extend_res_partner.xml'
    ],
    'assets': {
        'web.assets_backend': [
            # 'dental_practice/static/src/**/*',
        ],
    },
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3'
}
