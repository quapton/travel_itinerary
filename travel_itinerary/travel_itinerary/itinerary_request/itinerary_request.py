# itinerary_request.py
import frappe
import requests
from frappe.model.document import Document
from frappe.utils import now_datetime
import base64

class ItineraryRequest(Document):
    pass

def process_itinerary_request(doc):
    try:
        payload = {
            "location": doc.location,
            "days": doc.number_of_days,
            "start_date": doc.start_date,
            "travel_mode": doc.travel_mode,
            "interests": doc.interests,
            "budget": doc.budget_range,
            "accommodation": doc.accommodation_type,
            "email": doc.email
        }

        response = requests.post("http://ai-server/api/generate-itinerary", json=payload)

        if response.status_code == 200:
            filename = f"Itinerary_{doc.location}_{now_datetime().strftime('%Y%m%d_%H%M%S')}.pdf"
            file_url = save_pdf_to_file(response.content, filename, doc.name)

            doc.pdf_file = file_url
            doc.status = "Complete"
            doc.response_time = now_datetime()
            doc.save(ignore_permissions=True)
        else:
            doc.status = "Failed"
            doc.save(ignore_permissions=True)
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "ItineraryRequestError")
        doc.status = "Failed"
        doc.save(ignore_permissions=True)

def save_pdf_to_file(pdf_bytes, filename, attached_to):
    file_doc = frappe.get_doc({
        "doctype": "File",
        "file_name": filename,
        "attached_to_doctype": "Itinerary Request",
        "attached_to_name": attached_to,
        "is_private": 1,
        "content": base64.b64encode(pdf_bytes).decode("utf-8")
    })
    file_doc.save(ignore_permissions=True)
    return file_doc.file_url