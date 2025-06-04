```markdown
# 📄 Documentação L1 — Stress App

## 📌 Visão Geral
O **Stress App** é uma ferramenta que permite desenvolvedores testarem a resiliência e capacidade de resposta de suas aplicações por meio de requisições simultâneas controladas. Ele ajuda a identificar gargalos e limitações de infraestrutura de forma prática e automatizada.

## 🎯 Objetivo
Oferecer um mecanismo simples para que usuários possam submeter suas aplicações a cenários de carga e identificar o comportamento sob alta demanda, facilitando a avaliação de desempenho e estabilidade.

## ⚙️ Funcionalidades

### 1️⃣ Enviar múltiplas requisições GET para um endpoint

- **O que permite?**
  Permite que o usuário dispare múltiplas requisições HTTP GET para um endpoint de sua aplicação, simulando carga.

- **Como usar?**
  Realize uma requisição HTTP `GET` para o endpoint `/send-request` do Stress App, informando:
  - O endpoint da aplicação alvo.
  - A quantidade de requisições desejadas.

- **Requisitos / Parâmetros:**
  - `endPoint` (string, obrigatório) → endereço completo da aplicação alvo.
  - `request` (inteiro, obrigatório) → número de requisições a serem disparadas.

- **Endpoint:**
  - `/send-request`

- **Retorno:**
  ```json
  {
    "message": "Dispatched <quantidade> requests",
    "metric_id": "<id_da_metrica>"
  }
  ```
  - `message`: Confirmação de que as requisições foram enviadas.
  - `metric_id`: Identificador único para consultar as métricas da requisição. Este ID permite consultar informações sobre a requisição (quantidade de requisições, sucessos, erros) através do endpoint `/metrics/:id`.

### 2️⃣ Enviar múltiplos arquivos via requisições POST para um endpoint

- **O que permite?**
  Permite que o usuário envie múltiplos arquivos (atualmente, um arquivo `fake-pdf.pdf` fixo) via requisições HTTP POST para um endpoint.

- **Como usar?**
  Realize uma requisição HTTP `POST` para o endpoint `/send-file` do Stress App, informando:
  - O endpoint da aplicação alvo.
  - A quantidade de requisições desejadas.
  - O token de autorização.

- **Requisitos / Parâmetros:**
  - `endPoint` (string, obrigatório) → endereço completo da aplicação alvo.
  - `requestQTD` (inteiro, opcional, default: 2) → número de requisições a serem disparadas.
  - `authorization` (string, obrigatório) → Token de autorização para o envio do arquivo.

- **Endpoint:**
  - `/send-file`

- **Retorno:**
  ```json
  {
    "message": "Dispatched <quantidade> upload files",
    "outro": [<mensagens_de_retorno>],
    "metric_id": "<id_da_metrica>"
  }
  ```
  - `message`: Confirmação de que os arquivos foram enviados.
  - `outro`:  Array contendo mensagens de retorno de cada requisição. Caso a requisição não retorne uma mensagem, o valor default é `"Não encontrou nenhuma mensagem para essa requisição"`. Em caso de erro, o valor retornado é `"error"`.
  - `metric_id`: Identificador único para consultar as métricas da requisição. Este ID permite consultar informações sobre a requisição (quantidade de requisições, sucessos, erros) através do endpoint `/metrics/:id`.

### 3️⃣ Consultar métricas de uma requisição

- **O que permite?**
  Permite que o usuário consulte as métricas de uma requisição específica, utilizando o `metric_id` retornado ao enviar as requisições.

- **Como usar?**
  Realize uma requisição HTTP `GET` para o endpoint `/metrics/:id` do Stress App, substituindo `:id` pelo `metric_id` da requisição desejada.

- **Requisitos / Parâmetros:**
  - `id` (string, obrigatório) → `metric_id` da requisição.

- **Endpoint:**
  - `/metrics/:id`

- **Retorno:**
  ```json
  {
    "id": "<id_da_metrica>",
    "type": "send-request" ou "send-file",
    "quantity": <quantidade_de_requisicoes>,
    "success": <quantidade_de_sucesso>,
    "errors": <quantidade_de_erros>,
    "timestamp": "<data_e_hora_da_requisicao>"
  }
  ```
  - `id`: `metric_id` da requisição.
  - `type`: Tipo da requisição (`send-request` ou `send-file`).
  - `quantity`: Quantidade total de requisições enviadas.
  - `success`: Quantidade de requisições bem-sucedidas.
  - `errors`: Quantidade de requisições com erro.
  - `timestamp`: Data e hora em que a requisição foi enviada.

## 🔄 Fluxo de Funcionamento

### 📌 Ação: Realizar teste de carga (GET) na aplicação alvo.

**1.** Usuário define o endpoint da aplicação e a quantidade de requisições.
**2.** Usuário realiza uma requisição `GET` para:
```
GET /send-request
```
**Body (JSON):**
```json
{
  "endPoint": "https://minhaaplicacao.com/api/teste",
  "request": 4000
}
```
**3.** O Stress App processa a quantidade solicitada de requisições GET para o endpoint informado.
**4.** Retorna resposta:
```json
{
  "message": "Dispatched 4000 requests",
  "metric_id": "a1b2c3d4e5f6"
}
```

### 📌 Ação: Realizar teste de carga (POST com arquivo) na aplicação alvo.

**1.** Usuário define o endpoint da aplicação, a quantidade de requisições e o token de autorização.
**2.** Usuário realiza uma requisição `POST` para:
```
POST /send-file
```
**Body (JSON):**
```json
{
  "endPoint": "https://minhaaplicacao.com/api/upload",
  "requestQTD": 100,
  "authorization": "Bearer <token>"
}
```
**3.** O Stress App processa a quantidade solicitada de requisições POST com o arquivo para o endpoint informado.
**4.** Retorna resposta:
```json
{
  "message": "Dispatched 100 upload files",
  "outro": ["upload realizado com sucesso", ...],
  "metric_id": "f6e5d4c3b2a1"
}
```

### 📌 Ação: Consultar métricas do teste.

**1.** Usuário utiliza o `metric_id` retornado após o envio das requisições.
**2.** Usuário realiza uma requisição `GET` para:
```
GET /metrics/a1b2c3d4e5f6
```
**3.** O Stress App retorna as métricas da requisição correspondente ao `metric_id`.
**4.** Retorna resposta:
```json
{
  "id": "a1b2c3d4e5f6",
  "type": "send-request",
  "quantity": 4000,
  "success": 3900,
  "errors": 100,
  "timestamp": "2024-10-27T10:00:00.000Z"
}
```

## 📊 Impacto no Projeto

1. Permite identificar falhas e limitações sob alta carga.
2. Auxilia no planejamento de escalabilidade e melhorias de infraestrutura.
3. Oferece uma ferramenta rápida para simular cenários críticos de forma controlada.
4. Facilita a validação de endpoints críticos em ambientes de homologação e produção.
5. Permite o acompanhamento das requisições através das métricas.

## 🔌 Integrações

Nenhuma integração externa implementada atualmente.

## 💡 Melhorias Futuras (Roadmap)

1.  Permitir configuração de diferentes tipos de requisições (GET, POST, PUT, DELETE) com payloads customizáveis.
2.  Adicionar níveis de logs para rastrear o status das execuções.
3.  Implementar log rotativo para evitar arquivos de log muito grandes.
4.  Adicionar autenticação para controle de acesso.
5.  Permitir o upload de diferentes arquivos para o teste de envio de arquivos.
6.  Implementar dashboards para visualização das métricas.

## ⚠️ Pontos de Risco e Sugestões

1.  **Ausência de tratamento de erros:** Não há tratamento específico para cenários de erro nas requisições, como timeouts ou falhas de conexão.
2.  **Vulnerabilidade a ataques:** Sem autenticação ou mecanismos de proteção, o sistema pode ser utilizado para realizar ataques de negação de serviço (DoS).
3.  **Falta de flexibilidade:** O sistema não permite configurar o tipo de requisição (GET, POST, etc.) ou adicionar headers personalizados.
4.  **Escalabilidade limitada:** A arquitetura atual, com métricas armazenadas em memória, pode não ser escalável para grandes volumes de requisições ou múltiplos usuários.
5.  **Necessidade de limpeza manual dos logs:** Os logs são armazenados em arquivos que podem crescer indefinidamente, exigindo intervenção manual para limpeza e organização.
```