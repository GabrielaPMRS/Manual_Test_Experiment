import matplotlib.pyplot as plt


def create_histograms(d: dict):
    # Dados para os grupos
    dados_with_smell = d['with_smell']  # [passaram, não passaram]
    dados_without_smell = d['without_smell']  # [passaram, não passaram]

    # Nomes para os segmentos dos gráficos
    nomes = ['Passed', 'Failed']

    # Configurar a tela gráfica para ter 2 gráficos em 1 linha
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Gráfico de barras para o grupo With Smell
    axes[0].bar(nomes, dados_with_smell, color=['blue', 'red'], alpha=0.7)
    axes[0].set_title(
        f'{d["name"].replace("_", " ").title()}: Comparison of Test Result (With Smell)')
    axes[0].set_ylabel('Number of Participants')

    # Gráfico de barras para o grupo Without Smell
    axes[1].bar(nomes, dados_without_smell, color=['blue', 'red'], alpha=0.7)
    axes[1].set_title(
        f'{d["name"].replace("_", " ").title()}: Comparison of Test Result (Without Smell)')

    # Salvar o gráfico em alta resolução
    plt.tight_layout()
    plt.savefig(f'result_{d["name"]}.png', dpi=300)


if __name__ == "__main__":
    # Dados de exemplo para os quatro testes
    dados = [
        {
            'name': 'test_1',
            'with_smell': [5, 10],  # Passaram, Não passaram
            'without_smell': [15, 0],  # Passaram, Não passaram
        },
        {
            'name': 'test_2',
            'with_smell': [9, 6],  # Passaram, Não passaram
            'without_smell': [14, 1],  # Passaram, Não passaram
        },
        {
            'name': 'test_3',
            'with_smell': [15, 0],  # Passaram, Não passaram
            'without_smell': [15, 0],  # Passaram, Não passaram
        },
        {
            'name': 'test_4',
            'with_smell': [14, 1],  # Passaram, Não passaram
            'without_smell': [15, 0],  # Passaram, Não passaram
        }
    ]

    for d in dados:
        create_histograms(d)
