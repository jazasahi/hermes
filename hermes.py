import streamlit as st

st.set_page_config(page_title="Prior Authorization Checker", layout="centered")

st.title("🩺 Prior Authorization Checker")

drug_name = st.text_input("Enter Drug Name", placeholder="e.g., Ozempic")

plan = st.selectbox("Select Insurance Plan", ["", "Maryland Medicaid", "DC Medicaid", "California Medicaid"])

submit = st.button("Check PA Status")

if submit and drug_name and plan:
    drug = drug_name.strip().lower()
    plan_key = plan.lower().replace(" ", "_")

    if drug == "ozempic" and plan_key == "maryland_medicaid":
        pa_required = True
        notes = "Step therapy required. Must try metformin first."
        form_link = "https://example.com/md_form.pdf"
        alternatives = ["Metformin", "Rybelsus"]
    else:
        pa_required = False
        notes = "No prior authorization required."
        form_link = None
        alternatives = []

    st.subheader("📝 PA Results")
    st.markdown(f"**PA Required:** {'✅ Yes' if pa_required else '❌ No'}")
    st.markdown(f"**Notes:** {notes}")

    if pa_required and form_link:
        st.markdown(f"[📄 Download PA Form]({form_link})")

    if alternatives:
        st.markdown(f"**Covered Alternatives:** {', '.join(alternatives)}")
