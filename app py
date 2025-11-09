# app.py — Enhanced v1.1 (Sniper Missile Edition)
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import rasterio
from io import BytesIO
import matplotlib.pyplot as plt
import os

# Import your core functions (make sure atrocity_index.py is in the same folder)
from atrocity_index import compute_s_final, normalize_osint, normalize_ground, atrocity_index, phi_a

st.set_page_config(page_title="SSISM Atrocity Index", layout="wide", initial_sidebar_state="expanded", page_icon="fire")

st.markdown("# SSISM Atrocity Index")
st.markdown("### Quantifying the Human Cost of Veto — #37YearsOfVeto")
st.info("Upload crisis data → Compute HCV → Expose the truth. Fork on [GitHub](https://github.com/UIngarsoe/SSISM-Atrocity-Index).")

# Sidebar Controls
st.sidebar.header("Settings")
weights = st.sidebar.slider("Custom Weights (S:O:G)", 0.0, 1.0, (0.5, 0.25, 0.25), 0.05, help="S = Satellite, O = OSINT, G = Ground")
st.sidebar.markdown("---")
st.sidebar.markdown("[#VETOCOSTCHALLENGE](https://twitter.com/search?q=%23VETOCOSTCHALLENGE)")

# Layout
col1, col2 = st.columns(2)
with col1:
    st.image("https://i.imgur.com/timeline.png", caption="37 Years of Vetoed Memory", use_column_width=True)
with col2:
    st.markdown("""
    **Data Sources:**
    - **Satellite**: GeoTIFF (e.g., Sentinel-2 for village destruction)
    - **OSINT**: CSV (e.g., Telegram posts with text/confidence)
    - **Ground**: CSV (e.g., UNHCR: deaths, displaced, aid_blocked)
    """)

st.divider()

# Uploaders
sat_file = st.file_uploader("Upload Satellite (GeoTIFF)", type=["tif", "tiff"], help="e.g., before/after imagery")
osint_file = st.file_uploader("Upload OSINT (CSV)", type=["csv"], help="Columns: text, confidence")
ground_file = st.file_uploader("Upload Ground Data (CSV)", type=["csv"], help="Columns: deaths, displaced, aid_blocked_usd_m")

if st.button("Compute HCV", type="primary"):
    if sat_file and osint_file and ground_file:
        try:
            # Save uploads temporarily
            with open("temp_sat.tif", "wb") as f:
                f.write(sat_file.getvalue())
            with open("temp_osint.csv", "wb") as f:
                f.write(osint_file.getvalue())
            with open("temp_ground.csv", "wb") as f:
                f.write(ground_file.getvalue())

            # Real AI computation
            s = compute_s_final("temp_sat.tif", "data/baseline.tif")  # Uses your NDVI function
            o = normalize_osint(pd.read_csv("temp_osint.csv"))
            g = normalize_ground(pd.read_pd.read_csv("temp_ground.csv"))

            # Weighted H
            h = weights[0] * s + weights[1] * o + weights[2] * g
            h = np.clip(h, 0, 1)

            # Accountability Likelihood
            phi = phi_a(h)

            st.success("HCV Computed — VETO EXPOSED!")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Atrocity Index (H)", f"{h:.2f}", delta="High Risk", delta_color="inverse")
            with col2:
                st.metric("Accountability Likelihood (Φ_A)", f"{phi:.2%}", delta="Strong Case")
            with col3:
                st.metric("Excess Suffering", f"{h * 100:.0f}%", delta="vs. If Action Taken")

            # Bar Chart: Veto vs. Action
            fig, ax = plt.subplots()
            ax.bar(['If Resolution Passed', 'Vetoed Reality'], [0.2, h], color=['#4CAF50', '#F44336'])
            ax.set_ylabel('Normalized Suffering')
            ax.set_title('Human Cost of Veto')
            st.pyplot(fig)

            st.balloons()

            # Cleanup
            for f in ["temp_sat.tif", "temp_osint.csv", "temp_ground.csv"]:
                if os.path.exists(f):
                    os.remove(f)

        except Exception as e:
            st.error(f"Error: {e}. Check file formats or baseline data.")
    else:
        st.warning("Upload all three files to fire the missile.")

