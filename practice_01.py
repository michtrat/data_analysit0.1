import pandas as pd

column = ["Michał", "Natalia", "Papież"]
titles = {"Name": column,
          "Wzrost": [1.82, 1.65, 4.20],
          "Waga": [80, 60, 69]}
data = pd.DataFrame(titles)

select_column = data["Waga"][1]
select_row = data.iloc[1]["Waga"]  # komentarz

bmi = []

for i in range(len(data)):
    bmi_score = data["Waga"][i]/(data["Wzrost"][i]**2)
    bmi.append(bmi_score)
data["bmi"] = bmi

data.to_csv("bmi.csv", index=False, sep="\t")
print(data)
