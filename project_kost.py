import streamlit as st
import folium
from streamlit_folium import st_folium
import heapq
from collections import defaultdict
import math
import pandas as pd

st.set_page_config(page_title="DSS Kost Udayana", layout="wide")

LOKASI = {
    "Kampus Udayana": {
        "tipe": "kampus",
        "lat": -8.7975, "lon": 115.1686,
        "harga": 0, "fasilitas": "-", "rating": 0,
        "deskripsi": "Universitas Udayana, Jimbaran, Bali"
    },
    "Kost Jimbaran Asri": {
        "tipe": "kost", "lat": -8.7920, "lon": 115.1720,
        "harga": 900000, "fasilitas": "WiFi, AC",
        "rating": 4.3, "deskripsi": "Kost bersih dekat kampus, ada AC dan WiFi"
    },
    "Kost Mutiara": {
        "tipe": "kost", "lat": -8.8010, "lon": 115.1750,
        "harga": 750000, "fasilitas": "WiFi, Dapur, Parkir",
        "rating": 4.1, "deskripsi": "Kost ekonomis dengan dapur bersama"
    },
    "Kost Bali Indah": {
        "tipe": "kost", "lat": -8.7880, "lon": 115.1640,
        "harga": 1800000, "fasilitas": "WiFi, AC, Laundry, Parkir",
        "rating": 4.8, "deskripsi": "Kost premium lengkap fasilitas"
    },
    "Kost Sejahtera": {
        "tipe": "kost", "lat": -8.8050, "lon": 115.1620,
        "harga": 700000, "fasilitas": "Dapur, Parkir",
        "rating": 3.8, "deskripsi": "Kost ekonomis cocok untuk mahasiswa"
    },
    "Kost Harmoni": {
        "tipe": "kost", "lat": -8.7850, "lon": 115.1780,
        "harga": 1400000, "fasilitas": "WiFi, AC, Laundry",
        "rating": 4.6, "deskripsi": "Kost nyaman dengan suasana tenang"
    },
    "Kost Matahari": {
        "tipe": "kost", "lat": -8.8080, "lon": 115.1700,
        "harga": 1100000, "fasilitas": "WiFi, AC, Parkir",
        "rating": 4.4, "deskripsi": "Kost strategis dekat jalan utama"
    },
    "Kost Bukit Permai": {
        "tipe": "kost", "lat": -8.7940, "lon": 115.1650,
        "harga": 800000, "fasilitas": "WiFi, Dapur",
        "rating": 3.9, "deskripsi": "Kost murah dengan view bukit Jimbaran"
    },
    "Kost Griya Santai": {
        "tipe": "kost", "lat": -8.7900, "lon": 115.1760,
        "harga": 1250000, "fasilitas": "WiFi, AC, Dapur",
        "rating": 4.2, "deskripsi": "Kost santai lingkungan tenang dekat kampus"
    },
    "Kost Pesona Bali": {
        "tipe": "kost", "lat": -8.8020, "lon": 115.1680,
        "harga": 1600000, "fasilitas": "WiFi, AC, Laundry",
        "rating": 4.5, "deskripsi": "Kost nuansa Bali, bersih dan nyaman"
    },
    "Kost Mahasiswa Jimbaran": {
        "tipe": "kost", "lat": -8.8000, "lon": 115.1600,
        "harga": 700000, "fasilitas": "Dapur, Parkir",
        "rating": 3.7, "deskripsi": "Kost terjangkau pilihan mahasiswa hemat"
    },
    "Kost Nusa Indah": {
        "tipe": "kost", "lat": -8.7860, "lon": 115.1720,
        "harga": 1050000, "fasilitas": "WiFi, AC, Parkir",
        "rating": 4.3, "deskripsi": "Kost dengan parkir luas dan keamanan 24 jam"
    },
    "Kost Villa Jimbaran": {
        "tipe": "kost", "lat": -8.7830, "lon": 115.1660,
        "harga": 2000000, "fasilitas": "WiFi, AC, Laundry, Parkir, Dapur",
        "rating": 4.9, "deskripsi": "Kost mewah setara villa, fasilitas terlengkap"
    },
    "Kost Tirta Sari": {
        "tipe": "kost", "lat": -8.8030, "lon": 115.1730,
        "harga": 950000, "fasilitas": "WiFi, Dapur, Parkir",
        "rating": 4.0, "deskripsi": "Kost tenang dekat area persawahan Jimbaran"
    },
}


