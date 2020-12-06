# Copyright Odoo Community Association (OCA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


class Apriori(object):
    keys = [
        "renamed_modules",
        "merged_modules",
        "renamed_models",
        "merged_models",
    ]

    def __init__(self, apriori_dict):
        for key in self.keys:
            try:
                setattr(self, key, apriori_dict[key])
            except KeyError:
                from odoo.exceptions import ValidationError
                raise ValidationError(
                    "Invalid contents of apriori.json: no key '%s'" % key
                )
