# %%
import json
import pandas as pd
import streamlit as st

# %%
# openfile
json_path = f"Adisawi_toydata.json"
with open(json_path, "r") as f:
    xxx: dict = json.load(f)

# %%
# pandas
df = pd.DataFrame()
df["created_at"] = [x["createdAt"] for x in xxx]
df["type"] = [x["type"] for x in xxx]
df["notes_id"] = [f"""https://misskey.io/notes/{x["note"]["id"]}""" for x in xxx]

# %% title
st.title("Adisawi@misskey.io さんがリアクションしたノートの検索")
st.markdown("リアクションからノートを検索しよう")

# %% input reaction
reaction_origin = st.text_input("検索したいリアクションを入れよう")
reaction_searchword = f"{reaction_origin[:-1]}@.:"

# %% calc table
df_search = df[df["type"] == reaction_searchword]

# %% df_searchの結果について
st.write(f"{len(df_search)=}")
st.table(df_search)

if __name__ == '__main__':
    pass
