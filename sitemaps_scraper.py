import streamlit as st
import pandas as pd
from advertools import sitemap_to_df

# ---- Intrepid look (gointrepid.com) -------------------------------------------------------------------------
# Colours and fonts come from .streamlit/config.toml; this adds the logo, the link back to the tools page, the
# title and the card around the tool. static/logo-white.png is served because enableStaticServing = true.
st.set_page_config(page_title="Sitemap Extractor | Intrepid Digital", layout="centered")
st.html("""
<style>
/* Streamlit chrome: hide the top bar, its menu and the status widget. */
header[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stStatusWidget"] { display: none !important; }
.block-container { padding-top: 0 !important; max-width: 900px !important; }

/* Top row: the site logo at the size gointrepid.com uses (63px tall) and a link back to the tools page. */
.id-top { display: flex; align-items: center; justify-content: space-between; gap: 16px; padding: 28px 0 0; }
.id-top img { height: 63px; width: auto; display: block; }
.id-back { font-family: 'IBM Plex Mono', monospace; font-size: 12px; font-weight: 700; letter-spacing: .08em; text-transform: uppercase;
  color: #a2ff2c !important; text-decoration: none !important; white-space: nowrap; }
.id-back:hover { color: #95ff0e !important; }
@media (max-width: 640px) { .id-top img { height: 48px; } }

/* Hero */
.id-hero { padding: 56px 0 36px; }
.id-hero h1 { font-size: clamp(36px, 5.5vw, 64px) !important; line-height: 1.08 !important; letter-spacing: -.02em; padding: 0 0 18px !important; }
.id-hero h1 { margin: 0 !important; }
.id-hero p { margin: 4px 0 0 !important; font-size: 18px; line-height: 1.6; color: #bfbaba; max-width: 700px; }
.id-hero p strong { color: #e8eaf0; }

/* Tool card: the outer block gets the site's surface + volt edge. */
.st-key-tool { background: #1e1c1c; border: 1px solid rgba(255,255,255,.08); border-left: 3px solid #a2ff2c; padding: 36px 36px 32px; }

/* Uploader: dashed drop zone, centred. */
[data-testid="stFileUploaderDropzone"] { border: 1.5px dashed rgba(255,255,255,.18) !important; background: rgba(255,255,255,.02) !important; padding: 32px 20px !important; }
[data-testid="stFileUploaderDropzone"]:hover { border-color: #a2ff2c !important; background: rgba(162,255,44,.05) !important; }
[data-testid="stWidgetLabel"] p { font-family: 'IBM Plex Mono', monospace; font-size: 11px !important; letter-spacing: .14em; text-transform: uppercase; color: #6b6666 !important; }

/* Buttons: volt, dark ink, uppercase, as the site CTAs. */
.stButton button, .stDownloadButton button, [data-testid="stFileUploaderDropzone"] button { border-radius: 2px !important; }
.stButton button, .stDownloadButton button { background: #a2ff2c !important; border: 0 !important; padding: 14px 28px !important; }
.stButton button:hover, .stDownloadButton button:hover { background: #95ff0e !important; }
.stButton button p, .stDownloadButton button p { color: #0a0b0f !important; font-weight: 700 !important; font-size: 13px !important; letter-spacing: .04em; text-transform: uppercase; }

/* Metrics as the stat tiles. */
[data-testid="stMetric"] { background: #2a2828; padding: 14px 18px; }
[data-testid="stMetricValue"] { font-family: Outfit, sans-serif; font-weight: 800; }
[data-testid="stMetricLabel"] p { font-family: 'IBM Plex Mono', monospace; font-size: 11px !important; letter-spacing: .12em; text-transform: uppercase; color: #6b6666 !important; }
</style>
""")
st.html("""
<div class="id-top">
  <a href="https://www.gointrepid.com/tools/" target="_blank" rel="noopener"><img src="app/static/logo-white.png" alt="Intrepid Digital"></a>
  <a class="id-back" href="https://www.gointrepid.com/tools/" target="_blank" rel="noopener">&larr; All Tools</a>
</div>
<div class="id-hero">
  <h1>Sitemap Extractor</h1>
  <p>Enter a sitemap's URL to list every page in it (sitemap indexes included), then download the list as a CSV.</p>
</div>
""")
# --------------------------------------------------------------------------------------------------------------

# User input for URL
with st.container(key="tool"):
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
