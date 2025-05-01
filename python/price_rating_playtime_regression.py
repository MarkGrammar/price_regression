import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

df = pd.read_csv("price_rating_playtime_regression.csv")  
df

# Linear Regression

X = df[['price', 'positive_ratings', 'negative_ratings']]
y = df['average_playtime']

model = LinearRegression()
model.fit(X, y)

print("Intercept (β₀):", model.intercept_)
print("Coefficients (β₁, β₂, β₃):", model.coef_)
print("R² score:", model.score(X, y))

# Linear R. Visualisation

plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['price'], y=df['average_playtime'], alpha=0.3, label='Data')

price_range = np.linspace(df['price'].min(), df['price'].max(), 100).reshape(-1, 1)
X_mean_values = [[p[0], df['positive_ratings'].mean(), df['negative_ratings'].mean()] for p in price_range]
predicted_playtime = model.predict(X_mean_values)

plt.plot(price_range, predicted_playtime, color='red', label='Regression Line')

plt.title('Price vs Average Playtime')
plt.xlabel('Price ($)')
plt.ylabel('Average Playtime (minutes)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Anlamsız oldu çıkan doğrudan pek bir şey anlaşılmıyor. Outlier'lardan büyük ihtimalle

# Filtreli Regression Grafiği (2000 dk'nın üzerini almadım)

df_filtered = df[df['average_playtime'] < 2000]

X_filtered = df_filtered[['price', 'positive_ratings', 'negative_ratings']]
y_filtered = df_filtered['average_playtime']

model_filtered = LinearRegression()
model_filtered.fit(X_filtered, y_filtered)



print("Intercept (β₀):", model.intercept_)
print("Coefficients (β₁, β₂, β₃):", model.coef_)
print("R² score:", model.score(X, y))


# Regression Graph

os.makedirs("figures", exist_ok=True)

plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['price'], y=df['average_playtime'], alpha=0.3, label='Data')

price_range = np.linspace(df['price'].min(), df['price'].max(), 100).reshape(-1, 1)
X_mean_values = [[p[0], df['positive_ratings'].mean(), df['negative_ratings'].mean()] for p in price_range]
predicted_playtime = model.predict(X_mean_values)

plt.plot(price_range, predicted_playtime, color='red', label='Regression Line')

plt.title('Price vs Average Playtime')
plt.xlabel('Price ($)')
plt.ylabel('Average Playtime (minutes)')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("figures/price_vs_playtime_regression.capped.png", dpi=300)

plt.show()