# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
<<<<<<< 07b49e0657f0dbcdf2505fb7f323c617d1adad06

import odoo.addons.payment_stripe as stripe  # prevent circular import error with payment_stripe
||||||| 30cbd52a5c0d0a911648dcb45143a4ec551f606c
import odoo.addons.payment_stripe as stripe  # prevent circular import error with payment_stripe
=======
try:
    import odoo.addons.payment_stripe as stripe  # prevent circular import error with payment_stripe
except ModuleNotFoundError:
    stripe = None
>>>>>>> 4d9ae49ca244fcdd2194a40ebc2043d0e163c7e2


class ResCountry(models.Model):
    _inherit = 'res.country'

    is_stripe_supported_country = fields.Boolean(compute='_compute_is_stripe_supported_country')

    @api.depends('code')
    def _compute_is_stripe_supported_country(self):
        for country in self:
            country.is_stripe_supported_country = (
                stripe is not None
                and stripe.const.COUNTRY_MAPPING.get(
                    country.code, country.code
                ) in stripe.const.SUPPORTED_COUNTRIES
            )
