import streamlit as st
import pandas as pd
from advertools import sitemap_to_df

# Custom CSS for styling and external stylesheet
st.markdown(
    """
    <link rel="stylesheet" id="astra-theme-css-css" data-pmdelayedstyle="https://www.intrepidonline.com/wp-content/themes/astra/assets/css/minified/main.min.css?ver=4.6.8" media="all" href="https://www.intrepidonline.com/wp-content/themes/astra/assets/css/minified/main.min.css?ver=4.6.8">
    <link media="all" onload="this.media='all';this.onload=null;" rel="stylesheet" id="astra-google-fonts-css" href="https://www.intrepidonline.com/wp-content/cache/perfmatters/www.intrepidonline.com/fonts/8f516dc4344f.google-fonts.css">
    <link rel="stylesheet" id="astra-theme-dynamic-css" data-pmdelayedstyle="https://www.intrepidonline.com/wp-content/uploads/astra/astra-theme-dynamic-css-post-7386.css?ver=1720711612" media="all" href="https://www.intrepidonline.com/wp-content/uploads/astra/astra-theme-dynamic-css-post-7386.css?ver=1720711612">
    <link rel="stylesheet" id="additional-styles-css" data-pmdelayedstyle="https://www.intrepidonline.com/wp-content/themes/astra-child/dist/css/astraChild.min.css?ver=1.002" media="all" href="https://www.intrepidonline.com/wp-content/themes/astra-child/dist/css/astraChild.min.css?ver=1.002">
    <link rel="stylesheet" id="astra-addon-css-css" data-pmdelayedstyle="https://www.intrepidonline.com/wp-content/uploads/astra-addon/astra-addon-668f8149383bd2-70380954.css?ver=4.6.8" media="all" href="https://www.intrepidonline.com/wp-content/uploads/astra-addon/astra-addon-668f8149383bd2-70380954.css?ver=4.6.8">
    <link rel="stylesheet" id="astra-addon-dynamic-css" data-pmdelayedstyle="https://www.intrepidonline.com/wp-content/uploads/astra-addon/astra-addon-dynamic-css-post-7386.css?ver=1720711612" media="all" href="https://www.intrepidonline.com/wp-content/uploads/astra-addon/astra-addon-dynamic-css-post-7386.css?ver=1720711612">
    <link rel="stylesheet" id="elementor-frontend-css" data-pmdelayedstyle="https://www.intrepidonline.com/wp-content/plugins/elementor/assets/css/frontend-lite.min.css?ver=3.22.1" media="all" href="https://www.intrepidonline.com/wp-content/plugins/elementor/assets/css/frontend-lite.min.css?ver=3.22.1">
    <link rel="stylesheet" id="swiper-css" data-pmdelayedstyle="https://www.intrepidonline.com/wp-content/plugins/elementor/assets/lib/swiper/v8/css/swiper.min.css?ver=8.4.5" media="all" href="https://www.intrepidonline.com/wp-content/plugins/elementor/assets/lib/swiper/v8/css/swiper.min.css?ver=8.4.5">
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
