import math

def decimal_to_dms(angle):
    """
    Converte um ângulo em graus (formato decimal) para uma tupla (graus, minutos, segundos).
    Os segundos são retornados com todas as casas decimais.
    """
    # A parte inteira dos graus (pode ser negativa)
    degrees_int = int(angle)
    # Cálculo dos minutos (parte inteira dos minutos a partir do valor absoluto do resto)
    remainder = abs(angle - degrees_int) * 60
    minutes = int(remainder)
    # O restante convertido para segundos (com todas as casas decimais)
    seconds = (remainder - minutes) * 60
    return (degrees_int, minutes, seconds)

def cart_to_geodetic(X, Y, Z, a, f):
    """
    Converte coordenadas cartesianas (X, Y, Z) para geodésicas.
    
    Parâmetros:
      X, Y, Z : Coordenadas cartesianas (em metros)
      a       : Semi-eixo maior do elipsoide
      f       : Achatamento (valor numérico ou 1/valor)
    
    Retorna:
      (lat_dms, lon_dms, h) em que:
        lat_dms: tupla (graus, minutos, segundos) para a latitude;
        lon_dms: tupla (graus, minutos, segundos) para a longitude;
        h: altura em metros.
    """
    # Cálculos do elipsoide
    b = a * (1 - f)
    c = math.sqrt(a**2 - b**2)
    e_quadrado = (a**2 - b**2)/a**2      # parâmetros auxiliares:
    el_quadrado = e_quadrado/(1-e_quadrado)

    # Projeção no plano XY
    p = math.sqrt(X**2 + Y**2)
    
    # Cálculo intermediário do teta
    theta = math.atan((Z * a) / (p * b))
    
    # Latitude em radianos
    lat_rad = math.atan((Z + (el_quadrado) * b * math.sin(theta)**3) /
                        (p - (e_quadrado) * a * math.cos(theta)**3))
    
    # Longitude em radianos (usa atan2 para o quadrante correto)
    lon_rad = math.atan2(Y, X)
    
    # Raio de curvatura da vertical
    N = a / math.sqrt(1 - ((e_quadrado) * (math.sin(lat_rad)**2)))
    
    # Altura em relação ao elipsoide
    h = p / math.cos(lat_rad) - N

    # Conversão para graus decimais
    lat_deg = math.degrees(lat_rad)
    lon_deg = math.degrees(lon_rad)
    
    # Conversão para formato graus, minutos e segundos
    lat_dms = decimal_to_dms(lat_deg)
    lon_dms = decimal_to_dms(lon_deg)
    
    return lat_dms, lon_dms, h

def paraSAD_69(X, Y, Z):
    a = 6378160.0            # Semi-eixo maior para SAD-69
    f = 1 / 298.25           # Achatamento para SAD-69
    return cart_to_geodetic(X, Y, Z, a, f)

def paraWGS84(X, Y, Z):
    a = 6378137.0            # Semi-eixo maior para WGS84
    f = 0.00335281066        # Achatamento para WGS84
    return cart_to_geodetic(X, Y, Z, a, f)

def paraSIRGAS(X, Y, Z):
    a = 6378137.0            # Semi-eixo maior para SIRGAS
    f = 0.00335281068        # Achatamento para SIRGAS
    return cart_to_geodetic(X, Y, Z, a, f)

def paraCORREGO(X, Y, Z):
    a = 6378388.0            # Semi-eixo maior para CORREGO ALEGRE
    f = 0.00336700337        # Achatamento para CORREGO ALEGRE
    return cart_to_geodetic(X, Y, Z, a, f)
