import pandas as pd

# Ler arquivo CSV
data = pd.read_csv('input.csv')

# Deletando coluna
data.drop('AUTH_METHOD', inplace=True, axis=1)
data.drop('ACCOUNT_NAME', inplace=True, axis=1)
data.drop('ACCOUNT_EMAIL', inplace=True, axis=1)
data.drop('ACCOUNT_ORGANIZATION_UID', inplace=True, axis=1)
data.drop('ACCOUNT_ORGANIZATION_NAME', inplace=True, axis=1)
data.drop('ACCOUNT_TAGS', inplace=True, axis=1)
data.drop('FINDING_UID', inplace=True, axis=1)
data.drop('PROVIDER', inplace=True, axis=1)
data.drop('CHECK_ID', inplace=True, axis=1)
data.drop('CHECK_TYPE', inplace=True, axis=1)
data.drop('STATUS_EXTENDED', inplace=True, axis=1)
data.drop('MUTED', inplace=True, axis=1)
data.drop('SERVICE_NAME', inplace=True, axis=1)
data.drop('RESOURCE_TYPE', inplace=True, axis=1)
data.drop('RESOURCE_UID', inplace=True, axis=1)
data.drop('RELATED_URL', inplace=True, axis=1)
data.drop('RESOURCE_DETAILS', inplace=True, axis=1)
data.drop('RESOURCE_TAGS', inplace=True, axis=1)
data.drop('REGION', inplace=True, axis=1)
data.drop('REMEDIATION_RECOMMENDATION_URL', inplace=True, axis=1)
data.drop('REMEDIATION_CODE_CLI', inplace=True, axis=1)
data.drop('REMEDIATION_CODE_OTHER', inplace=True, axis=1)
data.drop('COMPLIANCE', inplace=True, axis=1)
data.drop('CATEGORIES', inplace=True, axis=1)
data.drop('DEPENDS_ON', inplace=True, axis=1)
data.drop('RELATED_TO', inplace=True, axis=1)
data.drop('NOTES', inplace=True, axis=1)
data.drop('PROWLER_VERSION', inplace=True, axis=1)
data.drop('REMEDIATION_CODE_NATIVEIAC', inplace=True, axis=1)
data.drop('REMEDIATION_CODE_TERRAFORM', inplace=True, axis=1)
data.drop('SUBSERVICE_NAME', inplace=True, axis=1)
data.drop('PARTITION', inplace=True, axis=1)

# Alterando valor de linhas
data['SEVERITY'] = data['SEVERITY'].replace({'low': 'Low'})
data['SEVERITY'] = data['SEVERITY'].replace({'medium': 'Medium'})
data['SEVERITY'] = data['SEVERITY'].replace({'high': 'High'})
data['SEVERITY'] = data['SEVERITY'].replace({'critical': 'Critical'})

# Deletando linhas Status PASS
data.drop(data[data['STATUS'] == 'PASS'].index, inplace = True)
data.drop('STATUS', inplace=True, axis=1)

# Deletando linhas Severity Low
data.drop(data[data['SEVERITY'] == 'Low'].index, inplace = True)

# Deletando linhas com headers
data.drop(data[data['SEVERITY'] == 'SEVERITY'].index, inplace = True)

# Deletando linhas com BigQuery Crypt
data.drop(data[data['REMEDIATION_RECOMMENDATION_TEXT'] == 'Encrypting datasets with Cloud KMS Customer-Managed Keys (CMKs) will allow for a more granular control over data encryption/decryption process.'].index, inplace = True)

# Deletando linhas com BigQuery Crypt
data.drop(data[data['REMEDIATION_RECOMMENDATION_TEXT'] == 'Encrypting tables with Cloud KMS Customer-Managed Keys (CMKs) will allow for a more granular control over data encryption/decryption process.'].index, inplace = True)

# Renomeando headers
#data.replace(to_replace =",", value = " ", inplace = True) Executado antes na mão
#data.replace(to_replace =";", value = ",", inplace = True) Executado antes na mão
data = data.rename(columns={data.columns[0]: 'Date', data.columns[1]: 'References', data.columns[2]: 'Title', data.columns[3]: 'Severity', data.columns[4]: 'Url',  data.columns[5]: 'Description', data.columns[6]: 'Impact', data.columns[7]: 'Mitigation'})
#TIMESTAMP,ACCOUNT_UID,CHECK_TITLE,SEVERITY,RESOURCE_NAME,DESCRIPTION,RISK,REMEDIATION_RECOMMENDATION_TEXT

# Função para incrementar o título
title_counts = {}
def increment_title(title):
    if title not in title_counts:
        title_counts[title] = 1
    else:
        title_counts[title] += 1
        title = f"{title} ({title_counts[title]})"
    return title

# Aplicar a função de incremento à coluna 'Title'
data['Title'] = data['Title'].apply(increment_title)

# Salvar o DataFrame modificado em um novo arquivo CSV
data.to_csv('output.csv', index=False)
data.info()
