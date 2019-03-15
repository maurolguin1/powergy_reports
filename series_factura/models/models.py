from openerp import fields,models,api

class plantilla_invoice(models.Model):
    _inherit = "account.invoice"

    adri_graf = fields.Char(string="No Adrisa/Grafo", compute="_get_adrisa")
    folio_patr = fields.Char(string="Folio S. Patrimonial", compute="_get_folio")
    marco = fields.Many2one("crm.lead", string="Marco", compute="_get_marco")
    n_pedido = fields.Char(string="No Pedido Cliente", compute="_get_pedido")

    @api.one
    def _get_adrisa(self):
        query = "select no_adrisa from sale_order where name='"+str(self.origin)+"' limit 1"
        self.env.cr.execute(query)
        vals = self.env.cr.fetchone()
        if vals:
            for va in vals:
                self.adri_graf = va

    @api.one
    def _get_folio(self):
        query = "select folio_patrimonial from sale_order where name='"+str(self.origin)+"' limit 1"
        self.env.cr.execute(query)
        vals = self.env.cr.fetchone()
        if vals:
            for va in vals:
                self.folio_patr = va

    @api.one
    def _get_marco(self):
        query = "select opportunity_id from sale_order where name='"+str(self.origin)+"' limit 1"
        self.env.cr.execute(query)
        vals = self.env.cr.fetchone()
        if vals:
            for va in vals:
                self.marco = va

    @api.one
    def _get_pedido(self):
        query = "select numor_customer from sale_order where name='"+str(self.origin)+"' limit 1"
        self.env.cr.execute(query)
        vals = self.env.cr.fetchone()
        if vals:
            for va in vals:
                self.n_pedido = va


class plantillas_invoice_line(models.Model):
    _inherit = 'account.invoice.line'

    serie= fields.Text('No Serie', compute='_get_serie')

    @api.one
    @api.depends('serie', 'origin', 'product_id')
    def _get_serie(self):
        cr = self.env.cr
        if self.origin:
            sql = "select splot.name from stock_picking pi left join stock_move sp on sp.picking_id =pi.id  left join stock_move_line spl on spl.move_id=sp.id left join stock_production_lot splot on splot.id=spl.lot_id where  pi.origin='"+str(self.origin)+"' AND sp.product_id="+str(self.product_id.id)+" AND splot.name != 'None'"
        else:
            ori = str(self.name)
            if(ori.find("Venta del ticket:")>=0):
                ori = ori.replace("Venta del ticket: ", "")
            else:
                ori = str(self.invoice_id.origin)
            if ori != '':
                sql = "select splot.name from stock_picking pi left join stock_move sp on sp.picking_id =pi.id	left join stock_move_line spl on spl.move_id=sp.id left join stock_production_lot splot on splot.id=spl.lot_id where  pi.origin='"+str(ori)+"' AND sp.product_id="+str(self.product_id.id)+" AND splot.name != 'None'"
        cr.execute(sql)
        nseries = cr.fetchall()
        serie_text = ''
        cont1 = 0
        for t in nseries:
            if cont1 > 0:
                serie_text = serie_text + ", "
            serie_text = serie_text + str(t[0])
            cont1 = cont1 + 1
        self.serie = serie_text

