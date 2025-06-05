frappe.ui.form.on("Itinerary Request", {
    refresh(frm) {
        if (frm.doc.status === "Complete" && frm.doc.pdf_file) {
            frm.add_custom_button("Download PDF", () => {
                window.open(frm.doc.pdf_file);
            });
        }
    }
});
