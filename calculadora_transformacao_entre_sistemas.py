import streamlit as st
import sistemasbrasileiros as sis
import  sistemas_cartesianos_geodesicos as sis_cart


## Calculadora de Conversão de Sistemas
st.markdown('## Calculadora de Conversão de Sistemas')

tipo_calculo = st.selectbox('Escolha qual sistema você deseja realizar a conversão', ('Selecione','Cartesiano -> Geodésico', 'Geodésico -> Cartesiano'))

match tipo_calculo:
    case 'Cartesiano -> Geodésico':
            
            # Qual o atual sistema da coordenada? OBS: SAD=1 WGS 84 EPSG:4326=2 SIRGAS 2000 EPSG:4674=3 CORREGO ALEGRE EPSG:4225=4: 
            sis_value_text = st.selectbox('Qual o atual sistema da coordenada?', ('Selecione','SAD 1969 EPSG:4618','WGS 84 EPSG:4326','SIRGAS 2000 EPSG:4674','CORREGO ALEGRE EPSG:4225'))

            if sis_value_text != 'Selecione':

                # Para Qual sistema? OBS: SAD=1 WGS 84 EPSG:4326=2 SIRGAS 2000 EPSG:4674=3 CORREGO ALEGRE EPSG:4225=4: 
                sis2_value_text = st.selectbox("Para qual sistema deseja converter?", ('Selecione','SAD 1969 EPSG:4618','WGS 84 EPSG:4326','SIRGAS 2000 EPSG:4674','CORREGO ALEGRE EPSG:4225'))

                if sis2_value_text != 'Selecione':

                    X = float(st.number_input("insira a Coordenada X: ", format="%0.9f"))
                    Y = float(st.number_input("insira a Coordenada Y: ", format="%0.9f"))
                    Z = float(st.number_input("insira a Coordenada Z: ", format="%0.9f"))

                    botao_cart_to_geodetic = st.button('Converter')

                    if botao_cart_to_geodetic:

                        match (sis_value_text,sis2_value_text):
                            # Partindo de SAD-69 para outro Sistema
                            case ('SAD 1969 EPSG:4618','SAD 1969 EPSG:4618'):
                                lat_dms, lon_dms, h = sis_cart.paraSAD_69(X, Y, Z)
                                st.markdown('## Resultado')
                                st.markdown("#### Latitude: {}° {}' {:.10f}''".format(lat_dms[0], lat_dms[1], lat_dms[2])+'\n'+
                                            "#### Longitude: {}° {}' {:.10f}''".format(lon_dms[0], lon_dms[1], lon_dms[2])+'\n'+
                                            "#### Altura: {:.4f} m".format(h))
                            case ('SAD 1969 EPSG:4618','WGS 84 EPSG:4326'):
                                lat_dms, lon_dms, h = sis_cart.paraWGS84(X-66.86,Y+4.37,Z-38.52)
                                st.markdown('## Resultado')
                                st.markdown("#### Latitude: {}° {}' {:.10f}''".format(lat_dms[0], lat_dms[1], lat_dms[2])+'\n'+
                                            "#### Longitude: {}° {}' {:.10f}''".format(lon_dms[0], lon_dms[1], lon_dms[2])+'\n'+
                                            "#### Altura: {:.4f} m".format(h))
                            case ('SAD 1969 EPSG:4618','SIRGAS 2000 EPSG:4674'):
                                lat_dms, lon_dms, h = sis_cart.paraSIRGAS(X-66.86,Y+4.37,Z-38.52)
                                st.markdown('## Resultado')
                                st.markdown("#### Latitude: {}° {}' {:.10f}''".format(lat_dms[0], lat_dms[1], lat_dms[2])+'\n'+
                                            "#### Longitude: {}° {}' {:.10f}''".format(lon_dms[0], lon_dms[1], lon_dms[2])+'\n'+
                                            "#### Altura: {:.4f} m".format(h))
                            case ('SAD 1969 EPSG:4618','CORREGO ALEGRE EPSG:4225'):
                                lat_dms, lon_dms, h = sis_cart.paraCORREGO(X+138.70,Y-164.40,Z-34.40)
                                st.markdown('## Resultado')
                                st.markdown("#### Latitude: {}° {}' {:.10f}''".format(lat_dms[0], lat_dms[1], lat_dms[2])+'\n'+
                                            "#### Longitude: {}° {}' {:.10f}''".format(lon_dms[0], lon_dms[1], lon_dms[2])+'\n'+
                                            "#### Altura: {:.4f} m".format(h))
                            # Partindo de WGS-84 para outro Sistema
                            case ('WGS 84 EPSG:4326','SAD 1969 EPSG:4618'):
                                # De WGS84 para SAD-69: soma-se 66.86 no X, subtrai-se 4.37 no Y e soma-se 38.52 no Z
                                lat_dms, lon_dms, h = sis_cart.paraSAD_69(X + 66.86, Y - 4.37, Z + 38.52)
                                st.markdown('## Resultado')
                                st.markdown("#### Latitude: {}° {}' {:.10f}''".format(lat_dms[0], lat_dms[1], lat_dms[2]) + '\n' +
                                            "#### Longitude: {}° {}' {:.10f}''".format(lon_dms[0], lon_dms[1], lon_dms[2]) + '\n' +
                                            "#### Altura: {:.4f} m".format(h))
                            case ('WGS 84 EPSG:4326','WGS 84 EPSG:4326'):
                                # De WGS84 para WGS84
                                lat_dms, lon_dms, h = sis_cart.paraWGS84(X, Y, Z)
                                st.markdown('## Resultado')
                                st.markdown("#### Latitude: {}° {}' {:.10f}''".format(lat_dms[0], lat_dms[1], lat_dms[2]) + '\n' +
                                            "#### Longitude: {}° {}' {:.10f}''".format(lon_dms[0], lon_dms[1], lon_dms[2]) + '\n' +
                                            "#### Altura: {:.4f} m".format(h))
                            case ('WGS 84 EPSG:4326','SIRGAS 2000 EPSG:4674'):
                                # Como WGS84 e SIRGAS são equivalentes (a transformação encadeada resultaria em identidade), não há alteração.
                                lat_dms, lon_dms, h = sis_cart.paraSIRGAS(X, Y, Z)
                                st.markdown('## Resultado')
                                st.markdown("#### Latitude: {}° {}' {:.10f}''".format(lat_dms[0], lat_dms[1], lat_dms[2]) + '\n' +
                                            "#### Longitude: {}° {}' {:.10f}''".format(lon_dms[0], lon_dms[1], lon_dms[2]) + '\n' +
                                            "#### Altura: {:.4f} m".format(h))
                            case ('WGS 84 EPSG:4326','CORREGO ALEGRE EPSG:4225'):
                                # A transformação é encadeada: WGS84 -> SAD-69 (X+66.86, Y-4.37, Z+38.52) e SAD-69 -> Corrego Alegre (X+138.70, Y-164.40, Z-34.40)
                                # Resultado final: X +205.56, Y -168.77, Z +4.12
                                lat_dms, lon_dms, h = sis_cart.paraCORREGO(X + 205.56, Y - 168.77, Z + 4.12)
                                st.markdown('## Resultado')
                                st.markdown("#### Latitude: {}° {}' {:.10f}''".format(lat_dms[0], lat_dms[1], lat_dms[2]) + '\n' +
                                            "#### Longitude: {}° {}' {:.10f}''".format(lon_dms[0], lon_dms[1], lon_dms[2]) + '\n' +
                                            "#### Altura: {:.4f} m".format(h))
                            # Partindo de SIRGAS para outro Sistema
                            case ('SIRGAS 2000 EPSG:4674','SAD 1969 EPSG:4618'):
                                # De SIRGAS para SAD-69: a regra é igual à de WGS84 para SAD-69, ou seja, soma-se 66.86 no X, subtrai-se 4.37 no Y e soma-se 38.52 no Z
                                lat_dms, lon_dms, h = sis_cart.paraSAD_69(X + 66.86, Y - 4.37, Z + 38.52)
                                st.markdown('## Resultado')
                                st.markdown("#### Latitude: {}° {}' {:.10f}''".format(lat_dms[0], lat_dms[1], lat_dms[2]) + '\n' +
                                            "#### Longitude: {}° {}' {:.10f}''".format(lon_dms[0], lon_dms[1], lon_dms[2]) + '\n' +
                                            "#### Altura: {:.4f} m".format(h))
                            case ('SIRGAS 2000 EPSG:4674','WGS 84 EPSG:4326'):
                                # Encadeamento: SIRGAS -> SAD-69 (X+66.86, Y-4.37, Z+38.52) e depois SAD-69 -> WGS84 (X-66.86, Y+4.37, Z-38.52) resulta na identidade
                                lat_dms, lon_dms, h = sis_cart.paraWGS84(X, Y, Z)
                                st.markdown('## Resultado')
                                st.markdown("#### Latitude: {}° {}' {:.10f}''".format(lat_dms[0], lat_dms[1], lat_dms[2]) + '\n' +
                                            "#### Longitude: {}° {}' {:.10f}''".format(lon_dms[0], lon_dms[1], lon_dms[2]) + '\n' +
                                            "#### Altura: {:.4f} m".format(h))
                            case ('SIRGAS 2000 EPSG:4674','SIRGAS 2000 EPSG:4674'):
                                # Encadeamento: SIRGAS -> SIRGAS
                                lat_dms, lon_dms, h = sis_cart.paraSIRGAS(X, Y, Z)
                                st.markdown('## Resultado')
                                st.markdown("#### Latitude: {}° {}' {:.10f}''".format(lat_dms[0], lat_dms[1], lat_dms[2]) + '\n' +
                                            "#### Longitude: {}° {}' {:.10f}''".format(lon_dms[0], lon_dms[1], lon_dms[2]) + '\n' +
                                            "#### Altura: {:.4f} m".format(h))
                            case ('SIRGAS 2000 EPSG:4674','CORREGO ALEGRE EPSG:4225'):
                                # Encadeamento: SIRGAS -> SAD-69 e SAD-69 -> Corrego Alegre, resultando em:
                                # X +66.86+138.70 = X +205.56, Y -4.37-164.40 = Y -168.77, Z +38.52-34.40 = Z +4.12
                                lat_dms, lon_dms, h = sis_cart.paraCORREGO(X + 205.56, Y - 168.77, Z + 4.12)
                                st.markdown('## Resultado')
                                st.markdown("#### Latitude: {}° {}' {:.10f}''".format(lat_dms[0], lat_dms[1], lat_dms[2]) + '\n' +
                                            "#### Longitude: {}° {}' {:.10f}''".format(lon_dms[0], lon_dms[1], lon_dms[2]) + '\n' +
                                            "#### Altura: {:.4f} m".format(h))
                            # Partindo de Corrego Alegre para outro Sistema
                            case ('CORREGO ALEGRE EPSG:4225','SAD 1969 EPSG:4618'):
                                # Inverso de SAD-69 para Corrego Alegre: subtrai-se 138.70 no X, soma-se 164.40 no Y e soma-se 34.40 no Z
                                lat_dms, lon_dms, h = sis_cart.paraSAD_69(X - 138.70, Y + 164.40, Z + 34.40)
                                st.markdown('## Resultado')
                                st.markdown("#### Latitude: {}° {}' {:.10f}''".format(lat_dms[0], lat_dms[1], lat_dms[2]) + '\n' +
                                            "#### Longitude: {}° {}' {:.10f}''".format(lon_dms[0], lon_dms[1], lon_dms[2]) + '\n' +
                                            "#### Altura: {:.4f} m".format(h))
                            case ('CORREGO ALEGRE EPSG:4225','WGS 84 EPSG:4326'):
                                # Encadeamento: Corrego Alegre -> SAD-69 (inverso de SAD->Corrego: X-138.70, Y+164.40, Z+34.40)
                                # e SAD-69 -> WGS84 (X-66.86, Y+4.37, Z-38.52):
                                # Total: X - (138.70+66.86) = X -205.56, Y + (164.40+4.37) = Y +168.77, Z + (34.40-38.52) = Z -4.12
                                lat_dms, lon_dms, h = sis_cart.paraWGS84(X - 205.56, Y + 168.77, Z - 4.12)
                                st.markdown('## Resultado')
                                st.markdown("#### Latitude: {}° {}' {:.10f}''".format(lat_dms[0], lat_dms[1], lat_dms[2]) + '\n' +
                                            "#### Longitude: {}° {}' {:.10f}''".format(lon_dms[0], lon_dms[1], lon_dms[2]) + '\n' +
                                            "#### Altura: {:.4f} m".format(h))
                            case ('CORREGO ALEGRE EPSG:4225','SIRGAS 2000 EPSG:4674'):
                                # Encadeamento: Corrego Alegre -> SAD-69 e SAD-69 -> SIRGAS resulta em:
                                # X -205.56, Y +168.77, Z -4.12
                                lat_dms, lon_dms, h = sis_cart.paraSIRGAS(X - 205.56, Y + 168.77, Z - 4.12)
                                st.markdown('## Resultado')
                                st.markdown("#### Latitude: {}° {}' {:.10f}''".format(lat_dms[0], lat_dms[1], lat_dms[2]) + '\n' +
                                            "#### Longitude: {}° {}' {:.10f}''".format(lon_dms[0], lon_dms[1], lon_dms[2]) + '\n' +
                                            "#### Altura: {:.4f} m".format(h))
                            case ('CORREGO ALEGRE EPSG:4225','CORREGO ALEGRE EPSG:4225'):
                                # Encadeamento: Corrego Alegre -> Corrego Alegre
                                lat_dms, lon_dms, h = sis_cart.paraCORREGO(X, Y, Z)
                                st.markdown('## Resultado')
                                st.markdown("#### Latitude: {}° {}' {:.10f}''".format(lat_dms[0], lat_dms[1], lat_dms[2]) + '\n' +
                                            "#### Longitude: {}° {}' {:.10f}''".format(lon_dms[0], lon_dms[1], lon_dms[2]) + '\n' +
                                            "#### Altura: {:.4f} m".format(h))

    case 'Geodésico -> Cartesiano':
        # Qual o atual sistema da coordenada? OBS: SAD=1 WGS 84 EPSG:4326=2 SIRGAS 2000 EPSG:4674=3 CORREGO ALEGRE EPSG:4225=4: 
        sis_value_text = st.selectbox('Qual o atual sistema da coordenada?', ('Selecione','SAD 1969 EPSG:4618','WGS 84 EPSG:4326','SIRGAS 2000 EPSG:4674','CORREGO ALEGRE EPSG:4225'))

        if sis_value_text != 'Selecione':

            st.markdown('## Latitude')

            g1 = int(st.number_input("insira o grau da latitude: "))
            m1 = int(st.number_input("insira os minutos da latitude: "))
            s1 = float(st.number_input("insira os segundos da latitude: ", format="%0.5f"))

            st.markdown('## Longitude')

            g2 = int(st.number_input("insira o grau da longitude: "))
            m2 = int(st.number_input("insira os minutos da longitude: "))
            s2 = float(st.number_input("insira os segundos da longitude: ", format="%0.5f"))

            st.markdown('## Altura')
            h = float(st.number_input("Altura em metros: ", format="%0.3f"))

            if g1 and g2 and m1 and m2 and s1 and s2:

                lat = sis.gmsdecimal(g1, m1, s1)
                lon = sis.gmsdecimal(g2, m2, s2)

                X = Y = Z = X1 = Y1 = Z1 = X2 = Y2 = Z2 = 0.000000
                lat1 = lon1 = h1 = 0.000000   

                # Para Qual sistema? OBS: SAD=1 WGS 84 EPSG:4326=2 SIRGAS 2000 EPSG:4674=3 CORREGO ALEGRE EPSG:4225=4: 
                sis2_value_text = st.selectbox("Para qual sistema deseja converter?", ('SAD 1969 EPSG:4618','WGS 84 EPSG:4326','SIRGAS 2000 EPSG:4674','CORREGO ALEGRE EPSG:4225'))

                # Usando match case para atribuir valores a sis e sis2
                match sis_value_text:
                    case 'SAD 1969 EPSG:4618':
                        sistema = 1
                    case 'WGS 84 EPSG:4326':
                        sistema = 2
                    case 'SIRGAS 2000 EPSG:4674':
                        sistema = 3
                    case 'CORREGO ALEGRE EPSG:4225':
                        sistema = 4

                match sis2_value_text:
                    case 'SAD 1969 EPSG:4618':
                        sistema2 = 1
                    case 'WGS 84 EPSG:4326':
                        sistema2 = 2
                    case 'SIRGAS 2000 EPSG:4674':
                        sistema2 = 3
                    case 'CORREGO ALEGRE EPSG:4225':
                        sistema2 = 4
            
                botao = st.button('Converter')
                if botao:
                    if sistema == 1 and sistema2 == 1:
                        valor = sis.SAD_69(lon, lat, h)
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(valor[0])+'\n'+'#### Y: '+str(valor[1])+'\n'+'#### Z: '+str(valor[2]))

                    if sistema == 1 and sistema2 == 2:
                        result = sis.SAD_69(lon, lat, h)
                        X1 = result[0] - 66.86
                        Y1 = result[1] + 4.37
                        Z1 = result[2] - 38.52
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(X1)+'\n'+'#### Y: '+str(Y1)+'\n'+'#### Z: '+str(Z1))

                    if sistema == 1 and sistema2 == 3:
                        result = sis.SAD_69(lon, lat, h)
                        X1 = result[0] - 66.86
                        Y1 = result[1] + 4.37
                        Z1 = result[2] - 38.52
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(X1)+'\n'+'#### Y: '+str(Y1)+'\n'+'#### Z: '+str(Z1))

                    if sistema == 1 and sistema2 == 4:
                        result = sis.SAD_69(lon, lat, h)
                        X1 = result[0] + 138.70
                        Y1 = result[1] - 164.40
                        Z1 = result[2] - 34.40
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(X1)+'\n'+'#### Y: '+str(Y1)+'\n'+'#### Z: '+str(Z1))
                        
                    if sistema == 2 and sistema2 == 1: 
                        result = sis.WGS84(lon, lat, h)
                        X1 = result[0] - 66.86
                        Y1 = result[1] + 4.37
                        Z1 = result[2] - 38.52
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(X1)+'\n'+'#### Y: '+str(Y1)+'\n'+'#### Z: '+str(Z1))

                    if sistema == 2 and sistema2 == 2:
                        valor = sis.WGS84(lon, lat, h)
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(valor[0])+'\n'+'#### Y: '+str(valor[1])+'\n'+'#### Z: '+str(valor[2]))

                    if sistema == 2 and sistema2 == 3: # De WGS para SAD-69 cancela com a operação de SAD-69 para SIRGAS
                        result = sis.WGS84(lon, lat, h)
                        X1 = result[0] 
                        Y1 = result[1] 
                        Z1 = result[2] 
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(X1)+'\n'+'#### Y: '+str(Y1)+'\n'+'#### Z: '+str(Z1))
                        
                    if sistema == 2 and sistema2 == 4:
                        result = sis.WGS84(lon, lat, h)
                        X1 = result[0] + 66.86 + 138.70
                        Y1 = result[1] - 4.37 - 164.40
                        Z1 = result[2] + 38.52 - 34.40
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(X1)+'\n'+'#### Y: '+str(Y1)+'\n'+'#### Z: '+str(Z1))

                    if sistema == 3 and sistema2 == 1:
                        result = sis.SIRGAS(lon, lat, h)
                        X1 = result[0] + 66.86
                        Y1 = result[1] - 4.37
                        Z1 = result[2] + 38.52
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(X1)+'\n'+'#### Y: '+str(Y1)+'\n'+'#### Z: '+str(Z1))
                        
                    if sistema == 3 and sistema2 == 2:
                        result = sis.SIRGAS(lon, lat, h)
                        X1 = result[0]
                        Y1 = result[1]
                        Z1 = result[2]
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(X1)+'\n'+'#### Y: '+str(Y1)+'\n'+'#### Z: '+str(Z1))
                        
                    if sistema == 3 and sistema2 == 3:
                        valor = sis.SIRGAS(lon, lat, h)
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(valor[0])+'\n'+'#### Y: '+str(valor[1])+'\n'+'#### Z: '+str(valor[2]))

                    if sistema == 3 and sistema2 == 4:
                        result = sis.SIRGAS(lon, lat, h)
                        X1 = result[0] + 66.86 + 138.70
                        Y1 = result[1] - 4.37 - 164.40
                        Z1 = result[2] + 38.52 - 34.40
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(X1)+'\n'+'#### Y: '+str(Y1)+'\n'+'#### Z: '+str(Z1))
                        
                    if sistema == 4 and sistema2 == 1:
                        result = sis.CORREGO(lon, lat, h)
                        X1 = result[0] - 138.70 
                        Y1 = result[1] + 164.40
                        Z1 = result[2] + 34.40
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(X1)+'\n'+'#### Y: '+str(Y1)+'\n'+'#### Z: '+str(Z1))

                    if sistema == 4 and sistema2 == 2:
                        result = sis.CORREGO(lon, lat, h)
                        X1 = result[0] - 138.70 -66.86
                        Y1 = result[1] + 164.40 + 4.37
                        Z1 = result[2] + 34.40 - 38.52
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(X1)+'\n'+'#### Y: '+str(Y1)+'\n'+'#### Z: '+str(Z1))

                    if sistema == 4 and sistema2 == 3:
                        result = sis.CORREGO(lon, lat, h)
                        X1 = result[0] - 138.70 -66.86
                        Y1 = result[1] + 164.40 + 4.37
                        Z1 = result[2] + 34.40 - 38.52
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(X1)+'\n'+'#### Y: '+str(Y1)+'\n'+'#### Z: '+str(Z1))

                    if sistema == 4 and sistema2 == 4:
                        valor = sis.CORREGO(lon, lat, h)
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(valor[0])+'\n'+'#### Y: '+str(valor[1])+'\n'+'#### Z: '+str(valor[2]))
