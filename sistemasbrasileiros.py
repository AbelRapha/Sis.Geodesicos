import math

# para usuario colocar grau, minuto, segundo e fazer direto a conversao
def gmsdecimal(g, m, s):
    if g > 0:
        decimal = math.radians(g + (m / 60) + (s / 3600))

    if g < 0:
        decimal = math.radians(g - (m / 60) - (s / 3600))

    return decimal

# para cada sistema/elipsoide tem: Semi-eixo maior(a), Achatamento(f)
def SAD_69(lon, lat, h):
    a = 6378160.0
    f = 0.0033528918692372
    b = (a * (1 - f))
    c = math.sqrt((a ** 2) - (b ** 2))
    e = c / a
    el = c / b
    N = (a) / math.sqrt(1 - ((e ** 2) * ((math.sin(lat)) ** 2)))
    p = (h + N) * math.cos(lat)
    X = (p) * math.cos(lon)
    Y = (p) * math.sin(lon)
    Z = ((N * (1 - (e * e))) + h) * (math.sin(lat))
    #print(" X: ", X, "\n Y: ", Y, "\n Z: ", Z)
    return (X, Y, Z)

def WGS84(lon, lat, h):
    a = 6378137.0
    f = 0.0033528106647475
    b = (a * (1 - f))
    c = math.sqrt((a ** 2) - (b ** 2))
    e = c / a
    el = c / b
    N = (a) / math.sqrt(1 - ((e ** 2) * ((math.sin(lat)) ** 2)))
    p = (h + N) * math.cos(lat)
    X = (p) * math.cos(lon)
    Y = (p) * math.sin(lon)
    Z = ((N * (1 - (e * e))) + h) * (math.sin(lat))
    #print(" X: ", X, "\n Y: ", Y, "\n Z: ", Z)
    return (X, Y, Z)

def SIRGAS(lon, lat, h):
    a = 6378137.0
    f = 0.0033528106811823
    b = (a * (1 - f))
    c = math.sqrt((a ** 2) - (b ** 2))
    e = c / a
    el = c / b
    N = (a) / math.sqrt(1 - ((e ** 2) * ((math.sin(lat)) ** 2)))
    p = (h + N) * math.cos(lat)
    X = (p) * math.cos(lon)
    Y = (p) * math.sin(lon)
    Z = ((N * (1 - (e * e))) + h) * (math.sin(lat))
    #print(" X: ", X, "\n Y: ", Y, "\n Z: ", Z)
    return(X, Y, Z)

def CORREGO(lon, lat, h):
    a = 6378388.0
    f = 0.0033670033670034
    b = (a * (1 - f))
    c = math.sqrt((a ** 2) - (b ** 2))
    e = c / a
    el = c / b
    N = (a) / math.sqrt(1 - ((e ** 2) * ((math.sin(lat)) ** 2)))
    p = (h + N) * math.cos(lat)
    X = (p) * math.cos(lon)
    Y = (p) * math.sin(lon)
    Z = ((N * (1 - (e * e))) + h) * (math.sin(lat))
    #print(" X: ", X, "\n Y: ", Y, "\n Z: ", Z)
    return (X, Y, Z)

def paraSAD_69(X, Y, Z):
    a = 6378160.0
    f = 1 / 298.25
    b = (a * (1 - f))
    c = math.sqrt((a * a) - (b * b))
    e = c / a
    el = c / b
    p = math.sqrt((X ** 2) + (Y ** 2))
    theta = math.atan((Z / p) * (a / b))
    senotheta = math.sin(theta)
    cossenotheta = math.cos(theta)
    lat1 = math.degrees(math.atan((Z + ((el ** 2) * b * (senotheta ** 3))) / (p - ( (e ** 2) * a * (cossenotheta ** 3)))))
    lon1 = math.degrees(math.atan(Y / X))
    N = ((a) / math.sqrt(1 - ((e ** 2) * ((math.sin(lat1) ** 2)))))
    h1 = (p / (math.cos(math.radians(lat1)))) - N
    glat1 = int(lat1) # lat =40.123456, glat=40
    minlat1 = int((lat1 - (glat1)) * 60)  # (40.123456-40) * 60 = 0.123456 * 60 = 7.40736, minlat = 7
    seglat1 = ((((lat1 - glat1) * 60) - minlat1) * 60) # (((40.123456 - 40) * 60 ) - 7) * 60))  = 
    glon1 = int(lon1)
    minlon1 = int((lon1 - (glon1)) * 60)
    seglon1 = ((((lon1 - glon1) * 60) - minlon1) * 60)
    
    #print("Latitude: ", glat1,"° ", abs(minlat1), "' ", abs(seglat1),"'' ",  " \nLongitude: ", glon1,"° ", abs(minlon1), "' ", abs(seglon1),"'' ", "\nAltura: ", h1)
    return (lat1, lon1, h1)
    
