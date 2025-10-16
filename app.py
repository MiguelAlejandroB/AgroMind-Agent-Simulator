import streamlit as st
import requests
import random
from datetime import datetime

# --- Agente 1: Experto en Clima (Usa API Real de Open-Meteo) ---
class ClimateAgent:
    """Agente que obtiene datos climáticos reales para una coordenada específica."""
    def get_forecast(self, lat, lon):
        try:
            url = "https://api.open-meteo.com/v1/forecast"
            params = {
                "latitude": lat,
                "longitude": lon,
                "hourly": "temperature_2m,precipitation_probability",
                "forecast_days": 1
            }
            response = requests.get(url, params=params)
            response.raise_for_status()  # Esto lanzará un error si la petición falla
            data = response.json()
            
            # Obtenemos el pronóstico para la hora actual
            current_hour_index = datetime.now().hour
            temp = data['hourly']['temperature_2m'][current_hour_index]
            rain_chance = data['hourly']['precipitation_probability'][current_hour_index]

            st.info(f"🌦️ **Climate Agent:** Forecast obtained. Temperature: **{temp}°C**, Rainfall probability: **{rain_chance}%**.")
            return {"temperature": temp, "rain_chance": rain_chance}
        except requests.exceptions.RequestException as e:
            st.error(f"Error en Agente Climático: No se pudo conectar a la API del clima. {e}")
            return None

# --- Agente 2: Experto Satelital (Simula NDVI para la demo) ---
class SatelliteAgent:
    """Agente que simula el análisis de imágenes satelitales para obtener el NDVI."""
    def get_ndvi(self, lat, lon):
        # En una aplicación real, aquí iría una llamada a una API como Sentinel Hub.
        # Para esta demo, simulamos un valor de NDVI realista.
        # Un NDVI < 0.4 indica posible estrés en la vegetación.
        ndvi = round(random.uniform(0.25, 0.85), 2) 
        
        st.info(f"🛰️ **Satellite Agent:** Analysis completed. Plant Health Index (NDVI) is **{ndvi}**.")
        
        if ndvi < 0.4:
            st.warning("The NDVI is low, which could indicate crop water stress.")
            
        return {"ndvi": ndvi}

# --- Agente 3: Experto en Decisión (Usa la lógica para sintetizar) ---
class DecisionAgent:
    """Agente que toma decisiones lógicas basadas en los datos de los otros agentes."""
    def analyze_and_decide(self, climate_data, satellite_data):
        temp = climate_data["temperature"]
        rain = climate_data["rain_chance"]
        ndvi = satellite_data["ndvi"]
        
        st.write("---")
        st.subheader("🧠 Decision Agent Reasoning:")
        
        # Lógica de decisión que combina ambos factores
        if ndvi < 0.4 and rain < 20:
            return "**🔥 CRITICAL ALERT:** The crop is showing stress (low NDVI) and no rainfall is expected. **IRRIGATION IS URGENTLY REQUIRED!**"
        elif temp > 30 and ndvi < 0.5 and rain < 30:
            return "**💧 RECOMMENDATION:** It's hot and the crop is showing mild stress. **Irrigation is recommended.**"
        elif rain > 60:
            return "**👍 OPTIMAL STATE:** Enough rainfall is expected. **No irrigation is required.**"
        else:
            return "**🤔 MONITORING:** The conditions are stable. **Reevaluate in 12 hours.**"

# --- Interfaz Gráfica con Streamlit ---
st.set_page_config(page_title="Panel de Decisión Agrícola", page_icon="🤖", layout="wide")

st.title("🤖 Multi-Agent Agricultural Decision Panel")
st.markdown("A collaborative AI simulation that uses real-time weather data to decide whether to irrigate a crop.")

# Coordenadas de ejemplo (un campo en Colombia)
col1, col2 = st.columns(2)
with col1:
    lat = st.number_input("Latitude", value=4.7110, format="%.4f")
with col2:
    lon = st.number_input("Longitude", value=-74.0721, format="%.4f")

if st.button("Analyze with a team of Agents", type="primary"):
    st.write(f"**Starting analysis for the coordinates:: `{lat}, {lon}`**")
    st.write("---")
    
    # 1. Desplegar agentes
    climate_expert = ClimateAgent()
    satellite_expert = SatelliteAgent()
    decision_maker = DecisionAgent()
    
    # 2. Obtener datos de los agentes especialistas
    climate_report = climate_expert.get_forecast(lat, lon)
    satellite_report = satellite_expert.get_ndvi(lat, lon)
    
    # 3. Tomar decisión si ambos agentes tuvieron éxito
    if climate_report and satellite_report:
        final_decision = decision_maker.analyze_and_decide(climate_report, satellite_report)
        st.header("🏁 Final Decision of the Team:")
        st.success(final_decision)
else:
    st.info("Enter the coordinates and press 'Analyze'.")