nilai_siswa.csv
pip install pandas matplotlib seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('nilai_siswa.csv')

data.info()
print(data.head())
print(data.describe())

print('----------------------------------')

print("rata-rata:", data['Nilai'].mean())
print("median:", data['Nilai'].median())
print("modus:", data['Nilai'].mode()[0])

print('----------------------------------')

matematika = data[data['Matpel'] == 'Matematika']
print("rata-rata matematika:", matematika['Nilai'].mean())
print("median matematika:", matematika['Nilai'].median())
print("modus matematika:", matematika['Nilai'].mode()[0])
print(matematika)

print('----------------------------------')

bahasaindonesia = data[data['Matpel'] == 'Bahasa Indonesia']
print("rata-rata bahasa indonesia:", bahasaindonesia['Nilai'].mean())
print("median bahasa indonesia:", bahasaindonesia['Nilai'].median())
print("modus bahasa indonesia:", bahasaindonesia['Nilai'].mode()[0])
print(bahasaindonesia)

print('----------------------------------')

bahasainggris = data[data['Matpel'] == 'Bahasa Inggris']
print("rata-rata bahasa inggris:", bahasainggris['Nilai'].mean())
print("median bahasa inggris:", bahasainggris['Nilai'].median())
print("modus bahasa inggris:", bahasainggris['Nilai'].mode()[0])
print(bahasainggris)

print('----------------------------------')

produktif = data[data['Matpel'] == 'Produktif']
print("rata-rata produktif:", produktif['Nilai'].mean())
print("median produktif:", produktif['Nilai'].median())
print("modus produktif:", produktif['Nilai'].mode()[0])
print(produktif)

print('----------------------------------')

fisika = data[data['Matpel'] == 'Fisika']
print("rata-rata fisika:", fisika['Nilai'].mean())
print("median fisika:", fisika['Nilai'].median())
print("modus fisika:", fisika['Nilai'].mode()[0])
print(fisika)

print('----------------------------------')

data.groupby('Matpel')['Nilai'].agg(['max','min'])
rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Matpel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.tight_layout()
plt.show()

sns.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.tight_layout()
plt.show()
