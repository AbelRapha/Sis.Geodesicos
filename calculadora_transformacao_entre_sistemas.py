import streamlit as st
import sistemasbrasileiros as sis
import  sistemas_cartesianos_geodesicos as sis_cart


## Calculadora de Conversão de Sistemas
st.markdown('## Calculadora de Conversão de Sistemas')

tipo_calculo = st.selectbox('Escolha qual sistema você deseja realizar a conversão', ('Selecione','Cartesiano -> Geodésico', 'Geodésico -> Cartesiano'))

match tipo_calculo:
    case 'Cartesiano -> Geodésico':
            # Para Qual sistema? OBS: SAD=1 WGS=2 SIRGAS=3 Corrego Alegre=4: 
            sis2_value_text = st.selectbox("Para qual sistema deseja converter?", ('Selecione','SAD-69','WGS','SIRGAS','CORREGO ALEGRE'))

            if sis2_value_text != 'Selecione':

                X = float(st.number_input("insira a Coordenada X: ", format="%0.9f"))
                Y = float(st.number_input("insira a Coordenada Y: ", format="%0.9f"))
                Z = float(st.number_input("insira a Coordenada Z: ", format="%0.9f"))

                botao_cart_to_geodetic = st.button('Converter')

                if botao_cart_to_geodetic:

                    match sis2_value_text:
                        case 'SAD-69':
                            lat_dms, lon_dms, h = sis_cart.paraSAD_69(X, Y, Z)
                            st.markdown('## Resultado')
                            st.markdown("#### Latitude: {}° {}' {:.10f}''".format(lat_dms[0], lat_dms[1], lat_dms[2])+'\n'+
                                        "#### Longitude: {}° {}' {:.10f}''".format(lon_dms[0], lon_dms[1], lon_dms[2])+'\n'+
                                        "#### Altura: {:.4f} m".format(h))
                        case 'WGS':
                            lat_dms, lon_dms, h = sis_cart.paraWGS84(X,Y,Z)
                            st.markdown('## Resultado')
                            st.markdown("#### Latitude: {}° {}' {:.10f}''".format(lat_dms[0], lat_dms[1], lat_dms[2])+'\n'+
                                        "#### Longitude: {}° {}' {:.10f}''".format(lon_dms[0], lon_dms[1], lon_dms[2])+'\n'+
                                        "#### Altura: {:.4f} m".format(h))
                        case 'SIRGAS':
                            lat_dms, lon_dms, h = sis_cart.paraSIRGAS(X,Y,Z)
                            st.markdown('## Resultado')
                            st.markdown("#### Latitude: {}° {}' {:.10f}''".format(lat_dms[0], lat_dms[1], lat_dms[2])+'\n'+
                                        "#### Longitude: {}° {}' {:.10f}''".format(lon_dms[0], lon_dms[1], lon_dms[2])+'\n'+
                                        "#### Altura: {:.4f} m".format(h))
                        case 'CORREGO ALEGRE':
                            lat_dms, lon_dms, h = sis_cart.paraCORREGO(X,Y,Z)
                            st.markdown('## Resultado')
                            st.markdown("#### Latitude: {}° {}' {:.10f}''".format(lat_dms[0], lat_dms[1], lat_dms[2])+'\n'+
                                        "#### Longitude: {}° {}' {:.10f}''".format(lon_dms[0], lon_dms[1], lon_dms[2])+'\n'+
                                        "#### Altura: {:.4f} m".format(h))

    case 'Geodésico -> Cartesiano':
        # Qual o atual sistema da coordenada? OBS: SAD=1 WGS=2 SIRGAS=3 Corrego Alegre=4: 
        sis_value_text = st.selectbox('Qual o atual sistema da coordenada?', ('Selecione','SAD-69','WGS','SIRGAS','CORREGO ALEGRE'))

        if sis_value_text != 'Selecione':

            st.markdown('## Latitude')

            g1 = int(st.number_input("insira o grau da latitude: "))
            m1 = int(st.number_input("insira os minutos da latitude: "))
            s1 = float(st.number_input("insira os segundos da latitude: ", format="%0.4f"))

            st.markdown('## Longitude')

            g2 = int(st.number_input("insira o grau da longitude: "))
            m2 = int(st.number_input("insira os minutos da longitude: "))
            s2 = float(st.number_input("insira os segundos da longitude: ", format="%0.4f"))

            st.markdown('## Altura')
            h = float(st.number_input("Altura em metros: ", format="%0.4f"))

            if g1 and g2 and m1 and m2 and s1 and s2:

                lat = sis.gmsdecimal(g1, m1, s1)
                lon = sis.gmsdecimal(g2, m2, s2)

                X = Y = Z = X1 = Y1 = Z1 = X2 = Y2 = Z2 = 0.000000
                lat1 = lon1 = h1 = 0.000000   

                # Para Qual sistema? OBS: SAD=1 WGS=2 SIRGAS=3 Corrego Alegre=4: 
                sis2_value_text = st.selectbox("Para qual sistema deseja converter?", ('SAD-69','WGS','SIRGAS','CORREGO ALEGRE'))

                # Usando match case para atribuir valores a sis e sis2
                match sis_value_text:
                    case 'SAD-69':
                        sistema = 1
                    case 'WGS':
                        sistema = 2
                    case 'SIRGAS':
                        sistema = 3
                    case 'CORREGO ALEGRE':
                        sistema = 4

                match sis2_value_text:
                    case 'SAD-69':
                        sistema2 = 1
                    case 'WGS':
                        sistema2 = 2
                    case 'SIRGAS':
                        sistema2 = 3
                    case 'CORREGO ALEGRE':
                        sistema2 = 4
            
                botao = st.button('Converter')
                if botao:
                    if sistema == 1 and sistema2 == 1:
                        valor = sis.SAD_69(lon, lat, h)
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(valor[0])+'\n'+'#### Y: '+str(valor[1])+'\n'+'#### Z: '+str(valor[2]))

                    if sistema == 1 and sistema2 == 2:
                        result = sis.SAD_69(lon, lat, h)
                        X1 = result[0] - 66.87
                        Y1 = result[1] + 4.37
                        Z1 = result[2] - 38.52
                        valor = sis.paraWGS84(X1, Y1, Z1)
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(valor[0])+'\n'+'#### Y: '+str(valor[1])+'\n'+'#### Z: '+str(valor[2]))

                    if sistema == 1 and sistema2 == 3:
                        result = sis.SAD_69(lon, lat, h)
                        X1 = result[0] - 67.35
                        Y1 = result[1] + 3.88
                        Z1 = result[2] - 38.22
                        valor = sis.paraSIRGAS(X1, Y1, Z1)
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(valor[0])+'\n'+'#### Y: '+str(valor[1])+'\n'+'#### Z: '+str(valor[2]))

                    if sistema == 1 and sistema2 == 4:
                        result = sis.SAD_69(lon, lat, h)
                        X1 = result[0] + 138.70
                        Y1 = result[1] - 164.40
                        Z1 = result[2] - 34.40
                        valor = sis.paraCORREGO(X1, Y1, Z1)
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(valor[0])+'\n'+'#### Y: '+str(valor[1])+'\n'+'#### Z: '+str(valor[2]))

                    if sistema == 2 and sistema2 == 1:
                        result = sis.WGS84(lon, lat, h)
                        X1 = result[0] + 66.87
                        Y1 = result[1] - 4.37
                        Z1 = result[2] + 38.52
                        valor = sis.paraSAD_69(X1, Y1, Z1)
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(valor[0])+'\n'+'#### Y: '+str(valor[1])+'\n'+'#### Z: '+str(valor[2]))

                    if sistema == 2 and sistema2 == 2:
                        valor = sis.WGS84(lon, lat, h)
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(valor[0])+'\n'+'#### Y: '+str(valor[1])+'\n'+'#### Z: '+str(valor[2]))

                    if sistema == 2 and sistema2 == 3:
                        result = sis.WGS84(lon, lat, h)
                        X1 = result[0] + 66.87
                        Y1 = result[1] - 4.37
                        Z1 = result[2] + 38.52
                        result2 = sis.paraSAD_69(X1, Y1, Z1)
                        result1 = sis.SAD_69(result2[0], result2[1], result2[2])
                        X2 = result1[0] - 67.35
                        Y2 = result1[1] + 3.88
                        Z2 = result1[2] - 38.22
                        valor = sis.paraSIRGAS(X2, Y2, Z2)
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(valor[0])+'\n'+'#### Y: '+str(valor[1])+'\n'+'#### Z: '+str(valor[2]))

                    if sistema == 2 and sistema2 == 4:
                        result = sis.WGS84(lon, lat, h)
                        X1 = result[0] + 66.87
                        Y1 = result[0] - 4.37
                        Z1 = result[0] + 38.52
                        result2 = sis.paraSAD_69(X1, Y1, Z1)
                        result1 = sis.SAD_69(result2[0], result2[1], result2[2])
                        X2 = result1[0] + 138.70
                        Y2 = result1[0] - 164.40
                        Z2 = Z - 34.40
                        valor = sis.paraCORREGO(X2, Y2, Z2)
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(valor[0])+'\n'+'#### Y: '+str(valor[1])+'\n'+'#### Z: '+str(valor[2]))

                    if sistema == 3 and sistema2 == 1:
                        result = sis.SIRGAS(lon, lat, h)
                        X1 = result[0] + 67.35
                        Y1 = result[1] - 3.88
                        Z1 = result[2] + 38.22
                        valor = sis.paraSAD_69(X1, Y1, Z1)
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(valor[0])+'\n'+'#### Y: '+str(valor[1])+'\n'+'#### Z: '+str(valor[2]))
                        
                    if sistema == 3 and sistema2 == 2:
                        sis.SIRGAS(lon, lat, h)
                        X1 = result[0] + 67.35
                        Y1 = result[1] - 3.88
                        Z1 = result[2] + 38.22
                        result2 = sis.paraSAD_69(X1, Y1, Z1)
                        result1 = sis.SAD_69(result2[0], result2[1], result2[2])
                        X2 = result1[0] - 66.87
                        Y2 = Y + 4.37
                        Z2 = Z - 38.52
                        valor = sis.paraWGS84(X2, Y2, Z2)
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(valor[0])+'\n'+'#### Y: '+str(valor[1])+'\n'+'#### Z: '+str(valor[2]))

                    if sistema == 3 and sistema2 == 3:
                        valor = sis.SIRGAS(lon, lat, h)
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(valor[0])+'\n'+'#### Y: '+str(valor[1])+'\n'+'#### Z: '+str(valor[2]))

                    if sistema == 3 and sistema2 == 4:
                        sis.SIRGAS(lon, lat, h)
                        X1 = X + 67.35
                        Y1 = Y - 3.88
                        Z1 = Z + 38.22
                        result2 = sis.paraSAD_69(X1, Y1, Z1)
                        result1 = sis.SAD_69(result2[0], result2[1], result2[2])
                        X2 = X + 138.70
                        Y2 = Y - 164.40
                        Z2 = Z - 34.40
                        valor = sis.paraCORREGO(X2, Y2, Z2)
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(valor[0])+'\n'+'#### Y: '+str(valor[1])+'\n'+'#### Z: '+str(valor[2]))

                    if sistema == 4 and sistema2 == 1:
                        sis.CORREGO(lon, lat, h)
                        X1 = X - 138.70
                        Y1 = Y + 164.40
                        Z1 = Z + 34.40
                        valor = sis.paraSAD_69(X1, Y1, Z1)
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(valor[0])+'\n'+'#### Y: '+str(valor[1])+'\n'+'#### Z: '+str(valor[2]))

                    if sistema == 4 and sistema2 == 2:
                        sis.CORREGO(lon, lat, h)
                        X1 = X - 138.70
                        Y1 = Y + 164.40
                        Z1 = Z + 34.40
                        result2 = sis.paraSAD_69(X1, Y1, Z1)
                        result1 = sis.SAD_69(result2[0], result2[1], result2[2])
                        X2 = X - 66.87
                        Y2 = Y + 4.37
                        Z2 = Z - 38.52
                        valor = sis.paraWGS84(X2, Y2, Z2)
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(valor[0])+'\n'+'#### Y: '+str(valor[1])+'\n'+'#### Z: '+str(valor[2]))

                    if sistema == 4 and sistema2 == 3:
                        sis.CORREGO(lon, lat, h)
                        X1 = X - 138.70
                        Y1 = Y + 164.40
                        Z1 = Z + 34.40
                        result2 = sis.paraSAD_69(X1, Y1, Z1)
                        result1 = sis.SAD_69(result2[0], result2[1], result2[2])
                        X2 = X - 67.35
                        Y2 = Y + 3.88
                        Z2 = Z - 38.22
                        valor = sis.paraSIRGAS(X2, Y2, Z2)
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(valor[0])+'\n'+'#### Y: '+str(valor[1])+'\n'+'#### Z: '+str(valor[2]))

                    if sistema == 4 and sistema2 == 4:
                        valor = sis.CORREGO(lon, lat, h)
                        st.markdown('## Resultado')
                        st.markdown('#### X: '+str(valor[0])+'\n'+'#### Y: '+str(valor[1])+'\n'+'#### Z: '+str(valor[2]))
