# Importa as bibliotecas necessárias
# Rode: !pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
import re

# Função para fazer web scraping em um site de notícias
def scrape_news(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Procura por parágrafos no texto principal da página
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        return " ".join(paragraphs)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL {url}: {e}")
        return ""

# Lista de palavras-chave para identificar violações de direitos
keywords = ['abuso infantil', 'trabalho infantil', 'violência contra criança', 'exploração infantil', 'maus-tratos']

# Exemplo de URL de um site de notícias
# **Substitua pela URL de um site de notícias real**
news_url = 'https://g1.globo.com/' # Esta é uma URL de exemplo
news_text = scrape_news(news_url)

# Converte o texto para minúsculas para facilitar a busca
news_text_lower = news_text.lower()

# Busca por palavras-chave no texto
encontradas = [keyword for keyword in keywords if re.search(r'\b' + keyword + r'\b', news_text_lower)]

if encontradas:
    print(f"Palavras-chave encontradas no artigo: {', '.join(encontradas)}")
else:
    print("Nenhuma palavra-chave relacionada a violações de direitos da criança foi encontrada.")

# Para o Azure, você poderia usar Azure Functions para rodar este código
# em um agendamento e Azure Cosmos DB para armazenar os resultados.
