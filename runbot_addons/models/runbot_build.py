# -*- coding: utf-8 -*-
from openerp.osv import orm


class runbot_build(orm.Model):
    _inherit = "runbot.build"

    def get_server_path(self, cr, uid, ids, *l, **kw):
        for build in self.browse(cr, uid, ids, context=None):
            if build.branch_id.odoo_core_branch:
                core_id = self.search(cr, uid, ['&', ('repo_id', '=', build.repo_id.odoo_core.id), ('branch_id', '=', build.branch_id.odoo_core_branch.id)])[0]
            elif build.repo_id.is_addon_repo:
                core_id = self.search(cr, uid, [('repo_id', '=', build.repo_id.odoo_core.id)])[0]
            else:
                core_id = build.id
            return super(runbot_build, self).get_server_path(cr, uid, [core_id], *l, **kw)

    def cmd(self, cr, uid, ids, context=None):
        for build in self.browse(cr, uid, ids, context=context):
            cmd, mods = super(runbot_build, self).cmd(cr, uid, ids, context=context)
            if build.repo_id.is_addon_repo:
                cmd.append('--addons-path=' + build.path('openerp', 'addons'))
            return cmd, mods
