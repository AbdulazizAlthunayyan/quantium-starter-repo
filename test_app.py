from app import app
from dash import html, dcc


def get_all_components(component):
    components = []

    if component is None:
        return components

    components.append(component)

    children = getattr(component, "children", None)

    if children is None:
        return components

    if isinstance(children, (list, tuple)):
        for child in children:
            components.extend(get_all_components(child))
    else:
        components.extend(get_all_components(children))

    return components


def test_header_is_present():
    components = get_all_components(app.layout)
    headers = [
        c for c in components
        if isinstance(c, html.H1) and c.children == "Soul Foods Pink Morsel Sales Visualiser"
    ]
    assert len(headers) == 1


def test_visualisation_is_present():
    components = get_all_components(app.layout)
    graphs = [c for c in components if isinstance(c, dcc.Graph)]
    assert len(graphs) == 1


def test_region_picker_is_present():
    components = get_all_components(app.layout)
    radio_items = [c for c in components if isinstance(c, dcc.RadioItems)]
    assert len(radio_items) == 1