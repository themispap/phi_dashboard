import streamlit as st
from utils import execute_query

# academic year selector
acad_year=st.sidebar.selectbox("Ακαδημαϊκό έτος",
                               ("2022-2023",
                                "2023-2024",
                                "2024-2025",
                                "2025-2026"),
                                index=2)
# past academic year
acad_year_past = {"2022-2023": "'2022-2023'",
                  "2023-2024": "'2022-2023'",
                  "2024-2025": "'2023-2024'",
                  "2025-2026": "'2024-2025'"}

# start and end date of each academic year
acad_years={"2022-2023": ("'2022-06-20'","'2023-06-18'"),
            "2023-2024": ("'2023-06-19'","'2024-06-16'"),
            "2024-2025": ("'2024-06-17'","'2025-06-15'"),
            "2025-2026": ("'2025-06-15'","'2026-06-14'")}
# start and end date of selected academic year
start = acad_years[acad_year][0]
end = acad_years[acad_year][1]

# personal expenses checkbox
personal_expenses=st.sidebar.checkbox('Προσωπικά έξοδα')

# definining the tabs of the dashboard
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(['Ισολογισμός',
                                                'Υπόλοιπα',
                                                'Διδακτικές ώρες',
                                                'Εγγραφές/Διαγραφές',
                                                'Χάρτης',
                                                'Πελάτες',
                                                'Μαθητές']
                                                )

with tab1: # Ισολογισμός
    # income dataframe of the selected academic year
    income = execute_query('sql/income_table.sql',start,end,acad_year)