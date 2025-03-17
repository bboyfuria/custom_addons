{
    "name": "Project Extension",
    "version": "1.0.1",
    "category": "Project",
    "summary": "Customized fields and features to Project Management",
    "depends": ["project"],
    "data": [
        'views/project_views.xml',
        'security/ir.model.access.csv'
    ],
    "assets": {
        'web.assets_backend': [
            'custom_addons/project_extension/static/src/project_extension.scss',
        ],
    },
    "installable": True,
    "application": False,
}






