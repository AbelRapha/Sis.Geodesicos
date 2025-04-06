import math

# Função para converter coordenadas de graus, minutos, segundos (gms) para decimal
def gms_para_decimal(g, m, s):
    if g > 0:
        return g + (m / 60) + (s / 3600)
    if g < 0:
        return g - (m / 60) - (s / 3600)


# Função para o método de Molodensky
def molodensky(lat, lon, h, dX, dY, dZ, a1, e1, a2, e2):
    # Convertendo latitude e longitude para radianos
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)

    # Parâmetros intermediários do elipsóide de origem
    RN = a1 / math.sqrt(1 - e1**2 * math.sin(lat_rad)**2)
    RM = RN * (1 - e1**2) / (1 - e1**2 * math.sin(lat_rad)**2)

    # Diferença de coordenadas geodésicas
    dLat = ((-dX * math.sin(lat_rad) * math.cos(lon_rad) - 
             dY * math.sin(lat_rad) * math.sin(lon_rad) + 
             dZ * math.cos(lat_rad)) + 
            (RN * e1**2 * math.sin(lat_rad) * math.cos(lat_rad)) * 
            (a2 - a1) / a1) / (RM + h)
    
    dLon = (-dX * math.sin(lon_rad) + dY * math.cos(lon_rad)) / ((RN + h) * math.cos(lat_rad))
    dH = dX * math.cos(lat_rad) * math.cos(lon_rad) + dY * math.cos(lat_rad) * math.sin(lon_rad) + dZ * math.sin(lat_rad) - (a2 - a1) * RN / a1

    # Aplicando as diferenças
    lat2 = lat + math.degrees(dLat)
    lon2 = lon + math.degrees(dLon)
    h2 = h + dH

    return lat2, lon2, h2

# Exemplo de parâmetros para os sistemas geodésicos
sistemas_de_sirgas = {
    "SAD-69": {"dX": +66.86, "dY": -4.37, "dZ": +38.52, "a": 6378160, "e2": 0.00669454185},
    "WGS-84": {"dX": 0, "dY": 0, "dZ": 0, "a": 6378137, "e2": 0.00669437999},
    "SIRGAS 2000": {"dX": 0, "dY": 0, "dZ": 0, "a": 6378137, "e2": 0.00669437999},
    "Córrego Alegre": {"dX": +205.56, "dY": -168.77, "dZ": +4.12, "a": 6378388, "e2": 0.00672267},
}

sistemas_de_wgs = {
    "SIRGAS 2000": {"dX": 0, "dY": 0, "dZ": 0, "a": 6378137, "e2": 0.00669437999},
    "SAD-69": {"dX": +66.86, "dY": -4.37, "dZ": +38.52, "a": 6378160, "e2": 0.00669454185},
    "Córrego Alegre": {"dX": +205.56, "dY": -168.77, "dZ": +4.12, "a": 6378388, "e2": 0.00672267},
    "WGS-84": {"dX": 0, "dY": 0, "dZ": 0, "a": 6378137, "e2": 0.00669437999}
}

sistemas_de_sad = {
    "SIRGAS 2000": {"dX": -66.86, "dY": +4.37, "dZ": -38.52, "a": 6378137, "e2": 0.00669437999},
    "WGS-84": {"dX": -66.86, "dY": +4.37, "dZ": -38.52, "a": 6378137, "e2": 0.00669437999},
    "Córrego Alegre": {"dX": +138.70, "dY": -164.40, "dZ": -34.40, "a": 6378388, "e2": 0.00672267},
    "SAD-69": {"dX": 0, "dY": 0, "dZ": 0, "a": 6378160, "e2": 0.00669454185}
}

sistemas_de_corrego = {
    "SIRGAS 2000": {"dX": -205.56, "dY": +168.77, "dZ": -4.12, "a": 6378137, "e2": 0.00669437999},
    "WGS-84": {"dX": -205.56, "dY": +168.77, "dZ": -4.12, "a": 6378137, "e2": 0.00669437999},
    "SAD-69": {"dX": -138.70, "dY": +164.40, "dZ": +34.40, "a": 6378160, "e2": 0.00669454185},
    "Córrego Alegre": {"dX": 0, "dY": 0, "dZ": 0, "a": 6378388, "e2": 0.00672267}
}
