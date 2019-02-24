{
    'name': 'Reports & Fields',
    'version': '1.0',
    'summary': 'Personalizacion de reportes y vistas para Powergy',
    'description': 'Adecuaciones a los reportes incluidos en odoo, se incluyen campos a diversas ventanas para el uso de datos en los reportes que en este modulo se agregan',
    'category': 'Personalizacion',
    'author': 'William Colin Macedo',
    'website': 'www.xmarts.com',
    'depends': ['base','purchase','contacts','sale_stock'],
    'data': ['views/view.xml',
    		 'reports/report_purchase_order.xml',
             'reports/report_factura.xml',
             'reports/report_delivery_split.xml',
             'reports/report_mrporder.xml',
             'reports/report_payment_receipt.xml',
             'reports/report_saleorder.xml',             
             'reports/report_albaran.xml' ],


}