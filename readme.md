# NF_TO_XML_SAMPA

## Sobre o Projeto

NF_TO_XML_SAMPA é uma ferramenta desenvolvida para facilitar a conversão de arquivos de Nota Fiscal Eletrônica (NF-e) para o formato XML compatível com o padrão oficial ABRASF 2.03 (com XSD). Utilizar esta ferramenta traz diversos ganhos, como:

- **Automatização**: Elimina processos manuais de conversão, reduzindo erros e economizando tempo.
- **Padronização**: Garante que os arquivos estejam no formato correto exigido pelo padrão oficial ABRASF 2.03 (com XSD).
- **Facilidade de uso**: Interface simples e comandos intuitivos.
- **Integração**: Pode ser facilmente integrada a outros sistemas ou fluxos de trabalho.

## Como Utilizar

### 1. Pré-requisitos
- Python 3.12 ou superior
- Ambiente virtual configurado (recomendado)
- Instalar as dependências necessárias (veja abaixo)

### 2. Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/NF_TO_XML_SAMPA.git
   cd NF_TO_XML_SAMPA
   ```
2. Crie e ative o ambiente virtual:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Formas de Utilização

### 1. Interface Web com Streamlit

Execute o aplicativo Streamlit para utilizar a interface gráfica:

```bash
streamlit run app.py
```

Você poderá fazer upload do arquivo CSV e baixar o XML gerado diretamente pela interface web.

### 2. API REST com FastAPI

Execute a API para conversão via requisição HTTP:

1. Instale os pacotes necessários:
   ```bash
   pip install fastapi uvicorn
   ```
2. Execute o servidor FastAPI:
   ```bash
   uvicorn api:app --reload
   ```
3. Acesse a documentação interativa em [http://localhost:8000/docs](http://localhost:8000/docs)

#### Exemplo de requisição via `curl`:
```bash
curl -X POST "http://localhost:8000/convert-csv" -F "file=@seuarquivo.csv" --output nfse_sp.xml
```

O arquivo XML será baixado como resposta.

### 3. Execução via linha de comando (se aplicável)

Caso o script principal aceite argumentos, execute:
```bash
python app.py --input seuarquivo.csv --output resultado.xml
```

## Suporte
Em caso de dúvidas ou problemas, abra uma issue no repositório ou entre em contato com o mantenedor.

---

**Ganhos ao utilizar esta ferramenta:**
- Redução de erros humanos
- Agilidade no processamento de documentos fiscais
- Facilidade de integração com sistemas contábeis
- Garantia de conformidade com o padrão oficial ABRASF 2.03 (com XSD)