def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) *
         math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) ** 2)
    return R * 2 * math.asin(math.sqrt(a))


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = set()

    def tambah_edge(self, a, b, jarak):
        self.nodes.add(a)
        self.nodes.add(b)
        self.graph[a].append((b, jarak))
        self.graph[b].append((a, jarak))

    def dijkstra(self, start):
        dist = {n: float('inf') for n in self.nodes}
        dist[start] = 0
        prev = {n: None for n in self.nodes}
        pq = [(0, start)]
        while pq:
            jarak_kini, node = heapq.heappop(pq)
            for tetangga, bobot in self.graph[node]:
                jarak_baru = jarak_kini + bobot
                if jarak_baru < dist[tetangga]:
                    dist[tetangga] = jarak_baru
                    prev[tetangga] = node
                    heapq.heappush(pq, (jarak_baru, tetangga))
        return dist, prev

    def ambil_jalur(self, prev, start, end):
        if end not in prev:
            return []
        jalur = []
        node = end
        while node is not None:
            jalur.append(node)
            node = prev.get(node)
        jalur.reverse()
        return jalur if jalur and jalur[0] == start else []


def buat_graph():
    g = Graph()
    nama_list = list(LOKASI.keys())
    for i in range(len(nama_list)):
        for j in range(i + 1, len(nama_list)):
            a, b = nama_list[i], nama_list[j]
            jarak = haversine(
                LOKASI[a]["lat"], LOKASI[a]["lon"],
                LOKASI[b]["lat"], LOKASI[b]["lon"]
            )
            g.tambah_edge(a, b, round(jarak, 2))
    return g

graph = buat_graph()


def rekomendasikan(dist, prev, budget_max, fasilitas_filter):
    hasil = []
    for nama, info in LOKASI.items():
        if info["tipe"] != "kost":
            continue
        if info["harga"] > budget_max:
            continue
        if fasilitas_filter != "Semua" and fasilitas_filter not in info["fasilitas"]:
            continue
        jarak = dist.get(nama, float('inf'))
        if jarak == float('inf'):
            continue
        jalur = graph.ambil_jalur(prev, "Kampus Udayana", nama)
        skor = (jarak * 0.4) + (info["harga"] / 1000000 * 0.2) - (info["rating"] * 0.4)
        hasil.append({
            "nama":      nama,
            "jarak":     round(jarak, 2),
            "harga":     info["harga"],
            "fasilitas": info["fasilitas"],
            "rating":    info["rating"],
            "deskripsi": info["deskripsi"],
            "jalur":     jalur,
            "skor":      round(skor, 2),
        })
    hasil.sort(key=lambda x: x["skor"])
    return hasil


def buat_peta(rekomendasi, jalur_highlight=None):
    peta = folium.Map(
        location=[-8.7975, 115.1686],
        zoom_start=14,
        tiles="OpenStreetMap"
    )

    nama_list = list(LOKASI.keys())
    for i in range(len(nama_list)):
        for j in range(i + 1, len(nama_list)):
            a, b = nama_list[i], nama_list[j]
            folium.PolyLine(
                locations=[[LOKASI[a]["lat"], LOKASI[a]["lon"]],
                            [LOKASI[b]["lat"], LOKASI[b]["lon"]]],
                color="#94a3b8", weight=1, opacity=0.3, dash_array="5"
            ).add_to(peta)

    if jalur_highlight and len(jalur_highlight) > 1:
        folium.PolyLine(
            locations=[[LOKASI[n]["lat"], LOKASI[n]["lon"]] for n in jalur_highlight],
            color="#ef4444", weight=4, opacity=0.9,
            tooltip="Jalur terpendek Dijkstra"
        ).add_to(peta)

    nama_rekomendasi = [r["nama"] for r in rekomendasi]
    for nama, info in LOKASI.items():
        if info["tipe"] == "kampus":
            icon = folium.Icon(color="orange", icon="university", prefix="fa")
            popup_text = f"<b>🏫 {nama}</b><br>{info['deskripsi']}"
        else:
            rank = nama_rekomendasi.index(nama) + 1 if nama in nama_rekomendasi else None
            color = "red" if rank == 1 else "blue" if rank else "gray"
            icon = folium.Icon(color=color, icon="home", prefix="fa")
            rank_label = f"⭐ Rekomendasi #{rank}" if rank else "Tidak lolos filter"
            popup_text = f"""
                <div style='font-family:sans-serif;min-width:190px;font-size:13px'>
                    <b>{'🥇 ' if rank==1 else '🏠 '}{nama}</b><br>
                    <span style='color:{'crimson' if rank else 'gray'};font-weight:bold'>{rank_label}</span>
                    <hr style='margin:5px 0'>
                    💰 Rp {info['harga']:,}/bulan<br>
                    ⭐ Rating: {info['rating']}<br>
                    🛠️ {info['fasilitas']}<br>
                    📝 {info['deskripsi']}
                </div>
            """
        folium.Marker(
            location=[info["lat"], info["lon"]],
            popup=folium.Popup(popup_text, max_width=230),
            tooltip=nama,
            icon=icon
        ).add_to(peta)
    return peta


