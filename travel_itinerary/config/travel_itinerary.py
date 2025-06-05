from frappe import _

def get_data():
	return [
		{
			"label": _("Itinerary Management"),
			"icon": "fa fa-map",
			"items": [
				{
					"type": "doctype",
					"name": "Itinerary Request",
					"description": _("Request AI-generated travel itinerary."),
					"onboard": 1
				}
			]
		}
	]
