
# %% carregando csv
import pandas as pd
import statistics as st

df_mamo = pd.read_csv("./data/mammographic_masses.data")
df_tratado = df_mamo.copy()
print(df_mamo)

# %% verificando quantos objetos tem dados faltando
print(df_mamo.query(
    'bi_rads == "?"'
    + 'or age == "?"'
    + 'or shape == "?"'
    + 'or margin == "?"'
    + 'or density == "?"'
    + 'or severity == "?"'
# %% tratando dados faltantes em BI-RADS utilizando moda
filtro = df_mamo["bi_rads"] == "?"
moda_bi_rads = st.mode(
    df_mamo[df_mamo["bi_rads"] != "?"].bi_rads
)

print(f"moda bi_rads: {moda_bi_rads}")

print(df_mamo[filtro].bi_rads)

df_tratado.loc[filtro, 'bi_rads'] = int(moda_bi_rads) + df_tratado[filtro].severity

print(df_tratado[filtro])
