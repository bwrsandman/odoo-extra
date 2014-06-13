# -*- coding: utf-8 -*-
from openerp.osv import orm, fields


class runbot_branch(orm.Model):
    _inherit = "runbot.branch"

    def create(self, cr, user, vals, context=None):
        repo = self.pool['runbot.repo'].browse(cr, user, vals['repo_id'], context=context)
        if repo.is_addon_repo:
            target_branch_id = self.search(
                cr, user,
                ['&', ('repo_id', '=', repo.odoo_core.id), ('name', '=', vals['name'])],
                context=context)
            if target_branch_id:
                vals['odoo_core_branch'] = target_branch_id[0]
        return super(runbot_branch, self).create(cr, user, vals, context=context)

    _columns = {
        'odoo_core_branch': fields.many2one('runbot.branch', string='Odoo Core Branch'),
        'is_addon_repo': fields.related('repo_id', 'is_addon_repo', type='boolean', string='Is Addon Branch'),
    }
