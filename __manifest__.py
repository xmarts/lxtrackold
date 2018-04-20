# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Lxtrack',
    'summary': 'Modulo del lxtrack',

    'description': """
    - Ruta de entregas de lxtrack
    """,
    'author': "Xmarts, Nayeli Valencia Díaz",
    'website': "http://www.xmarts.com",
    'depends': ['base'],
    'data': [
        'views/route_orders_views.xml',
        'wizard/partner_process.xml',

    ]
}
