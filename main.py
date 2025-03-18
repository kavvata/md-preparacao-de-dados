
# %% carregando csv
import pandas as pd
import statistics as st

df_mamo = pd.read_csv("./data/mammographic_masses.data")
df_tratado = df_mamo.copy()
print(df_mamo)

# %% verificando quantos objetos tem dados faltando
dirty = df_mamo.query(
    'bi_rads == "?"'
    + 'or age == "?"'
    + 'or shape == "?"'
    + 'or margin == "?"'
    + 'or density == "?"'
    + 'or severity == "?"'
)

print(dirty)
