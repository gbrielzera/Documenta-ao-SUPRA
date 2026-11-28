# TesteDouglas
# Caminho: Catálogo > Biblioteca de scripts > TesteDouglas
# Fonte: Utilização_de_veículo_locado_Versão_10_Indenização_por_Guarda_e_zelo_do_veículo_da_frota_(Lote).xml

import clr
clr.AddReference("System.Net.Http")
clr.AddReference("Newtonsoft.Json")

from System.Net.Http import HttpClient, StringContent
from System.Text import Encoding
from System import Uri
from System.Threading.Tasks import Task
import json

def generate_content_with_gemini(api_key, prompt):
    """
    Função que se conecta à API do Gemini e retorna a resposta.
    """
    
    api_endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="
    url = Uri(api_endpoint + api_key)

    client = HttpClient()

    # Monta o corpo da requisição em JSON
    json_body = '{"contents":[{"parts":[{"text":"%s"}]}]}' % prompt.replace('"', '\\"')
    content = StringContent(json_body, Encoding.UTF8, "application/json")

    # Faz a requisição de forma assíncrona
    task = client.PostAsync(url, content)
    task.Wait() # Espera a requisição terminar

    response = task.Result
    
    # Verifica se a requisição foi bem sucedida
    response.EnsureSuccessStatusCode()

    # Lê o conteúdo da resposta de forma assíncrona
    response_task = response.Content.ReadAsStringAsync()
    response_task.Wait() # Espera a leitura terminar

    response_body = response_task.Result

    # Processa o JSON para extrair o texto
    try:
        data = json.loads(response_body)
        text_response = data['candidates'][0]['content']['parts'][0]['text']
        return text_response
    except (KeyError, json.JSONDecodeError) as e:
        return "Erro ao processar a resposta da API: " + str(e)
