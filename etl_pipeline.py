import pandas as pd
import json

# ==============================================================================
# FASE E: EXTRAÇÃO (Caminho ajustado para o diretório 'data/')
# ==============================================================================
def extract_data(file_path='data/faturas_raw.json'):
    """Lê o arquivo JSON, simulando a extração de dados de faturas."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Converte a lista de dicionários para um DataFrame do Pandas
        df = pd.DataFrame(data)
        
        print(f"✅ Extração Concluída: {len(df)} registros lidos.")
        print("\n--- DataFrame Original ---")
        # Visualizando as primeiras linhas e tipos de dados para análise da Fase T
        print(df.head()) 
        print(df.dtypes)
        print("--------------------------\n")
        
        return df
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo '{file_path}' não encontrado. Certifique-se de que a pasta 'data' e o arquivo estão no local correto.")
        return None

# Ponto de entrada do script
if __name__ == "__main__":
    df_extraido = extract_data()
    
    # A Fase T (Transformação) virá aqui no próximo passo!
    if df_extraido is not None:
        pass
