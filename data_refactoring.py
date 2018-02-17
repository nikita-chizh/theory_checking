import pandas
import os

categorical_cols = [
    "paragraph_num",
    "rubric_id",
    "test_underlying",
    "is_num_in_head",
    "is_year_in_head",
    "is_quest_sign_in_head",
    "is_voskl_sign_head",
    "is_semicolon_in_head",
    "is_celeb_connected",
    "has_vurezka",
    "has_inst",
    "has_twit",
    "has_fb",
    "has_vk",
    "has_ytube",
    "is_unterw",
    "has_videoscr",
    "has_query",
    "has_service",
    "has_sing_pict",
]

cwd = os.getcwd()
filename = cwd + "/data.xlsx"
# FILTERING: remove < 250 pageviews
df = pandas.read_excel(filename,)
df = df[df.Pageviews > 250]
df = df.drop(["ID "], axis=1)
df['id'] = range(1, len(df) + 1)
df.set_index('id')
df.to_csv(cwd + "/filtered.csv")
#CATEGORIZING:
categorised = pandas.get_dummies(df, columns=categorical_cols)
categorised.to_csv(cwd + "/categorised.csv")

# SCAING AND SPLITING
def scale_colum(df, col_name):
    df[col_name] = df.apply(lambda x: (x.astype(float) - min(x)) / (max(x) - min(x)), axis=0)[col_name]

df = categorised
# scaling
columns = ["symbols", "average_line_length"]
# delete ejection
df = df[df.symbols < 10000]
scale_colum(df, "symbols")
scale_colum(df, "average_line_length")
# now split dataFrame to test and learn
# each 20th is for testing
X_test = df[df.id % 20 == 0]
X_learn = df[df.id % 20 != 0]
Y_test = X_test[["Pageviews", "Avg. Time on Page", "Percent Scrolls"]]
Y_learn = X_learn[["Pageviews", "Avg. Time on Page", "Percent Scrolls"]]
#delete cols
X_learn = X_learn[X_learn.columns.difference(["id", "Pageviews", "Avg. Time on Page", "Percent Scrolls"])]
X_test = X_test[X_test.columns.difference(["id", "Pageviews", "Avg. Time on Page", "Percent Scrolls"])]
# write all
X_test.to_csv(cwd + "/X_test.csv")
X_learn.to_csv(cwd + "/X_learn.csv")
Y_test.to_csv(cwd + "/Y_test.csv")
Y_learn.to_csv(cwd + "/Y_learn.csv")
