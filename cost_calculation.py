import datetime
import streamlit as st
from fpdf import FPDF

# Title of the app
st.title("Kalkulator trasy")

# Input fields with default values
car = st.text_input("Marka samochodu: ", value="Toyota")
engine_capacity = st.text_input("Pojemność silnika: ", value="2.0L")
license_plate = st.text_input("Numer rejestracyjny: ", value="ABC123")
start_state = st.text_input("Początkowy stan licznika: ", value="10000")
name_surname = st.text_input("Imię i nazwisko: ", value="Jan Kowalski")

start_date = st.date_input("Data trasy: ")

# Preconfigured selector for single selection
routes = {
    "A": {"name": "Droga A", "start": "Miasto A", "end": "Miasto B", "distance": 400},
    "B": {"name": "Droga B", "start": "Miasto B", "end": "Miasto C", "distance": 600},
}
preconfigured_routes = [routes["A"]["name"], routes["B"]["name"]]
selected_route = st.selectbox("Wybór trasy:", preconfigured_routes)

selected_route_obj = None
for key, route in routes.items():
    if route["name"] == selected_route:
        selected_route_obj = route
        break

# Display the entered information
st.write(
    "Podsumowanie: ", car, engine_capacity, license_plate, start_state, name_surname
)
st.write("Start: ", start_date)
st.write("Wybrana trasa: ", selected_route)

if selected_route_obj:
    end_state = int(start_state) + selected_route_obj["distance"]
    data = {
        "date": [start_date],
        "name": [name_surname],
        "car name": [car],
        "route": [selected_route],
        "start state": [start_state],
        "end state": [end_state],
    }
    st.table(data)

    if st.button("Export to PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=8)

        # Add hardcoded date in the top right corner
        today_date = datetime.datetime.now().strftime("%Y-%m-%d")
        pdf.cell(0, 10, today_date, 0, 1, "R")

        # Add table header
        headers = ["Date", "Name", "Car Name", "Route", "Start State", "End State"]
        col_width = pdf.w / 8  # Adjust column width to fit the page
        for header in headers:
            pdf.cell(col_width, 8, header, 1)
        pdf.ln()

        # Add table data
        for i in range(len(data["date"])):
            pdf.cell(col_width, 8, str(data["date"][i]), 1)
            pdf.cell(col_width, 8, data["name"][i], 1)
            pdf.cell(col_width, 8, data["car name"][i], 1)
            pdf.cell(col_width, 8, data["route"][i], 1)
            pdf.cell(col_width, 8, str(data["start state"][i]), 1)
            pdf.cell(col_width, 8, str(data["end state"][i]), 1)
            pdf.ln()

        pdf.ln(10)  # Add some space before the description
        pdf.cell(0, 10, "Podpis", 0, 1, "L")

        # Save the PDF
        pdf.output("route_summary.pdf")
        st.success("PDF exported successfully!")

# Inputy
# Marka samochodu
# Pojemność slinka
# Nr rejestracyjny
# Stan licznika na start
# Imie nazwisko

# selektor daty
# Wybór tras, prekonfigurowanych, adres, odległość
# na podstawie tego tworzy data trasa stan licznika przed, po
