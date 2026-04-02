import matplotlib.pyplot as plt
import seaborn as sns

# Generate a plot
sns.set_theme()
tips = sns.load_dataset("tips")
sns.relplot(data=tips, x="total_bill", y="tip")

# Save functionality
plt.savefig("my_chart.png", dpi=300, bbox_inches='tight')
plt.show()