st.title("🏠 DSS Pemilihan Kost — Universitas Udayana, Bali")
st.caption("Rekomendasi kost berbasis Graph + Algoritma Dijkstra dengan peta nyata OpenStreetMap")
st.divider()

with st.sidebar:
    st.header("⚙️ Filter Pencarian")
    budget = st.slider(
        "💰 Budget Maksimum (Rp/bulan)",
        min_value=700000, max_value=2000000,
        value=1200000, step=50000,
        format="Rp %d"
    )
    fasilitas = st.selectbox(
        "🏷️ Fasilitas yang Diinginkan",
        ["Semua", "WiFi", "AC", "Dapur", "Parkir", "Laundry"]
    )
    st.divider()
    st.markdown("**🗺️ Legend Peta:**")
    st.markdown("🟠 Kampus Udayana")
    st.markdown("🔴 Rekomendasi #1")
    st.markdown("🔵 Rekomendasi lainnya")
    st.markdown("⚫ Tidak lolos filter")
    st.markdown("━━ Garis merah = jalur Dijkstra")

dist, prev = graph.dijkstra("Kampus Udayana")
rekomendasi = rekomendasikan(dist, prev, budget, fasilitas)

col_peta, col_hasil = st.columns([1.5, 1])

with col_peta:
    st.subheader("🗺️ Peta Kost Area Udayana")
    jalur_tampil = rekomendasi[0]["jalur"] if rekomendasi else None
    peta = buat_peta(rekomendasi, jalur_highlight=jalur_tampil)
    st_folium(peta, width=700, height=500)
    if jalur_tampil:
        st.info(
            f"🔴 Jalur merah → **{rekomendasi[0]['nama']}** "
            f"({rekomendasi[0]['jarak']} km dari kampus)"
        )

with col_hasil:
    st.subheader(f"✨ Rekomendasi ({len(rekomendasi)} kost)")
    if not rekomendasi:
        st.warning("Tidak ada kost yang sesuai. Coba naikkan budget atau ubah filter fasilitas.")
    else:
        for i, k in enumerate(rekomendasi):
            with st.expander(f"#{i+1}  {k['nama']}  ⭐ {k['rating']}", expanded=(i == 0)):
                st.caption(k['deskripsi'])
                st.divider()
                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown("📏 **Jarak dari Kampus**")
                    st.markdown(f"### {k['jarak']} km")
                with col_b:
                    st.markdown("⭐ **Rating**")
                    st.markdown(f"### {k['rating']}")
                col_c, col_d = st.columns(2)
                with col_c:
                    st.markdown("💰 **Harga / bulan**")
                    st.markdown(f"### Rp {k['harga']:,}")
                with col_d:
                    st.markdown("🎯 **Skor DSS**")
                    st.markdown(f"### {k['skor']}")
                st.divider()
                st.markdown(f"🛠️ **Fasilitas:** {k['fasilitas']}")
                st.markdown(f"🗺️ **Jalur:** `{'  →  '.join(k['jalur'])}`")

st.divider()

st.subheader("📊 Hasil Dijkstra — Jarak Terpendek dari Kampus Udayana")
rows = []
for nama, info in LOKASI.items():
    if info["tipe"] != "kost":
        continue
    jalur = graph.ambil_jalur(prev, "Kampus Udayana", nama)
    lolos = "✅" if nama in [r["nama"] for r in rekomendasi] else "❌"
    rows.append({
        "Kost":         nama,
        "Jarak (km)":   round(dist[nama], 2),
        "Harga (Rp)":   f"Rp {info['harga']:,}",
        "Rating":       info["rating"],
        "Fasilitas":    info["fasilitas"],
        "Lolos Filter": lolos,
        "Jalur":        " → ".join(jalur),
    })
df = pd.DataFrame(rows).sort_values("Jarak (km)")
st.dataframe(df, use_container_width=True, hide_index=True)

st.caption("Project Struktur Data | DSS Pemilihan Kost | Graph + Dijkstra + Folium Maps")