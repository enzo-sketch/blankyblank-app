import streamlit as st

# Title of the App
st.title("Dashboard User Guide and FAQ")

# Step-by-Step on How to Use the Dashboard
st.header("Step-by-Step on How to Use the Dashboard:")

st.subheader("1. Open the Web Browser")
st.write(
    "Launch your preferred web browser and enter the website URL into the address bar. "
    "Press Enter to access the website."
)

st.subheader("2. Access the Dashboard")
st.write(
    "Locate the dashboard link or tab in the website's main menu. Click on it to open the dashboard."
)

st.subheader("3. Familiarize with the Layout")
st.write(
    "Once the dashboard loads, take time to explore the layout. This includes:"
)
st.markdown(
    """
    - **Navigation menu:** Typically found at the top or left side of the screen.
    - **Widgets or panels:** These display important data summaries.
    - **Settings/Profile icon:** Often located at the top-right corner for personalizing your dashboard settings.
    """
)

st.subheader("4. Explore Features")
st.write(
    "You can interact with various features to analyze data, locate content, and explore more details."
)
st.markdown(
    """
    - **View and analyze data summaries and charts:** These provide quick insights into the data you are tracking.
    - **Use the search box:** Enter specific keywords to find content quickly.
    - **Interact with buttons, tabs, and dropdown menus:** These allow you to delve deeper into detailed information.
    """
)

st.subheader("5. Customize (if available)")
st.write(
    "You can personalize the dashboard layout by adjusting the following settings:"
)
st.markdown(
    """
    - Rearranging widgets.
    - Changing the theme.
    - Modifying settings as per your preferences.
    """
)

# Common Questions Regarding the Data and Its Interpretation
st.header("Common Questions Regarding the Data and Its Interpretation:")

st.subheader("What does the total waste count represent?")
st.write(
    "It shows the cumulative count of different waste categories (such as bottles and utensils) for the selected date."
)

st.subheader("Why does the chart sometimes show zero or empty data?")
st.write(
    "This could occur when no data is available for that specific time or category. "
    "You may need to check the date or try refreshing the page."
)

st.subheader("How are the recycling trends tracked?")
st.write(
    "The trends track the volume of recyclable items disposed of on campus, "
    "which can be analyzed over specific time periods like today, this month, or year."
)

# Technical Issues Section
st.header("Technical Issues")

st.subheader("Camera cannot detect trash:")
st.write("**Solution:** Ensure you are within the camera's detection range. If the trash bin hasn't been opened yet, try waiting a few seconds for the system to process the data.")

st.subheader("Data not displaying properly:")
st.write("**Solution:** Try refreshing the dashboard page. If issues persist, check your internet connection and ensure the system is operating correctly.")

st.subheader("Issues with the trash collector data:")
st.write("**Solution:** If the data is malfunctioning, try refreshing the dashboard to re-fetch updated information.")


