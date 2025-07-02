app_name = "travel_itinerary"
app_title = "Travel Itinerary"
app_publisher = "partners@quapton"
app_description = "a tool that simplifies the process of creating detailed and organized travel plans"
app_email = "partners@quapton.com"
app_license = "mit"
app_icon_url = "/assets/travel_itinerary/images/flight.png"
app_icon_title = "Travel Itinerary"
app_icon_route = "/travel_itinerary"
# Apps
# ------------------
doctype_js = {
    "Itinerary Request": "public/js/itinerary_request.js"
}
# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "travel_itinerary",
# 		"logo": "/assets/travel_itinerary/images/flight.png",
# 		"title": "Travel Itinerary",
# 		"route": "/travel_itinerary",
# 		# "has_permission": "travel_itinerary.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/travel_itinerary/css/custom_font.css"

# app_include_css = "/assets/travel_itinerary/css/travel_itinerary.css"
# app_include_js = "/assets/travel_itinerary/js/travel_itinerary.js"

# include js, css files in header of web template
# web_include_css = "/assets/travel_itinerary/css/travel_itinerary.css"
# web_include_js = "/assets/travel_itinerary/js/travel_itinerary.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "travel_itinerary/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "travel_itinerary/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "travel_itinerary.utils.jinja_methods",
# 	"filters": "travel_itinerary.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "travel_itinerary.install.before_install"
# after_install = "travel_itinerary.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "travel_itinerary.uninstall.before_uninstall"
# after_uninstall = "travel_itinerary.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "travel_itinerary.utils.before_app_install"
# after_app_install = "travel_itinerary.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "travel_itinerary.utils.before_app_uninstall"
# after_app_uninstall = "travel_itinerary.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "travel_itinerary.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"travel_itinerary.tasks.all"
# 	],
# 	"daily": [
# 		"travel_itinerary.tasks.daily"
# 	],
# 	"hourly": [
# 		"travel_itinerary.tasks.hourly"
# 	],
# 	"weekly": [
# 		"travel_itinerary.tasks.weekly"
# 	],
# 	"monthly": [
# 		"travel_itinerary.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "travel_itinerary.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "travel_itinerary.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "travel_itinerary.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["travel_itinerary.utils.before_request"]
# after_request = ["travel_itinerary.utils.after_request"]

# Job Events
# ----------
# before_job = ["travel_itinerary.utils.before_job"]
# after_job = ["travel_itinerary.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"travel_itinerary.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


standard_dropdown_items = [
	{
		"name1": "app_selector",
		"label": "Apps",
		"type": "Route",
		"route": "#",
		"is_standard": 1,
	},
	{
		"name1": "toggle_theme",
		"label": "Toggle theme",
		"type": "Route",
		"icon": "moon",
		"route": "#",
		"is_standard": 1,
	},
	{
		"name1": "settings",
		"label": "Settings",
		"type": "Route",
		"icon": "settings",
		"route": "#",
		"is_standard": 1,
	},
	{
		"name1": "login_to_fc",
		"label": "Login to Frappe Cloud",
		"type": "Route",
		"route": "#",
		"is_standard": 1,
	},
	{
		"name1": "about",
		"label": "About",
		"type": "Route",
		"icon": "info",
		"route": "#",
		"is_standard": 1,
	},
	{
		"name1": "separator",
		"label": "",
		"type": "Separator",
		"is_standard": 1,
	},
	{
		"name1": "logout",
		"label": "Log out",
		"type": "Route",
		"icon": "log-out",
		"route": "#",
		"is_standard": 1,
	},
]