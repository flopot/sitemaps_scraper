import streamlit as st
import pandas as pd
from advertools import sitemap_to_df

# Custom CSS for styling and external stylesheet
st.markdown(
    """
    <style>
    .stHeadingWithActionElements,.stMarkdown,.stMarkdownContainer,.st-ae,.st-bd,.st-be,.st-bf,.st-bg,.st-bh,.st-bi,.st-bj,.st-bk,.st-bl,.st-bm,.st-ah,.st-bn,.st-bo,.st-bp,.st-bq,.st-br,.st-bs,.st-bt,.st-bu,.st-ax,.st-ay,.st-az,.st-bv,.st-b1,.st-b2,.st-bc,.st-bw,.st-bx,.st-by{
        color: black
    }

    appview-container, button {
        background-color: white
    }
    
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
