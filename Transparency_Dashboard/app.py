import streamlit as st

from st_pages import Page, Section, show_pages, add_page_title


st.set_page_config(
    page_title="Welcome!",
    )

# Specify what pages should be shown in the sidebar, with their titles and icons
show_pages(
    [
        Page("app.py", "Home", "🏠"),
        Page("pages/Patient Price Search.py","Patient Price Comparison", ':bar_chart:'),
        Page("pages/Insurance Provider Comparison.py", "Analyst Comparison", ":chart_with_upwards_trend:"),
        Page("pages/Pricing Data Explorer.py", "Data Explorer",':pick:'),
        Page("pages/Map Overview.py",'Map Overview',':airplane:')
    ]
)

st.write("# Welcome to Transparency in Coverage Explorer! 👋")

st.sidebar.success("Select a dashboard above.")

st.markdown(
    """
    Data from Transparency in Coverage

    ***
    **👈 Select a dashboard from the sidebar** to see coverage information!
    
    ### Want to learn more?
    - Jump into our [documentation](https://github.com/mehta-akshay/transparency-in-coverage)
    - Background on [Transparency in Coverage](https://www.cms.gov/healthplan-price-transparency)
    - Creation of this app was created with [Streamlit](https://streamlit.io)
"""
)
