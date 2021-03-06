import streamlit as st
import requests
import json

st.title('Pro Info Finder')

def get_naf_code(siren_number):

    siren_number = str(siren_number).replace(' ','')
    url = "https://entreprise.data.gouv.fr/api/sirene/v3/unites_legales/" + siren_number

    info_dict = {}
     
    try:
        res = requests.get(url).json()

        info_dict["Address"] = res["unite_legale"]["etablissement_siege"]["geo_adresse"]
        info_dict["ZIP"] = res["unite_legale"]["etablissement_siege"]["code_postal"]
        info_dict["City"] = res["unite_legale"]["etablissement_siege"]["libelle_commune"]
        info_dict["NAF"] = str(res["unite_legale"]["activite_principale"]).replace('.','')
        info_dict["Creation_date"] = res["unite_legale"]["date_creation"]
        info_dict["Legal_category"] = res["unite_legale"]["categorie_juridique"]
        info_dict["TVA_Intra"] = res["unite_legale"]["numero_tva_intra"]
        info_dict["Name"] = res["unite_legale"]["denomination"]

        return info_dict
    except:
        return "Error - Check Société.com"

SIREN_to_check = st.number_input('Insert SIREN number', value=534479589)
res = get_naf_code(SIREN_to_check)

try:
    st.write('**Legal name is :** ', res["Name"])
    st.write('**Address is :** ', res["Address"])
    st.write('**ZIP is :** ', res["ZIP"])
    st.write('**City is :** ', res["City"])
    st.write('**NAF is :** ', res["NAF"])
    st.write('**Date of creation is :** ', res["Creation_date"])
    st.write('**Legal cateogry is :** ', res["Legal_category"])
    st.write('**TVA Intracommunautaire is :** ', res["TVA_Intra"])
except:
    st.write('**Error - Check Société.com**')
