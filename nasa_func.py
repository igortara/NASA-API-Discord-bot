# --- Importing necessary libraries ---
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import io


# --- Functions ---
def get_nasa_image(type):
    today = datetime.now().strftime("%Y-%m-%d")
    ext = None

    if type == "FIRMS":
        ext = "VIIRS_SNPP_Thermal_Anomalies_375m_All"
    elif type == "TrueColor":
        ext = "VIIRS_SNPP_CorrectedReflectance_TrueColor"

    args = {
        "SERVICE": "WMS",
        "VERSION": "1.3.0",
        "REQUEST": "GetMap",
        "LAYERS": f"{ext}",
        "STYLES": "",
        "FORMAT": "image/jpeg",
        "CRS": "EPSG:4326",
        "WIDTH": "1920",
        "HEIGHT": "1080",
        "BBOX": "30, -10, 70, 60",
        "TIME": today,
    }
    resp = requests.get(
        "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi?", params=args
    )
    if resp.status_code == 200:
        b = io.BytesIO(resp.content)
        b.seek(0)
        return b
    else:
        return None


def get_apod_image():
    apod_url = "https://apod.nasa.gov/apod/astropix.html"
    soup = BeautifulSoup(requests.get(apod_url).content, "html.parser")
    find_img = soup.find("img")
    if find_img is not None:
        return f"https://apod.nasa.gov/apod/{find_img['src']}"
    else:
        return None
