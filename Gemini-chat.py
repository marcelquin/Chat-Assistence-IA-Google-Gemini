import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configura a API do Gemini
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

def chat_with_gemini(prompt):
    try:
        # Inicializa o modelo
        model = genai.GenerativeModel('gemini-pro')
        
        # Gera a resposta
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

def main():
    print("Bem-vindo ao Chat com Gemini!")
    print("Digite 'sair' para encerrar o programa.")
    
    while True:
        pergunta = input("\nVocê: ")
        if pergunta.lower() == 'sair':
            print("Até logo!")
            break
        
        resposta = chat_with_gemini(pergunta)
        print(f"\nGemini: {resposta}")

if __name__ == "__main__":
    main()