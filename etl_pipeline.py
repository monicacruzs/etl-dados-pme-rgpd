import pandas as pd
import json
import numpy as np # Necessário para funções de limpeza de dados
import re # Necessário para funções de texto (embora não usado neste T, é bom ter)

# ==============================================================================
# FASE E: EXTRAÇÃO (Caminho ajustado para o diretório 'data/')
# ==============================================================================
def extract_data(file_path='data/faturas_raw.json'):
    """Lê o arquivo JSON, simulando a extração de dados de faturas."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        df = pd.DataFrame(data)
        
        print(f"✅ Extração Concluída: {len(df)} registros lidos.")
        print("\n--- DataFrame Original (Tipos Brutos) ---")
        print(df.head()) 
        print(df.dtypes)
        print("------------------------------------------\n")
        
        return df
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo '{file_path}' não encontrado. Certifique-se de que a pasta 'data' e o arquivo estão no local correto.")
        return None

# ==============================================================================
# FASE T: TRANSFORMAÇÃO (Limpeza e Governança RGPD - Ação Principal)
# ==============================================================================
def transform_data(df):
    """Realiza a limpeza, tipagem e padronização dos dados e anonimização RGPD."""

    print("⏳ Iniciando Transformação (Fase T)...")
    
    # 1. Tratar Nulos (Imposto)
    df['imposto_valor'] = df['imposto_valor'].fillna('R$ 0.00')
    
    # 2. Limpeza e Conversão de Tipos (Valores)
    def clean_currency(value):
        if isinstance(value, str):
            value = value.replace('R$', '').replace(' ', '').replace(',', '.')
        try:
            return float(value)
        except (ValueError, TypeError):
            return 0.0

    df['imposto_valor_float'] = df['imposto_valor'].apply(clean_currency)
    df['valor_total_float'] = df['valor_total'].apply(clean_currency)
    
    # Converte 'taxa_desconto' para float
    df['taxa_desconto'] = pd.to_numeric(df['taxa_desconto'], errors='coerce').fillna(0.0)

    # 3. Padronização de Texto (Status)
    df['status_pagamento'] = df['status_pagamento'].str.lower()
    
    # 4. TRATAMENTO DE NULOS (Data)
    df['data_emissao'] = df['data_emissao'].fillna('1900-01-01')
    
    # 5. [CAMADA KAURA] - Anonimização RGPD (nif_cliente)
    df['cliente_id_anonimo'] = 'CLIENTE_' + df['id_fatura'].astype(str)
    # Remove colunas brutas e sensíveis
    df = df.drop(columns=['nif_cliente', 'imposto_valor', 'valor_total']) 

    print("✅ Transformação Concluída.")
    print("\n--- DataFrame Transformado (Pronto para Load) ---")
    print(df.head())
    print(df.dtypes)
    print("------------------------------------------------\n")
    
    return df

# ==============================================================================
# FASE L: LOAD (Carregamento)
# ==============================================================================
def load_data(df, output_file='data/faturas_processed.csv'):
    """Carrega o DataFrame transformado para um arquivo CSV."""
    
    print(f"⏳ Iniciando Carregamento (Fase L)...")
    
    df.to_csv(output_file, index=False)
    
    print(f"✅ Carregamento Concluído! Dados salvos em: {output_file}")

# ==============================================================================
# PONTO DE ENTRADA PRINCIPAL (Com todas as chamadas)
# ==============================================================================
if __name__ == "__main__":
    df_extraido = extract_data()
    
    if df_extraido is not None:
        df_transformado = transform_data(df_extraido)
        
        # Chamada para a Fase L
        load_data(df_transformado)