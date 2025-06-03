```markdown
# 📄 Documentação L1 — Stress App

## 📌 Visão Geral
O **Stress App** é uma ferramenta que permite desenvolvedores testarem a resiliência e capacidade de resposta de suas aplicações por meio de requisições simultâneas controladas. Ele ajuda a identificar gargalos e limitações de infraestrutura de forma prática e automatizada.

## 🎯 Objetivo
Oferecer um mecanismo simples para que usuários possam submeter suas aplicações a cenários de carga e identificar o comportamento sob alta demanda, facilitando a avaliação de desempenho e estabilidade.

## ⚙️ Funcionalidades

### 1️⃣ Testar a capacidade de resposta de uma aplicação via requisições múltiplas (GET)

- **O que permite?**
  Permite que o usuário dispare múltiplas requisições HTTP `GET` para um endpoint de sua aplicação, simulando carga.

- **Como usar?**
  Realize uma requisição HTTP `GET` para o endpoint `/send-request` do Stress App, informando:
  - A URL da aplicação alvo (endPoint).
  - A quantidade de requisições desejadas (request).

- **Requisitos / Parâmetros:**
  - `endPoint` (string, body) → endereço completo da aplicação alvo.
  - `request` (inteiro, body) → número de requisições a serem disparadas.

- **Endpoint:** `/send-request`

### 2️⃣ Testar a capacidade de resposta de uma aplicação via requisições múltiplas (POST com arquivo)

- **O que permite?**
  Permite que o usuário dispare múltiplas requisições HTTP `POST` para um endpoint de sua aplicação, simulando o upload de um arquivo, simulando carga.

- **Como usar?**
  Realize uma requisição HTTP `POST` para o endpoint `/send-file` do Stress App, informando:
  - A URL da aplicação alvo (endPoint).
  - A quantidade de requisições desejadas (requestQTD).
  - Um token de autorização (authorization).

- **Requisitos / Parâmetros:**
  - `endPoint` (string, body) → endereço completo da aplicação alvo.
  - `requestQTD` (inteiro, body) → número de requisições a serem disparadas.
  - `authorization` (string, body) → token de autorização.

- **Endpoint:** `/send-file`

**Observação:** O sistema utiliza o arquivo `fake-pdf.pdf` para simular o upload.

### 3️⃣ Consultar o status de um teste de carga

- **O que permite?**
  Permite que o usuário consulte o status de um teste de carga realizado previamente, utilizando o `metric_id` retornado.

- **Como usar?**
  Realize uma requisição HTTP `GET` para o endpoint `/metrics/:id`, substituindo `:id` pelo `metric_id` do teste que deseja consultar.

- **Requisitos / Parâmetros:**
    - `id` (string, via URL) → `metric_id` do teste de carga.

- **Endpoint:** `/metrics/:id`

## 🔄 Fluxo de Funcionamento

### 📌 Ação: Realizar teste de carga (GET) na aplicação alvo.

**1.** Usuário define o endereço da aplicação e a quantidade de requisições.
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

**3.** O Stress App processa a quantidade solicitada de requisições para a URL informada.
**4.** Retorna resposta:

```json
{
  "message": "Dispatched 4000 requests",
  "metric_id": "unique_id"
}
```

**Identificadores:**

*   `metric_id`: Identificador único do teste de carga realizado. Pode ser utilizado para consultar o status do teste posteriormente através do endpoint `/metrics/:id`.

### 📌 Ação: Realizar teste de carga (POST com arquivo) na aplicação alvo.

**1.** Usuário define o endereço da aplicação, a quantidade de requisições e o token de autorização.
**2.** Usuário realiza uma requisição `POST` para:

```
POST /send-file
```

**Body (JSON):**
```json
{
  "endPoint": "https://minhaaplicacao.com/api/teste",
  "requestQTD": 4000,
  "authorization": "Bearer <token>"
}
```

**3.** O Stress App processa a quantidade solicitada de requisições, enviando o arquivo `fake-pdf.pdf` para a URL informada.
**4.** Retorna resposta:

```json
{
  "message": "Dispatched 4000 upload files",
  "outro": [],
  "metric_id": "unique_id"
}
```

**Identificadores:**

*   `metric_id`: Identificador único do teste de carga realizado. Pode ser utilizado para consultar o status do teste posteriormente através do endpoint `/metrics/:id`.

### 📌 Ação: Consultar Status do Teste de Carga

**1.** O usuário utiliza o `metric_id` recebido após a execução do teste.
**2.** O usuário realiza uma requisição `GET` para:

```
GET /metrics/{metric_id}
```

**Exemplo:**

```
GET /metrics/a1b2c3d4e5f67890
```

**3.** O Stress App retorna as informações sobre o teste, como quantidade de requisições realizadas, sucesso e erros.

**Resposta (JSON):**

```json
{
    "id": "a1b2c3d4e5f67890",
    "type": "send-request",
    "quantity": 4000,
    "success": 3900,
    "errors": 100,
    "timestamp": "2024-10-27T10:00:00.000Z"
}
```

**Importante:**
Atualmente, o Stress App **retorna informações básicas de sucesso e erro**, e armazena as métricas em memória.
O servidor está rodando na porta **3333**.

## 📊 Impacto no Projeto

1. Permite identificar falhas e limitações sob alta carga.
2. Auxilia no planejamento de escalabilidade e melhorias de infraestrutura.
3. Oferece uma ferramenta rápida para simular cenários críticos de forma controlada.
4. Facilita a validação de endpoints críticos em ambientes de homologação e produção.

## 🔌 Integrações

Nenhuma integração externa implementada atualmente.

## 💡 Melhorias Futuras (Roadmap)

1. Implementar serviço de métricas, exibindo:
   - Tempo médio de resposta.
   - Quantidade de falhas.
   - Percentual de sucesso.
2. Permitir configuração de diferentes tipos de requisições (GET, POST, PUT, DELETE).
3. Adicionar níveis de logs para rastrear o status das execuções.
4. Implementar log rotativo para evitar arquivos de log muito grandes.
5. Adicionar autenticação para controle de acesso (já existente para `/send-file`).
6. Permitir o upload de diferentes arquivos para o endpoint `/send-file`.
7. Validar os schemas de entrada das requisições.

## ⚠️ Pontos de Risco e Sugestões

1.  **Falta de métricas detalhadas:** A ausência de métricas como tempo de resposta, taxa de erros e utilização de recursos dificulta a identificação precisa de gargalos e a avaliação do impacto do teste de carga. **Sugestão:** Implementar a coleta e exibição dessas métricas.
2.  **Suporte limitado a tipos de requisição:** Atualmente, o sistema suporta apenas requisições POST (para envio de arquivos) e GET (para requisições simples). A falta de suporte a outros métodos HTTP (PUT, DELETE) limita a cobertura dos testes. **Sugestão:** Adicionar suporte a diferentes tipos de requisição.
3.  **Capacidade de configuração da carga:** Atualmente, a ferramenta apenas permite definir a quantidade de requisições. Não é possível configurar o tempo entre requisições, a duração do teste, ou outras formas de simular diferentes padrões de carga. **Sugestão:** Adicionar opções de configuração de tempo e duração dos testes.
4. **Armazenamento de métricas em memória:** As métricas são armazenadas em memória, o que significa que são perdidas quando o servidor é reiniciado. **Sugestão:** Implementar um banco de dados para persistir as métricas.
5. **Inconsistência no método HTTP para `/send-request`:** O endpoint `/send-request` utiliza o método GET, mas recebe os parâmetros `endPoint` e `request` no corpo da requisição. Isso não é uma prática comum e pode causar confusão. **Sugestão:** Alterar o método para POST ou utilizar query parameters para receber os parâmetros no endpoint `/send-request`.
6. **Falta de controle sobre o arquivo de upload:** O endpoint `/send-file` sempre envia o mesmo arquivo (`fake-pdf.pdf`). Isso limita a flexibilidade dos testes, pois não é possível simular o upload de diferentes tipos de arquivos ou variar o tamanho dos arquivos. **Sugestão:** Permitir que o usuário especifique o arquivo a ser enviado no endpoint `/send-file`.
```