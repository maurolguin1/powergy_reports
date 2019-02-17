from odoo import api, _, tools, fields, models, exceptions
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from datetime import datetime
from . import amount_to_text


class ReportPurchase(models.Model):

	_inherit = 'purchase.order'

	type_order = fields.Selection([('national','National'),
							   		('international','International')], help='Choose the type of order', default='national',required=True)
	observations= fields.Text(string='Observations')
	amount_to_text = fields.Char(compute='_get_amount_to_text', string='Monto en Texto', readonly=True,
                                 help='Amount of the invoice in letter')
	
	@api.one
	@api.depends('amount_total')
	def _get_amount_to_text(self):
		self.amount_to_text = amount_to_text.get_amount_to_text(self, self.amount_total)


class ReportFactura(models.Model):

	_inherit = 'account.invoice'

	observations= fields.Text(string='Observations')


class ReportPago(models.Model):

	_inherit = 'account.payment'

	cambio = fields.Float(string='Tipo Cambio')
	bank_reference = fields.Char(string='Ref. Bancaria')


class QuotationsFields(models.Model):
	_name='sale.order'
	_inherit = 'sale.order'

	indiv_orders = fields.Text(string='Pedidos Individuales')	
	name_site = fields.Char(string='Nombre de sitio')
	no_adrisa = fields.Char(string='No. Adrisa/Grafo')
	folio_patrimonial = fields.Char(string='Folio de pase de acceso de Seguridad Patrimonial')

	observations= fields.Text(string='Observations')
	numor_customer = fields.Char(string='Numero de Pedido Cliente')
	fianza = fields.Char(string='Fianza')
	receipt_date = fields.Date(string='Fecha de recepcion')
	delivery_time = fields.Char(string='Tiempo de Entrega')
	deliver_pro = fields.Char(string="Lugar de enterga", help='Ingresa aqui el lugar de la entrega')
	warranty = fields.Char(string='Garantia')
	made_by = fields.Many2one('res.users', string='Elaborado por')

class FieldsAlbaran(models.Model):

	_inherit = 'stock.picking'

	observations = fields.Text(string='Observations')
	op_text = fields.Char(string='OP')
	concept = fields.Selection([('suministro','Suministro'),
								('instalacion','Instalacion')],string='Concepto')

class ClabeField(models.Model):

	_inherit = 'res.partner'

	clabe_banco = fields.Char(string='CLABE', help='Aqui puedes ingresar tu CLABE de tu cuenta bancaria')
