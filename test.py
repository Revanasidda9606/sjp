import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('titanic.csv')
plt.scatter(df['Age'],df['Fare'])
plt.title('Age vs price')
plt.xlabel('Age')
plt.ylabel('Price')
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('titanic.csv')
plt.boxplot(df['Fare'])
plt.title('Box Plot of Fare')
plt.ylabel('Fare')
plt.show()


















# plt.boxplot(df['mpg'])
# plt.title('Box Plot of MPG')
# plt.ylabel('MPG')
# plt.show()

