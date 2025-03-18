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
# %% tratando de dados faltantes em forma
moda_forma_benigna = st.mode([int(shape) for shape in df_mamo.loc[
    (df_mamo["severity"] == 0) & (df_mamo["shape"] != "?"), "shape"
]])

moda_forma_maligna = st.mode([int(shape) for shape in df_mamo.loc[
    (df_mamo["severity"] == 1) & (df_mamo["shape"] != "?"), "shape"
]])


print(f"media forma severidade benigna : {moda_forma_benigna}")
print(f"media forma severidade maligna : {moda_forma_maligna}")

filtro = (df_mamo["shape"] == "?")
print(df_mamo[filtro].head())

df_tratado.loc[filtro & (df_mamo["severity"] == 0), 'shape'] = moda_forma_benigna
df_tratado.loc[filtro & (df_mamo["severity"] == 1), 'shape'] = moda_forma_maligna

print(df_tratado[filtro].head())

# %% tratando de dados faltantes em contorno
moda_contorno_benigna = st.mode([int(margin) for margin in df_mamo.loc[
    (df_mamo["severity"] == 0) & (df_mamo["margin"] != "?"), "margin"
]])

moda_contorno_maligna = st.mode([int(margin) for margin in df_mamo.loc[
    (df_mamo["severity"] == 1) & (df_mamo["margin"] != "?"), "margin"
]])

print(f"media contorno severidade benigna : {moda_contorno_benigna}")
print(f"media contorno severidade maligna : {moda_contorno_maligna}")

filtro = df_mamo["margin"] == "?"

print(df_mamo[filtro].head(6))

df_tratado.loc[filtro & (df_mamo["severity"] == 0), "margin"] = moda_contorno_benigna
df_tratado.loc[filtro & (df_mamo["severity"] == 1), "margin"] = moda_contorno_maligna

print(df_tratado[filtro].head(6))

# %% tratando dados faltantes em densidade

# NOTE: no material fornecido pelo livro, a densidade é a mesma para as duas classes,
# sendo possivel eliminar um calculo de moda
moda_densidade_benigna = st.mode([int(density) for density in df_mamo.loc[
    (df_mamo["severity"] == 0) & (df_mamo["density"] != "?"), "density"
]])
moda_densidade_maligna = st.mode([int(density) for density in df_mamo.loc[
    (df_mamo["severity"] == 1) & (df_mamo["density"] != "?"), "density"
]])

print(f"media densidade severidade benigna : {moda_densidade_benigna}")
print(f"media densidade severidade maligna : {moda_densidade_maligna}")

filtro = df_mamo["density"] == "?"

print(df_mamo[filtro].head())

df_tratado.loc[filtro & (df_mamo["severity"] == 0), "density"] = moda_densidade_benigna
df_tratado.loc[filtro & (df_mamo["severity"] == 1), "density"] = moda_densidade_maligna

print(df_tratado[filtro].head())
