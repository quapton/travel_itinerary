from frappe import _

def get_data():
    return [
        {
            "module_name": "Travel Itinerary",
            "label": _("Travel Tools"),
            "icon": "fa fa-map",
            "type": "module",
            "color": "blue",
            "items": [
                {
                    "type": "doctype",
                    "name": "Itinerary Request",
                    "label": _("Itinerary Request"),
                    "description": _("Submit a travel plan request."),
                }
            ]
        }
    ]
