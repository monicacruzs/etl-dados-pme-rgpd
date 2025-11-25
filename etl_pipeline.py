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

# ==============================================================================
# FASE L: LOAD (Carregamento)
# ==============================================================================
def load_data(df, output_file='data/faturas_processed.csv'):
    """Carrega o DataFrame transformado para um arquivo CSV."""
    
    print(f"⏳ Iniciando Carregamento (Fase L)...")
    
    # Salva o DataFrame no formato CSV (Comma Separated Values)
    # index=False evita salvar o índice numérico do Pandas no arquivo
    df.to_csv(output_file, index=False)
    
    print(f"✅ Carregamento Concluído! Dados salvos em: {output_file}")

# ==============================================================================
# PONTO DE ENTRADA PRINCIPAL (Atualizado)
# ==============================================================================
if __name__ == "__main__":
    df_extraido = extract_data()
    
    if df_extraido is not None:
        df_transformado = transform_data(df_extraido)
        
        # Chamada para a nova Fase L (LOAD)
        load_data(df_transformado)
