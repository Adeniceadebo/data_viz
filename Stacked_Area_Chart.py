# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
# the difference between the international and domestic services
df_international_domestic_services = pd.read_csv('international_domestic_services.csv')
df_international_domestic_services

colors =['#011638', '#7e2987']
labels = ['International', 'Domestic']
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
plt.stackplot(df_international_domestic_services['Date'],
                 df_international_domestic_services['International'],
                 df_international_domestic_services['Domestic'],
                 labels=labels, colors=colors, alpha=0.8, edgecolor='none')
plt.xticks(df_international_domestic_services['Date'], rotation=45)
plt.legend(loc='upper left', fontsize=12, labels =labels)
plt.ylabel('Number of Services', fontsize=14)
plt.xlabel('Dates', fontsize=14)
plt.title('International vs Domestic Services Over Time', fontsize=16,weight='bold', colors='black')
plt.savefig('international_vs_domestic_services.png', dpi=300)
sns.despine()
plt.tight_layout()
plt.show()
# %%