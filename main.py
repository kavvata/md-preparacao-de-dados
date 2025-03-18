# %% carregando csv
from numpy import floor
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
))
# %% tratando dados faltantes em BI-RADS utilizando moda
filtro = df_mamo["bi_rads"] == "?"
moda_bi_rads = st.mode(df_mamo[df_mamo["bi_rads"] != "?"].bi_rads)

print(f"moda bi_rads: {moda_bi_rads}")

print(df_mamo[filtro].bi_rads)

df_tratado.loc[filtro, 'bi_rads'] = int(moda_bi_rads) + df_tratado[filtro].severity

print(df_tratado[filtro])
# %% tratando dados faltantes em idade
media_idade = st.mean([int(age) for age in df_mamo.loc[df_mamo["age"] != "?"].age])
media_idade = int(floor(media_idade))
print(f"media idade: {media_idade}")

filtro = df_mamo["age"] == "?"
print(df_mamo[filtro])

df_tratado.loc[filtro, 'age'] = media_idade

print(df_tratado[filtro])