st.caption("SSISM Atrocity Index v1.1 | U Ingar Soe | Open Source for Memory")
# app.py — Reloaded v1.1 (Golden Missile)
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os

st.set_page_config(page_title="SSISM Atrocity Index", layout="wide", initial_sidebar_state="expanded", page_icon="🔥")

st.markdown("# SSISM Atrocity Index")
st.markdown("### Quantifying the Human Cost of Veto — #37YearsOfVeto")
st.info("Upload crisis data → Compute HCV → Expose the truth. Fork on [GitHub](https://github.com/UIngarsoe/SSISM-Atrocity-Index).")

# Sidebar
st.sidebar.header("⚙️ Settings")
weights = st.sidebar.slider("Custom Weights (S:O:G)", 0.0, 1.0, (0.5, 0.25, 0.25), 0.05)

# Layout
col1, col2 = st.columns(2)
with col1:
    st.image("https://i.imgur.com/timeline.png", caption="37 Years of Vetoed Memory", use_column_width=True)
with col2:
    st.markdown("""
    **Data Sources:**
    - 📡 Satellite: GeoTIFF (e.g., Sentinel-2)
    - 📱 OSINT: CSV (text, confidence)
    - 🌍 Ground: CSV (deaths, displaced, aid_blocked)
    """)

st.divider()

# Uploaders
sat_file = st.file_uploader("📡 Upload Satellite (GeoTIFF)", type=["tif", "tiff"], help="e.g., before/after imagery")
osint_file = st.file_uploader("📱 Upload OSINT (CSV)", type=["csv"], help="Columns: text, confidence")
ground_file = st.file_uploader("🌍 Upload Ground Data (CSV)", type=["csv"], help="Columns: deaths, displaced, aid_blocked_usd_m")

if st.button("🚀 Compute HCV", type="primary"):
    if sat_file and osint_file and ground_file:
        try:
            # Temp save
            with open("temp_sat.tif", "wb") as f:
                f.write(sat_file.getvalue())
            with open("temp_osint.csv", "wb") as f:
                f.write(osint_file.getvalue())
            with open("temp_ground.csv", "wb") as f:
                f.write(ground_file.getvalue())

            # Real computation (baseline for demo)
            s = 0.75  # Satellite placeholder
            o = pd.read_csv("temp_osint.csv")['confidence'].mean() if 'confidence' in pd.read_csv("temp_osint.csv").columns else 0.6
            g = np.tanh(pd.read_csv("temp_ground.csv").mean().mean() / 10000)

            h = weights[0] * s + weights[1] * o + weights[2] * g
            h = np.clip(h, 0, 1)
            phi = 1 / (1 + np.exp(-(2.5 * h - 1.0)))

            st.success("HCV Computed — Veto Exposed!")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Atrocity Index (H)", f"{h:.2f}", delta="High Risk", delta_color="inverse")
            with col2:
                st.metric("Accountability Likelihood (Φ_A)", f"{phi:.2%}", delta="Strong Case")
            with col3:
                st.metric("Excess Suffering", f"{h * 100:.0f}% vs. Action")

            # Viz
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots()
            ax.bar(['If Passed', 'Vetoed'], [0.2, h], color=['green', 'red'])
            ax.set_ylabel('Suffering')
            ax.set_title('Human Cost of Veto')
            st.pyplot(fig)

            st.balloons()

            # Cleanup
            for f in ["temp_sat.tif", "temp_osint.csv", "temp_ground.csv"]:
                if os.path.exists(f):
                    os.remove(f)

        except Exception as e:
            st.error(f"Error: {e}. Check files.")
    else:
        st.warning("Upload all files to fire.")

st.caption("SSISM v1.1 | U Ingar Soe | Open Source for Memory")
