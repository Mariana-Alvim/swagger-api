# API Timezone

Este projeto consiste numa API Flask-RESTful com Swagger desenvolvida em Python, num container Docker.

<br>

**Objetivo:** Este serviço possibilita obter o horário local conforme o fuso horário do CEP fornecido.
<br>

---
### Execução

Para executar este microsserviço, basta gerar a imagem a partir do Dockerfile executando o comando **1** no mesmo diretório do projeto, e então, processar a imagem por meio do comando **2**.

1. `docker-compose build`
<br>
2. `docker-compose up`
<br>

---
### Métodos
A API Timezone possui dois métodos, o GET e o POST. Por meio do método GET é possível verificar se a rota está funcionado. E, o método POST possibilita receber o horário local conforme o CEP informado na requisição (vide exemplo a seguir). Os endpoints dos métodos estão listados na tabela.   
<br>

---
### Acesso
Esta API pode ser acessada na porta `9000`. 
<br>

---
### Endpoints
<div align="center">

|Endpoint|Método|
|---|---|
|/|GET|
|/main|POST|

</div>
<br>
A documentação Swagger está diponível por meio do endpoint `/docs`.

<br>

---
### Exemplos de uso
Exemplo de requisição do horário local de um CEP (05508010) referente ao fuso horário de Brasília (GTM-3).

<div align="center">
<video 
src="https://user-images.githubusercontent.com/104532249/225744372-421f375c-c874-43c7-b67b-3d9b85fdede5.mp4" 
style="width:85%" muted autoplay loop playsinline>
</div>
</video>

<br>

No segundo exemplo de aplicação abaixo, foi enviada uma requisição para obter o horário local de acordo com o fuso horário de Fernando de Noronha (GMT-2), requisitando o CEP 53990-000.  

<br>

<div align="center">
<video 
src="https://user-images.githubusercontent.com/104532249/225744391-d0ce3f0f-2c6b-4593-a0ab-f15ede1c2f72.mp4" 
style="width:85%" muted autoplay loop playsinline>
</video></div>



&nbsp;

---
### REQUERIMENTOS
A API Timezone está integrada à API PyCEPCorreios para consulta de endereço a partir do CEP. Ademais, a API possui integração às bibliotecas subcitadas:
* GeoPy: localiza as coordenadas de um endereço
* TimezoneFinder: busca o fuso horário local conforme as coordenadas do usuário

&nbsp;

---
### A API foi desenvolvida por meio do tamplate disponibilizado pelo Patrick.  
* Link de acesso ao template: https://github.com/PatrickLdA/swagger_api

&nbsp;

---
