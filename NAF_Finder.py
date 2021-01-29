import streamlit as st
import requests
import json

st.title('NAF Finder')

def get_ape_code(siren_number):

    siren_number = str(siren_number).replace(' ','')
    url = "https://entreprise.data.gouv.fr/api/sirene/v3/unites_legales/" + siren_number
     
    try:
    	res = requests.get(url).json()
    	return str(res["unite_legale"]["activite_principale"]).replace('.','')
    except:
        return "Error - Check Société.com"

SIREN_to_check = st.number_input('Insert SIREN number', value=804645034)


st.write('NAF code of ', SIREN_to_check, 'is : ', get_ape_code(SIREN_to_check))