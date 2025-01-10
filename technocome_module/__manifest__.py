# -*- coding: utf-8 -*-
{
    'name': 'Technocome Status Folder',
    'version': '16.0',
    'summary': '''Technocome,
        class,''',
    'description':
        '''Technocome Status Folder''',
    'category': 'Technocome/SALE',
    'author': "Technocome Status Folder",
    'company': 'Technocome Status Folder',
    'price': 0,
    'currency': 'USD',
    'website': "https://www.nishan.com",
    'depends': ['base', 'mail', 'board','sale'],  # 'web_domain_field'
    'data': [
        'security/ir.model.access.csv',
        'data/send_mail.xml',
        'views/sale_order_inherit.xml',
        'views/status_folder.xml',
        'views/attendance_view.xml',

        'views/menus.xml',




    ],


    'images': ['static/description/banner.gif'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': True,
    'application': True,
     'assets': {
        'web.assets_backend': [
             'technocome_module/static/css/style.css',
        ],
}
}

