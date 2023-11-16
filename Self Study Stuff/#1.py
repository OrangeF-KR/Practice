import matplotlib.pyplot as plt

ages = ['10대', '20대', '30대', '40대', '50대', '60대', '70대', '80대']

male_ratio = [9.2, 18.7, 23.5, 23.5, 22.1, 18.2, 12.3, 4.2]
female_ratio = [8.7, 17.6, 22.3, 23.2, 23.7, 19.6, 15.1, 6.4]

plt.stackplot(ages, male_ratio, female_ratio, colors=['blue','red'])

plt.title('도쿄 연령대별 인구 비율')
plt.xlabel('연령대')
plt.ylabel('비율(%)')
plt.legend(['남자','여자'])

plt.show()