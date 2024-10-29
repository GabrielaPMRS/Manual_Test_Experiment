import matplotlib.pyplot as plt
import seaborn as sns
import ptitprince as pt
import pandas as pd


def create_raincloud_plot(d):
    # Combinar dados para seaborn e ptitprince
    with_smell = d['with_smell']
    without_smell = d['without_smell']
    dados = pd.DataFrame({
        'Execution Time (seconds)': with_smell + without_smell,
        'Condition': ['With Smell'] * len(with_smell) + ['Without Smell'] * len(without_smell)
    })

    # Configuração do gráfico
    plt.figure(figsize=(10, 6))
    ax = pt.RainCloud(x='Condition', y='Execution Time (seconds)', data=dados,
                      palette=['red', 'blue'], bw=.2, width_viol=.6,
                      orient='h', alpha=.65, dodge=True)

    # Título e rótulos
    plt.title(d['title'], fontsize=14)
    plt.xlabel("Execution Time (seconds)")
    plt.tight_layout()

    # Salvar o gráfico em alta resolução
    plt.savefig(f'raincloud_{d["name"]}.png', dpi=300)


if __name__ == "__main__":
    # Dados para os quatro testes
    dados = [
        {
            'name': 'exe_time_test_1',
            'with_smell': [295, 219, 76, 116, 160, 103, 362, 140, 256, 209, 320, 250, 612, 541, 414],
            'without_smell': [43, 22, 25, 56, 35, 15, 23, 22, 97, 19, 26, 14, 29, 19, 28],
            'title': 'Test 1: Comparison of critical zone time in seconds'
        },
        {
            'name': 'exe_time_test_2',
            'with_smell': [48, 63, 104, 67, 115, 115, 143, 52, 40, 154, 46, 86, 86, 332, 149],
            'without_smell': [33, 30, 54, 65, 18, 28, 29, 189, 61, 20, 31, 13, 28, 17, 23],
            'title': 'Test 2: Comparison of critical zone time in seconds'
        },
        {
            'name': 'exe_time_test_3',
            'with_smell': [31, 21, 17, 74, 12, 32, 29, 20, 47, 34, 26, 22, 28, 115, 54],
            'without_smell': [47, 46, 95, 21, 83, 38, 64, 31, 38, 36, 49, 34, 25, 33, 39],
            'title': 'Test 3: Comparison of critical zone time in seconds'
        },
        {
            'name': 'exe_time_test_4',
            'with_smell': [33, 34, 247, 65, 31, 48, 64, 32, 62, 49, 41, 56, 60, 86, 80],
            'without_smell': [115, 95, 152, 57, 41, 59, 68, 70, 88, 51, 67, 34, 34, 59, 51],
            'title': 'Test 4: Comparison of critical zone time in seconds'
        }
    ]

    for d in dados:
        create_raincloud_plot(d)
