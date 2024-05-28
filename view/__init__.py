from view.health import get_health


def add_url_rules(app):
    app.add_url_rule(methods=["GET"], rule="/healthz", view_func=get_health)
