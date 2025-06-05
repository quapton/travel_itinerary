frappe.ui.form.on("Itinerary Request", {
  refresh(frm) {
    if (!frm.doc.__islocal && frm.doc.status !== "Complete") {
      frm.add_custom_button("Generate Itinerary PDF", () => {
        frappe.call({
          method: "travel_itinerary.travel_itinerary.doctype.itinerary_request.itinerary_request.process_itinerary_request",
          args: { docname: frm.doc.name },
          callback: (r) => {
            if (!r.exc) {
              frappe.msgprint("✅ PDF generation triggered. Refresh in a few seconds.");
              frm.reload_doc();
            }
          },
        });
      });
    }

    if (frm.doc.status === "Complete" && frm.doc.pdf_file) {
      frm.add_custom_button("Download PDF", () => {
        window.open(frm.doc.pdf_file);
      });
    }
  },
});
