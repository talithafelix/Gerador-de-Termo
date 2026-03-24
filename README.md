
# Gerador de Termo de Responsabilidade

Este projeto foi desenvolvido para automatizar a geração de termos de responsabilidade utilizados no processo de entrega de laptops, dockstations e acessórios aos funcionários.

Atualmente, o processo de criação desses termos costuma ser feito manualmente ou via mala direta no Word, o que pode ser demorado e suscetível a erros. Este programa facilita o fluxo ao permitir que o usuário informe apenas os dados necessários, gerando automaticamente um documento preenchido a partir de um modelo padronizado.

## Objetivo do Projeto

Quando um equipamento é entregue a um funcionário, é obrigatório emitir um termo de responsabilidade contendo informações sobre os itens recebidos. Embora o conteúdo do termo seja sempre o mesmo, alguns campos variam a cada entrega, como:

- Modelo do laptop
- Serial do laptop
- Modelo e serial da dockstation (quando houver)
- Nome do funcionário
- Indicação de entrega de mochila
- Indicação de entrega de dockstation

Este programa foi criado para substituir processos manuais e agilizar a emissão desse documento.

## Funcionamento

Para gerar o termo, o programa utiliza um arquivo modelo do Microsoft Word chamado **Modelo_termo.docx**, que deve estar localizado na mesma pasta do executável, assim como o arquivo de exemplo neste repositório.

Dentro do documento existem campos específicos que são preenchidos automaticamente. É fortemente recomendado que esses campos sejam criados como **Campos de Texto (Formulário Herdado)** através da guia *Desenvolvedor* no Word. Caso sejam utilizados campos simples, as *runs* internas do documento *.docx* podem causar falhas no preenchimento.

## Campos Utilizados no Modelo

O documento deve conter exatamente os seguintes campos:

```
[Modelo_L]
[Laptop_Serial]
[Modelo_D]
[Dock_Serial]
[Nome]
[check_m]
[check_d]
[Modelo_D2]
```

### Descrição dos Campos

| Campo | Descrição |
|-------|-----------|
| **[Modelo_L]** | Modelo do laptop entregue ao funcionário |
| **[Laptop_Serial]** | Número de série do laptop |
| **[Modelo_D]** | Modelo da dockstation (campo opcional) |
| **[Dock_Serial]** | Serial da dockstation (obrigatório caso o item seja entregue) |
| **[Nome]** | Nome do funcionário que receberá os itens |
| **[check_m]** | Campo marcado com "X" caso o funcionário receba mochila |
| **[check_d]** | Campo marcado com "X" caso uma dockstation seja entregue |
| **[Modelo_D2]** | Nome da dockstation para outra área do documento que exige formatação diferente |

O campo **[Modelo_D2]** existe para casos específicos de formulários que exigem o modelo da dockstation em mais de um local, mas com formatações diferentes. Ele pode ser removido ou renomeado conforme a necessidade do formulário utilizado.

## Adaptação para Outros Formulários

Caso outra equipe ou empresa deseje utilizar o código, basta modificar o modelo do documento (Modelo_termo.docx) e ajustar os nomes dos campos conforme necessário. A lógica permanece padrão e facilmente adaptável.

## Possíveis Melhorias Futuras

- [ ] Transformar os campos de **Modelo do Laptop** e **Modelo da Dockstation** em listas selecionáveis baseadas em opções pré-definidas.
- [ ] Permitir o cadastro, edição e exclusão de novos modelos diretamente pela interface do aplicativo.
- [ ] Criar um histórico local de todos os termos já gerados, possibilitando consulta e reimpressão.