def paraWGS84(X, Y, Z):
    a = 6378137.0
    f = 0.00335281066
    b = (a * (1 - f))
    c = math.sqrt((a * a) - (b * b))
    e = c / a
    el = c / b
    p = math.sqrt((X ** 2) + (Y ** 2))
    theta = math.atan((Z / p) * (a / b))
    senotheta = math.sin(theta)
    cossenotheta = math.cos(theta)
    lat1 = math.degrees(math.atan((Z + ((el ** 2) * b * (senotheta ** 3))) / (p - ( (e ** 2) * a * (cossenotheta ** 3)))))
    lon1 = math.degrees(math.atan(Y / X))
    N = ((a) / math.sqrt(1 - ((e ** 2) * ((math.sin(lat1) ** 2)))))
    h1 = (p / (math.cos(math.radians(lat1)))) - N
    glat1 = int(lat1) # lat =40.123456, glat=40
    minlat1 = int((lat1 - (glat1)) * 60)  # (40.123456-40) * 60 = 0.123456 * 60 = 7.40736, minlat = 7
    seglat1 = ((((lat1 - glat1) * 60) - minlat1) * 60) # (((40.123456 - 40) * 60 ) - 7) * 60))  = 
    glon1 = int(lon1)
    minlon1 = int((lon1 - (glon1)) * 60)
    seglon1 = ((((lon1 - glon1) * 60) - minlon1) * 60)
    
    #print("Latitude: ", glat1,"° ", abs(minlat1), "' ", abs(seglat1),"'' ",  " \nLongitude: ", glon1,"° ", abs(minlon1), "' ", abs(seglon1),"'' ", "\nAltura: ", h1)
    return (lat1, lon1, h1)

def paraSIRGAS(X, Y, Z):
    a = 6378137.0
    f = 0.00335281068
    b = (a * (1 - f))
    c = math.sqrt((a * a) - (b * b))
    e = c / a
    el = c / b
    p = math.sqrt((X ** 2) + (Y ** 2))
    theta = math.atan((Z / p) * (a / b))
    senotheta = math.sin(theta)
    cossenotheta = math.cos(theta)
    lat1 = math.degrees(math.atan((Z + ((el ** 2) * b * (senotheta ** 3))) / (p - ( (e ** 2) * a * (cossenotheta ** 3)))))
    lon1 = math.degrees(math.atan(Y / X))
    N = ((a) / math.sqrt(1 - ((e ** 2) * ((math.sin(lat1) ** 2)))))
    h1 = (p / (math.cos(math.radians(lat1)))) - N
    glat1 = int(lat1) # lat =40.123456, glat=40
    minlat1 = int((lat1 - (glat1)) * 60)  # (40.123456-40) * 60 = 0.123456 * 60 = 7.40736, minlat = 7
    seglat1 = ((((lat1 - glat1) * 60) - minlat1) * 60) # (((40.123456 - 40) * 60 ) - 7) * 60))  = 
    glon1 = int(lon1)
    minlon1 = int((lon1 - (glon1)) * 60)
    seglon1 = ((((lon1 - glon1) * 60) - minlon1) * 60)
    
    #print("Latitude: ", glat1,"° ", abs(minlat1), "' ", abs(seglat1),"'' ",  " \nLongitude: ", glon1,"° ", abs(minlon1), "' ", abs(seglon1),"'' ", "\nAltura: ", h1)
    return (lat1, lon1, h1)

def paraCORREGO(X, Y, Z):
    a = 6378388.0
    f = 0.00336700337
    b = (a * (1 - f))
    c = math.sqrt((a * a) - (b * b))
    e = c / a
    el = c / b
    p = math.sqrt((X ** 2) + (Y ** 2))
    theta = math.atan((Z / p) * (a / b))
    senotheta = math.sin(theta)
    cossenotheta = math.cos(theta)
    lat1 = math.degrees(math.atan((Z + ((el ** 2) * b * (senotheta ** 3))) / (p - ( (e ** 2) * a * (cossenotheta ** 3)))))
    lon1 = math.degrees(math.atan(Y / X))
    N = ((a) / math.sqrt(1 - ((e ** 2) * ((math.sin(lat1) ** 2)))))
    h1 = (p / (math.cos(math.radians(lat1)))) - N
    glat1 = int(lat1) # lat =40.123456, glat=40
    minlat1 = int((lat1 - (glat1)) * 60)  # (40.123456-40) * 60 = 0.123456 * 60 = 7.40736, minlat = 7
    seglat1 = ((((lat1 - glat1) * 60) - minlat1) * 60) # (((40.123456 - 40) * 60 ) - 7) * 60))  = 
    glon1 = int(lon1)
    minlon1 = int((lon1 - (glon1)) * 60)
    seglon1 = ((((lon1 - glon1) * 60) - minlon1) * 60)
    
    #print("Latitude: ", glat1,"° ", abs(minlat1), "' ", abs(seglat1),"'' ",  " \nLongitude: ", glon1,"° ", abs(minlon1), "' ", abs(seglon1),"'' ", "\nAltura: ", h1)
    return (lat1, lon1, h1)
