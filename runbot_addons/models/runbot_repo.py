# -*- coding: utf-8 -*-
from openerp.osv import orm, fields


class runbot_repo(orm.Model):
    _inherit = "runbot.repo"

    _columns = {
        'is_addon_repo': fields.boolean("Is Addon Repository"),
        'odoo_core': fields.many2one('runbot.repo', string='Odoo Core'),
        'needed_repos': fields.many2many(
            'runbot.repo', rel='runbot_repo_rel',
            id1='dependant_id', id2='dependency_id',
            string='Needed Addon Repositories'
        ),
    }
