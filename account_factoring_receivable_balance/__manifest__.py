# © 2022 David BEAL @ Akretion
# © 2022 Alexis DE LATTRE @ Akretion

{
    "name": "Account Factoring Receivable Balance",
    "version": "17.0.1.0.0",
    "category": "Accounting",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "https://github.com/akretion/odoo-factoring",
    "maintainers": [
        "bealdav",
        "alexis-via",
    ],
    "depends": [
        "account",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/misc.xml",
        "views/account_journal.xml",
        "views/company.xml",
        "views/partner.xml",
        "views/subrogation_receipt.xml",
    ],
    "demo": [
        "views/company_demo.xml",
    ],
}
