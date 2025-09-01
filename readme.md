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

### 3. Utilização

1. Coloque o arquivo de Nota Fiscal (ex: `nfse_sp.xml`) na pasta do projeto.
2. Execute o script principal:
   ```bash
   python app.py --input nfse_sp.xml --output resultado.xml
   ```
   - `--input`: caminho do arquivo NF-e a ser convertido
   - `--output`: nome do arquivo XML de saída

3. O arquivo convertido estará disponível no local especificado.

### 4. Exemplo de Uso
```bash
python app.py --input nfse_sp.xml --output resultado.xml
```

### 5. Suporte
Em caso de dúvidas ou problemas, abra uma issue no repositório ou entre em contato com o mantenedor.

---

**Ganhos ao utilizar esta ferramenta:**
- Redução de erros humanos
- Agilidade no processamento de documentos fiscais
- Facilidade de integração com sistemas contábeis
- Garantia de conformidade com o padrão oficial ABRASF 2.03 (com XSD)

