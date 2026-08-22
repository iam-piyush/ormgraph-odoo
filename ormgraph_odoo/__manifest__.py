{
    "name": "ORMGraph — ERD Studio, Database Diagram & Architecture Visualizer",
    "version": "19.0.1.0.0",
    "category": "Developer Tools",
    "summary": "Interactive ERD diagram generator, database schema explorer, model relationship graph & BFS dependency pathfinder for Odoo developers.",
    "description": """
ORMGraph — Live Architecture & ERD Explorer for Odoo
===================================================

Visualize, explore, and debug your entire Odoo data model in real time!

Key Features:
-------------
* **Interactive ERD Diagram**: Rich table cards with colored field badges (Many2one, One2many, Many2many, Char, Boolean, etc.).
* **Structural Graph View**: Cytoscape-powered high-performance graph with multiple layout algorithms (Flow, Hierarchy, Organic).
* **Pathfinder**: Find direct and multi-hop relationship paths between any two models.
* **1-Click Smart Button**: Open any model's architecture directly from Technical -> Models form view.
* **Architecture Health & Cycles**: Detect circular dependencies and explore strongly connected components.
* **High-Res PNG Export**: 3x ultra-clear diagram export with custom framing and padding.
* **Smart Auto-Cluster ZIP Bundle**: Automatically partitions large graphs (>20 models) into Hub sub-graphs and bundles high-res diagrams into a ZIP archive.
* **Zero Config**: Works instantly with all installed custom and base Odoo modules.
    """,
    "author": "Piyush Kumar",
    "website": "https://iampiyush.one",
    "license": "LGPL-3",
    "depends": ["base", "web"],
    "data": [
        "views/ir_model_views.xml",
        "views/menu_views.xml",
    ],
    "images": [
        "static/description/banner.png",
        "static/description/01_studio_overview.png",
        "static/description/02_module_graph.png",
        "static/description/03_erd_cards.png",
        "static/description/04_relational_pathfinder.png",
        "static/description/05_architecture_health_export.png",
        "static/description/06_erd.png",
        "static/description/07_graph.png",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
