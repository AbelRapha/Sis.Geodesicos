import math
from molodensky import gms_para_decimal

def calcular_p(lon_rad, lon0_rad):
    """
    Calcula o valor de 'p' a partir da diferença entre a longitude local
    e a longitude do meridiano central, ambas em radianos.

    Args:
        lon_rad (float): Longitude local em radianos.
        lon0_rad (float): Longitude do meridiano central (LMC) em radianos.

    Returns:
        float: O valor de 'p'.
    """

    # Passo 1: Calcular a diferença angular em radianos
    delta_lon_rad = lon_rad - lon0_rad

    # Passo 2: Converter a diferença angular de graus para segundos de arco
    # 1 grau = 3600 segundos de arco
    delta_lon_segundos_arco = delta_lon_rad * 3600

    # Passo 4: Aplicar a fórmula para calcular 'p'
    # A fórmula original é p = 0,0001 * delta_delta_segundos_arco
    # Assumindo que delta_delta_segundos_arco é a nossa delta_lon_segundos_arco
    p = 0.0001 * delta_lon_segundos_arco

    return p

def geodetica_para_utm_manual(lat, lon, elipsoide='WGS84'):
    """
    Converte coordenadas geodésicas para UTM sem uso de bibliotecas externas.
    Suporte atual: WGS84, SIRGAS 2000, SAD-69, CORREGO ALEGRE
    """
    # Parâmetros dos elipsoides
    parametros = {
        'WGS84':        {'a': 6378137.0,     'f': 1 / 298.257223563},
        'SIRGAS 2000':  {'a': 6378137.0,     'f': 1 / 298.257222101},
        'SAD-69':       {'a': 6378160.0,     'f': 1 / 298.25},
        'CORREGO ALEGRE': {'a': 6378388.0,   'f': 1 / 297.0},
        'GRS80' :         {'a': 6378137.0, 'f': 1/298.257222101 }
    }

    if elipsoide not in parametros:
        raise ValueError("Elipsoide inválido.")

    a = parametros[elipsoide]['a']
    f = parametros[elipsoide]['f']
    b = a*(1-f)
    e2 = 2 * f - f ** 2  # excentricidade ao quadrado
    e = math.sqrt(e2) # excentricidade
    el = math.sqrt(a**2 - b**2)/b # e'

    # Conversão de str para dms
    ## Latitude
    g, m, s = map(float, lat.split())
    lat_rad = gms_para_decimal(g, m, s)
    
    ## Longitude
    g, m, s = map(float, lon.split())
    lon_rad = gms_para_decimal(g, m, s)

    # Cálculo do Meridiano
    lon0_rad = 6 * round(lon_rad/6) + 3  # Meridiano central
 
    # Cálculo do P
    p = calcular_p(lon_rad,lon0_rad)

    # Conversão para radianos
    lon_rad = math.radians(lon_rad)
    lat_rad = math.radians(lat_rad)

    N = a / math.sqrt(1 - e**2 * math.sin(lat_rad)**2)
    M = a* (1 - e2) / math.sqrt((1 - e2 * math.sin(lat_rad) ** 2)**3)
    #Geodesica para UTM (Prametros)
    K0 = 0.9996
    pll= 206264.8062 #segundos(em GMS) 
    A = 1+((3/4)*(e**2)) +((45/64)*(e**4))+((175/256)*(e**6))+((11025/16384)*(e**8))+((43659/65536)*(e**10))
    B = ((3/4)*(e**2))+((15/16)*(e**4))+((525/512)*(e**6))+((2205/2048)*(e**8))+((72765/65536)*(e**10))
    C = ((15/64)*(e**4))+((105/256)*(e**6))+((2205/4096)*(e**8))+((10395/16384)*(e**10))
    D = ((35/512)*(e**6))+((315/2048)*(e**8))+((31185/131072)*(e**10))
    E = ((315/16384)*(e**8))+((3465/65536)*(e**10))
    F = ((639/131072)*(e**10))
    S = (a * (1 - (e**2))) * (((A * lat_rad) - ((B/2) * math.sin(2 * lat_rad)) + ((C/4) * math.sin(4 * lat_rad)) - ((D/6) * math.sin(6 * lat_rad)) + ((E/8) * math.sin(8 * lat_rad)) - ((F/10) * math.sin(10 * lat_rad))))
    I = K0*S
    II = ((N*math.sin(lat_rad)*math.cos(lat_rad)*K0*(10**8))/(2*(pll**2)))
    III = ((N*math.sin(lat_rad)*((math.cos(lat_rad))**3))/(24*(pll**4)))*(5-(math.tan(lat_rad)**2)+(9*(el**2)*(math.cos(lat_rad)**2))+(4*(el**4)*(math.cos(lat_rad)**4)))*(K0*(10**16))
    IV = ((N*math.cos(lat_rad)*K0*(10**4))/(pll))
    V = ((N*((math.cos(lat_rad))**3))/(6*(pll**3)))*(1-(math.tan(lat_rad)**2)+((e**2)*(math.cos(lat_rad)**2)))*(K0*(10**12))
    A6 = ((N*math.sin(lat_rad)*(math.cos(lat_rad)**5))/(720*(pll**6)))*(61-(58*(math.tan(lat_rad)**2))+(math.tan(lat_rad)**4)+(270*(el**2)*(math.cos(lat_rad)**2))-(330*(el**2)*(math.sin(lat_rad)**2)))*(K0*(10**24))
    B5 = ((N*(math.cos(lat_rad)**5))/(120*(pll**5)))*(5-(18*(math.tan(lat_rad)**2))+(math.tan(lat_rad)**4)+(14*(el**2)*(math.cos(lat_rad)**2))-(58*(el**2)*(math.sin(lat_rad)**2)))*(K0*(10**20))

    easting = IV*p + V*p**3 + B5*p**5
    northing = I + II*p**2 + III*p**4 + A6*p**6

    if lat_rad < 0:
        northing += 10000000.0  # hemisfério sul
    easting += 500000

    return easting, northing, 'S' if lat_rad < 0 else 'N'