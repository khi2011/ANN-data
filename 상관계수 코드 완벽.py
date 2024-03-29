import numpy as np
import matplotlib.pyplot as plt

# CSV 파일에서 데이터 읽어오기
with open(r'C:\Users\user\Desktop\240325_Creep data_test2.csv', 'r') as f:
    first_row = f.readline().strip().split(',')

data = np.genfromtxt(r'C:\Users\user\Desktop\240325_Creep data_test2.csv', delimiter=',', skip_header=1)  # 첫 번째 행은 변수 이름이므로 건너뜁니다

# 상관 행렬 계산
correlation_matrix = np.corrcoef(data, rowvar=False)

# 글꼴 및 글자 크기 설정
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 15

# 열린 히트맵 시각화
plt.figure(figsize=(10, 10))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar(label='Correlation coefficient')
plt.title('Correlation Coefficient')
plt.xticks(ticks=np.arange(len(first_row)), labels=first_row, rotation=90)
plt.yticks(ticks=np.arange(len(first_row)), labels=first_row)
#plt.xlabel('Input Elements')
#plt.ylabel('Input Elements')
plt.tight_layout() 
plt.show()
