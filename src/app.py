import streamlit as st
from cv_parser import extraer_texto_pdf, extraer_skills
from main import obtener_todas_las_ofertas
from matcher import calcular_compatibilidad

st.set_page_config(page_title="CV Job Matcher", page_icon="🎯")
st.title(" CV Job Matcher")
st.write("Sube tu CV y encuentra las ofertas de trabajo más compatibles en Chile.")

archivo = st.file_uploader("Sube tu CV en PDF", type="pdf")

if archivo is not None:
    texto_cv = extraer_texto_pdf(archivo)
    skills = extraer_skills(texto_cv)

    st.subheader("Skills detectadas")
    st.write(", ".join(skills) if skills else "No se detectaron skills conocidas.")

    cantidad = st.slider("¿Cuántas ofertas mostrar?", min_value=5, max_value=50, value=20, step=5)

    if st.button("🔍 Buscar ofertas compatibles"):
        with st.spinner("Recolectando ofertas de ChileTrabajos, GetOnBrd y BNE... (BNE puede tardar ~1 min)"):
            ofertas = obtener_todas_las_ofertas()
            resultado = calcular_compatibilidad(texto_cv, ofertas)

        st.success(f"Se analizaron {len(ofertas)} ofertas")
        st.subheader(f"Top {cantidad} más compatibles")

        for oferta in resultado[:cantidad]:
            titulo_expander = f"{oferta['compatibilidad']}% — {oferta['titulo']} · {oferta['fuente']}"
            with st.expander(titulo_expander):
                if oferta["fecha"]:
                    st.caption(f"📅 Publicada: {oferta['fecha']}")
                st.write(oferta["descripcion"])
                st.markdown(f"[Ver oferta completa]({oferta['url']})")