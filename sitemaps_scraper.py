import streamlit as st
import pandas as pd
from advertools import sitemap_to_df

# Custom CSS for styling and external stylesheet
st.markdown(
    """
    <link rel="stylesheet" id="astra-addon-css-css" data-pmdelayedstyle="https://www.intrepidonline.com/wp-content/uploads/astra-addon/astra-addon-668f8149383bd2-70380954.css?ver=4.6.8" media="all" href="https://www.intrepidonline.com/wp-content/uploads/astra-addon/astra-addon-668f8149383bd2-70380954.css?ver=4.6.8">
    <link rel="stylesheet" id="astra-addon-dynamic-css" data-pmdelayedstyle="https://www.intrepidonline.com/wp-content/uploads/astra-addon/astra-addon-dynamic-css-post-7386.css?ver=1720711612" media="all" href="https://www.intrepidonline.com/wp-content/uploads/astra-addon/astra-addon-dynamic-css-post-7386.css?ver=1720711612">
    <link rel="stylesheet" id="powerpack-frontend-css" data-pmdelayedstyle="https://www.intrepidonline.com/wp-content/plugins/powerpack-lite-for-elementor/assets/css/min/frontend.min.css?ver=2.7.19" media="all" href="https://www.intrepidonline.com/wp-content/plugins/powerpack-lite-for-elementor/assets/css/min/frontend.min.css?ver=2.7.19">
    <link rel="stylesheet" id="elementor-pro-css" data-pmdelayedstyle="https://www.intrepidonline.com/wp-content/plugins/elementor-pro/assets/css/frontend-lite.min.css?ver=3.22.0" media="all" href="https://www.intrepidonline.com/wp-content/plugins/elementor-pro/assets/css/frontend-lite.min.css?ver=3.22.0">
    <link rel="stylesheet" id="font-awesome-5-all-css" data-pmdelayedstyle="https://www.intrepidonline.com/wp-content/plugins/elementor/assets/lib/font-awesome/css/all.min.css?ver=3.22.1" media="all" href="https://www.intrepidonline.com/wp-content/plugins/elementor/assets/lib/font-awesome/css/all.min.css?ver=3.22.1">
    <style>
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app title
st.title('Sitemap URL Scraper')

# Subtitle
st.markdown(
    """
    by [Intrepid Digital](https://www.intrepidonline.com/)
    """,
    unsafe_allow_html=True
)

# User input for URL
sitemap_url = st.text_input('Enter the URL of the sitemap', 'https://www.WEBSITE.com/sitemap.xml')

# Button to execute the scraping
if st.button('Scrape Sitemap'):
    if sitemap_url:
        # Use sitemap_to_df to extract URLs
        df = sitemap_to_df(sitemap_url)
        
        # Display the DataFrame in the app (optional)
        st.write(df[['loc', 'sitemap']])
        
        # Convert DataFrame to CSV for download
        csv = df[['loc', 'sitemap']].to_csv(index=False).encode('utf-8')
        
        # Create a button to download the CSV file
        st.download_button(label="Download URLs as CSV",
                           data=csv,
                           file_name="sitemap_urls.csv",
                           mime='text/csv')
    else:
        st.error("Please enter a valid URL.")
