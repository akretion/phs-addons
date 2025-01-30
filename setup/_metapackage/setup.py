import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-akretion-phs-addons",
    description="Meta package for akretion-phs-addons Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-connector_medipim',
        'odoo14-addon-delivery_carrier_chronopost',
        'odoo14-addon-delivery_carrier_gls',
        'odoo14-addon-delivery_carrier_label_colisprive',
        'odoo14-addon-delivery_carrier_mondial_relay',
        'odoo14-addon-disable_quick_create_by_default',
        'odoo14-addon-dispute',
        'odoo14-addon-dispute_purchase',
        'odoo14-addon-dispute_stock',
        'odoo14-addon-email_template',
        'odoo14-addon-mail_no_portal_button',
        'odoo14-addon-phs_delivery_label',
        'odoo14-addon-phs_product_auto_tags',
        'odoo14-addon-phs_responsible_supplier',
        'odoo14-addon-phs_sale_order',
        'odoo14-addon-phs_stock',
        'odoo14-addon-phs_supplier_responsible_purchase',
        'odoo14-addon-product_editor',
        'odoo14-addon-product_view_optional_field',
        'odoo14-addon-reporting_access',
        'odoo14-addon-res_partner_mandatory_field',
        'odoo14-addon-sale_import',
        'odoo14-addon-sale_report_out_of_stock',
        'odoo14-addon-shopfloor_mobile_multi_barcode',
        'odoo14-addon-stock_reception_error',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
