import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime

# Page configuration - This must be at the top of the file
st.set_page_config(page_title="R.E.A.C.H Waste Management Dashboard", layout="wide")

# Static Data - Predefined counts for Bottle and Utensil waste
static_counts = {
    'bottle': 25,  # Example count for bottles
    'utensil': 40  # Example count for utensils
}

# Load data using static counts
data = pd.DataFrame({
    'category': ['Bottle', 'Utensils'],
    'count': [static_counts['bottle'], static_counts['utensil']],
    'date': [datetime.today().date(), datetime.today().date()]
})

# Ensure the 'date' column is in datetime format
data['date'] = pd.to_datetime(data['date'])

# Header
st.title("R.E.A.C.H Waste Management Dashboard")
st.subheader("Enhancing Waste Management Practices at Arellano University - Jose Rizal Campus")

# Introduction Section
st.markdown("""### Introduction to the R.E.A.C.H Waste Management Dashboard
Welcome to the R.E.A.C.H Waste Management Dashboard! This platform is designed to enhance waste management practices at **Arellano University - Jose Rizal Campus**.""")

# Goals Section
st.markdown("""### Goals of the R.E.A.C.H Project
- **Raise Awareness**: Increase student awareness of waste management issues.
- **Promote Recycling**: Encourage recycling practices among students and faculty.
- **Track Waste**: Monitor waste generation and recycling efforts on campus.
- **Engage the Community**: Foster a culture of sustainability within the university.""")

# Sidebar for Year, Month, Day, Today's Data, and Color Theme
with st.sidebar:
    st.title("Settings")

    # Year selection
    year = st.selectbox("Select Year", range(2024, datetime.today().year + 1))

    # Month selection
    month = st.selectbox("Select Month", list(range(1, 13)), format_func=lambda x: datetime(2000, x, 1).strftime('%B'))

    # Day selection based on selected month
    days_in_month = [
        31,  # January
        28 + (1 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 0),  # February
        31,  # March
        30,  # April
        31,  # May
        30,  # June
        31,  # July
        31,  # August
        30,  # September
        31,  # October
        30,  # November
        31   # December
    ]
    day = st.selectbox("Select Day", list(range(1, days_in_month[month - 1] + 1)))

    # Data View Selection
    view_today = st.radio("View Data For:", options=["Today", "Selected Month"])

    # Color Theme Selection
    selected_color = st.selectbox("Select Color Theme", ['blue', 'green', 'red'])

    # Initialize filtered_data DataFrame
    filtered_data = pd.DataFrame()

    # Today's data
    if view_today == "Today":
        today = datetime.today().date()
        today_data = pd.DataFrame({
            'category': ['Bottle', 'Utensils'],
            'count': [static_counts['bottle'], static_counts['utensil']],
            'date': [today, today]
        })

        st.write(f"Data for {today}:")
        if not today_data.empty:
            st.write(today_data)

        # Set filtered_data for today
        filtered_data = today_data
    else:
        # Selected Month Data
        selected_date = datetime(year, month, day)
        filtered_data = data[data['date'] == selected_date]
        if filtered_data.empty:
            st.write(f"No data available for {selected_date.strftime('%B %d, %Y')}.")
            # Create placeholder data
            filtered_data = pd.DataFrame({'category': ['Bottle', 'Utensils'], 'count': [0, 0], 'date': [selected_date, selected_date]})

# Check if filtered_data contains 'count' before performing operations
if 'count' in filtered_data.columns:
    # Donut Chart Function
    def make_donut(percentage, label, color):
        colors = {
            'blue': ['#29b5e8', '#155F7A'],
            'green': ['#27AE60', '#12783D'],
            'red': ['#E74C3C', '#781F16']
        }
        source = pd.DataFrame({"Topic": ['', label], "% value": [100 - percentage, percentage]})

        plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
            theta="% value",
            color=alt.Color("Topic:N", scale=alt.Scale(domain=[label, ''], range=colors[color]), legend=None)
        ).properties(width=130, height=130)

        text = plot.mark_text(align='center', color=colors[color][0], fontSize=20, fontWeight=700).encode(
            text=alt.value(f'{percentage:.1f} %')
        )
        return plot + text

    # Main Layout Columns
    col1, col2, col3 = st.columns((1.5, 4.5, 2), gap='medium')

    # Column 1 - Metrics Card and Donut Chart
    with col1:
        st.markdown("#### Waste Metrics")
        total_items = filtered_data['count'].sum()
        st.metric(label="Total Waste Items", value=total_items)

        st.markdown("#### Waste Composition")
        for category in filtered_data['category'].unique():
            category_count = filtered_data[filtered_data['category'] == category]['count'].iloc[0]
            donut_chart = make_donut((category_count / total_items) * 100 if total_items > 0 else 0, category, selected_color)
            st.altair_chart(donut_chart)

    # Column 2 - Waste Trends by Category
    with col2:
        st.markdown("#### Waste Trends by Category")
        for category in ["Bottle", "Utensils"]:
            st.markdown(f"### {category}")
            category_data = filtered_data[filtered_data['category'] == category]

            # Create placeholder data if there's no data
            if category_data.empty:
                category_data = pd.DataFrame({'date': [datetime.today().date()], 'count': [0]})

            # Create line chart
            line_chart = alt.Chart(category_data).mark_line(color=selected_color, point=True).encode(
                x=alt.X('date:T', title="Date"),
                y=alt.Y('count:Q', title="Count"),
                tooltip=['date', 'count']
            ).properties(width=300, height=200).interactive()

            # Create bar chart
            bar_chart = alt.Chart(category_data).mark_bar(color='lightgray', opacity=0.7).encode(
                x=alt.X('date:T', title="Date"),
                y=alt.Y('count:Q', title="Count"),
                tooltip=['date', 'count']
            ).properties(width=300, height=200)

            # Display charts side by side
            charts_col1, charts_col2 = st.columns(2)
            with charts_col1:
                st.altair_chart(line_chart, use_container_width=True)
            with charts_col2:
                st.altair_chart(bar_chart, use_container_width=True)

    # Column 3 - Summary Table and About Section
    with col3:
        st.markdown("#### Recyclable Items Summary")
        if not filtered_data.empty:
            summary_data = filtered_data[['category', 'count']].groupby('category').sum().reset_index()
            summary_data.columns = ['Category', 'Count']
            st.table(summary_data)

        # About Section
        st.markdown(
            """
            <div style='background-color: #f0f8ff; padding: 20px; border-radius: 10px;'>
                <h3 style='text-align: center;'>About the Dashboard</h3>
                <p style='text-align: justify;'>This dashboard provides insights into waste management on campus, focusing on recyclable items. 
                Use this tool to track trends and help promote sustainability initiatives. 
                Thank you for being a part of our eco-friendly efforts!</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# Error handling for missing 'count' column
else:
    st.error("The 'count' column is missing from the filtered data.")
