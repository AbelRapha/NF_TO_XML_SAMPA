import pandas as pd
import xml.etree.ElementTree as ET
import streamlit as st
import io

def converter_csv_para_xml(df: pd.DataFrame) -> bytes:
    """
    Converte o DataFrame de CSV da NFSe-SP no layout oficial ABRASF para XML.
    Retorna os bytes do XML.
    """
    # Remove linhas "Total"
    df = df[df["Tipo de Registro"] != "Total"]

    # Raiz XML
    root = ET.Element("ListaNfse")

    for _, row in df.iterrows():
        nfse = ET.SubElement(root, "Nfse")
        inf_nfse = ET.SubElement(nfse, "InfNfse")

        # Dados básicos
        ET.SubElement(inf_nfse, "Numero").text = row["Nº NFS-e"]
        ET.SubElement(inf_nfse, "CodigoVerificacao").text = row["Código de Verificação da NFS-e"]
        ET.SubElement(inf_nfse, "DataEmissao").text = row["Data Hora NFE"].split(" ")[0]

        # Identificação RPS
        identificacao_rps = ET.SubElement(inf_nfse, "IdentificacaoRps")
        ET.SubElement(identificacao_rps, "Numero").text = row["Número do RPS"]
        ET.SubElement(identificacao_rps, "Serie").text = row["Série do RPS"]
        ET.SubElement(identificacao_rps, "Tipo").text = "1"

        # Serviço
        servico = ET.SubElement(inf_nfse, "Servico")
        valores = ET.SubElement(servico, "Valores")
        ET.SubElement(valores, "ValorServicos").text = row["Valor dos Serviços"].replace(".", "").replace(",", ".")
        ET.SubElement(valores, "ValorDeducoes").text = row["Valor das Deduções"].replace(".", "").replace(",", ".")
        ET.SubElement(valores, "ValorIss").text = row["ISS devido"].replace(".", "").replace(",", ".")
        ET.SubElement(valores, "Aliquota").text = row["Alíquota"].replace(",", ".")
        ET.SubElement(servico, "ItemListaServico").text = row["Código do Serviço Prestado na Nota Fiscal"]
        ET.SubElement(servico, "Discriminacao").text = row["Discriminação dos Serviços"]
        ET.SubElement(servico, "CodigoMunicipio").text = row.get("Município Prestação - c d. IBGE", "3550308")

        # Prestador
        prestador = ET.SubElement(inf_nfse, "PrestadorServico")
        id_prestador = ET.SubElement(prestador, "IdentificacaoPrestador")
        ET.SubElement(id_prestador, "Cnpj").text = row["CPF/CNPJ do Prestador"].replace(".", "").replace("/", "").replace("-", "")
        ET.SubElement(id_prestador, "InscricaoMunicipal").text = row["Inscrição Municipal do Prestador"]
        ET.SubElement(prestador, "RazaoSocial").text = row["Razão Social do Prestador"]

        endereco_prestador = ET.SubElement(prestador, "Endereco")
        ET.SubElement(endereco_prestador, "Endereco").text = row["Endereço do Prestador"]
        ET.SubElement(endereco_prestador, "Numero").text = row["Número do Endereço do Prestador"]
        ET.SubElement(endereco_prestador, "Complemento").text = row["Complemento do Endereço do Prestador"]
        ET.SubElement(endereco_prestador, "Bairro").text = row["Bairro do Prestador"]
        ET.SubElement(endereco_prestador, "CodigoMunicipio").text = "3550308"  # São Paulo
        ET.SubElement(endereco_prestador, "Uf").text = row["UF do Prestador"]
        ET.SubElement(endereco_prestador, "Cep").text = row["CEP do Prestador"].replace("-", "")

        # Tomador
        tomador = ET.SubElement(inf_nfse, "TomadorServico")
        id_tomador = ET.SubElement(tomador, "IdentificacaoTomador")
        cpf_cnpj = ET.SubElement(id_tomador, "CpfCnpj")
        ET.SubElement(cpf_cnpj, "Cnpj").text = row["CPF/CNPJ do Tomador"].replace(".", "").replace("/", "").replace("-", "")
        ET.SubElement(tomador, "RazaoSocial").text = row["Razão Social do Tomador"]

        endereco_tomador = ET.SubElement(tomador, "Endereco")
        ET.SubElement(endereco_tomador, "Endereco").text = row["Endereço do Tomador"]
        ET.SubElement(endereco_tomador, "Numero").text = row["Número do Endereço do Tomador"]
        ET.SubElement(endereco_tomador, "Complemento").text = row["Complemento do Endereço do Tomador"]
        ET.SubElement(endereco_tomador, "Bairro").text = row["Bairro do Tomador"]

        # Dicionário de municípios principais (metrópoles brasileiras)
        CIDADES_IBGE = {
            ("São Paulo", "SP"): "3550308",
            ("Rio de Janeiro", "RJ"): "3304557",
            ("Belo Horizonte", "MG"): "3106200",
            ("Brasília", "DF"): "5300108",
            ("Salvador", "BA"): "2927408",
            ("Fortaleza", "CE"): "2304400",
            ("Curitiba", "PR"): "4106902",
            ("Manaus", "AM"): "1302603",
            ("Recife", "PE"): "2611606",
            ("Porto Alegre", "RS"): "4314902",
            ("Belém", "PA"): "1501402",
            ("Goiânia", "GO"): "5208707",
            ("Campinas", "SP"): "3509502",
            ("São Luís", "MA"): "2111300",
            ("Maceió", "AL"): "2704302",
            ("Natal", "RN"): "2408102",
            ("Teresina", "PI"): "2211001",
            ("Campo Grande", "MS"): "5002704",
            ("João Pessoa", "PB"): "2507507",
            ("Aracaju", "SE"): "2800308",
            ("Cuiabá", "MT"): "5103403",
            ("Florianópolis", "SC"): "4205407",
            ("Vitória", "ES"): "3205309",
            ("Macapá", "AP"): "1600303",
            ("Boa Vista", "RR"): "1400100",
            ("Palmas", "TO"): "1721000",
            ("Porto Velho", "RO"): "1100205",
            ("Rio Branco", "AC"): "1200401",
        }

        # Código município do tomador
        cidade = (row["Cidade do Tomador"] or "").strip()
        uf = (row["UF do Tomador"] or "").strip()

        cod_mun_tomador = CIDADES_IBGE.get((cidade, uf), "3550308")  # default SP se não encontrado
        ET.SubElement(endereco_tomador, "CodigoMunicipio").text = cod_mun_tomador
        ET.SubElement(endereco_tomador, "Uf").text = row["UF do Tomador"]
        ET.SubElement(endereco_tomador, "Cep").text = row["CEP do Tomador"].replace("-", "")

    # Gerar XML em memória
    tree = ET.ElementTree(root)
    xml_bytes = io.BytesIO()
    tree.write(xml_bytes, encoding="utf-8", xml_declaration=True)
    return xml_bytes.getvalue()

# ---- APP STREAMLIT ----
st.title("Conversor NFSe CSV → XML (Prefeitura SP)")

st.write("Faça upload do arquivo CSV exportado do portal da Prefeitura de SP para gerar o XML no layout ABRASF.")

uploaded_file = st.file_uploader("Selecione o arquivo CSV", type=["csv"])

if uploaded_file is not None:
    # Ler CSV em DataFrame
    df = pd.read_csv(uploaded_file, sep=";", dtype=str, encoding="latin1")
    st.success("Arquivo CSV carregado com sucesso!")

    # Converter
    xml_bytes = converter_csv_para_xml(df)

    # Download
    st.download_button(
        label="Baixar XML Gerado",
        data=xml_bytes,
        file_name="nfse_sp.xml",
        mime="application/xml"
    )
