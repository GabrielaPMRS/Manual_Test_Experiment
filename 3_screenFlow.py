import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def create_violinplot(d: dict):
    with_smell = d['with_smell']
    without_smell = d['without_smell']

    dados = pd.DataFrame({
        'Screen Flow (steps)': with_smell + without_smell,
        'Test': ['With Smell'] * len(with_smell) + ['Without Smell'] * len(without_smell)
    })

    # Crie o violin plot
    plt.figure(figsize=(8, 6))
    sns.violinplot(data=dados, x='Test', y='Screen Flow (steps)', hue='Test', dodge=False,
                   palette=["red", "green"])

    # Adicione os pontos médios
    means = [np.mean(with_smell), np.mean(without_smell)]
    for i, mean in enumerate(means):
        plt.plot(i, mean, 'o', color='black')

    # Personalize o gráfico
    plt.title(d['title'])
    plt.xlabel("Test")
    plt.ylabel("Screen Flow (steps)")

    plt.savefig(f'violinplot_{d["name"]}.png', dpi=300)


if __name__ == "__main__":
    dados = [
        {
            'name': 'screenFlow_test_1',
            'with_smell': [49, 25, 27, 28, 47, 14, 66, 43, 33, 32, 49, 76, 96, 101, 63],
            'without_smell': [3, 3, 4, 4, 4, 3, 3, 3, 29, 3, 9, 3, 3, 4, 4],
            'title': 'Test 1: Comparison of critical zone screen flow'
        },
        {
            'name': 'screenFlow_test_2',
            'with_smell': [6, 18, 17, 11, 28, 27, 32, 15, 11, 30, 13, 67, 13, 45, 22],
            'without_smell': [4, 3, 9, 6, 6, 4, 5, 13, 10, 4, 6, 3, 4, 3, 4],
            'title': 'Test 2: Comparison of critical zone screen flow'
        },
        {
            'name': 'screenFlow_test_3',
            'with_smell': [5, 4, 2, 4, 3, 4, 4, 3, 12, 4, 4, 3, 3, 6, 6],
            'without_smell': [4, 4, 10, 3, 11, 4, 5, 4, 3, 4, 4, 6, 6, 4, 6],
            'title': 'Test 3: Comparison of critical zone screen flow'
        },
        {
            'name': 'screenFlow_test_4',
            'with_smell': [8, 11, 39, 8, 6, 10, 17, 8, 7, 8, 10, 16, 8, 10, 11],
            'without_smell': [16, 10, 20, 7, 7, 7, 12, 10, 10, 9, 12, 7, 7, 10, 11],
            'title': 'Test 4: Comparison of critical zone screen flow'
        }
    ]

    for d in dados:
        create_violinplot(d)


# # Dados
# with_smell = [49, 25, 27, 28, 47, 14, 66, 43, 33, 32, 49, 76, 96, 101, 63]
# without_smell = [3, 3, 4, 4, 4, 3, 3, 3, 29, 3, 9, 3, 3, 4, 4]

# # Combine os dados em um dataframe para Seaborn
# dados = pd.DataFrame({
#     'Screen Flow (steps)': with_smell + without_smell,
#     'Test': ['With Smell'] * len(with_smell) + ['Without Smell'] * len(without_smell)
# })

# # Crie o violin plot
# plt.figure(figsize=(8, 6))
# sns.violinplot(data=dados, x='Test', y='Screen Flow (steps)', hue='Test',
#                palette=["red", "green"])

# # Adicione os pontos médios
# means = [np.mean(with_smell), np.mean(without_smell)]
# for i, mean in enumerate(means):
#     plt.plot(i, mean, 'o', color='black')

# # Personalize o gráfico
# plt.title("Test 1: Comparison of critical zone screen flow")
# plt.xlabel("Test")
# plt.ylabel("Screen Flow (steps)")


# plt.savefig("beanplot_high_res.png", dpi=300)
