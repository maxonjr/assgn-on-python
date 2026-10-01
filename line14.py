import seaborn as sns
import pandas as pd

data = pd.DataFrame({'x':[1,2,3,4],'y': [10,20,25,30]})
sns.scatterplot(x='x', y='y', data=data)
plt.show()