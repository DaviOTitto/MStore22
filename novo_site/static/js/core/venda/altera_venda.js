// Envia número do botão pesquisar clicado
let valor = 0;
function setaDadosModal(valor) {
  document.getElementById('btn_importar_produto').value = valor;
}  

// Recupera dados da venda já realizada e insere nos campos
$(document).ready(function () {
  $("#id_main-Cod_Cli_VEN").val("{{ cliente.pk }}");
  $("#id_main-Cod_Cli_VEN_aux").val("{{ cliente.full_name }}");    
  let itens_venda = '{{ itens_venda | safe }}';
  let k = 0;
  for(let i = 0; i <= itens_venda.length; i++) {
    $(`#id_product-${i}-Cod_Pro_ITEVEN`).val(itens_venda[k]);
    $(`#id_product-${i}-Cod_Pro_ITEVEN_aux`).val(itens_venda[k+1]);
    k += 2;
  }
}); 

// Realiza ações após apertar o botão adicionar item
$(document).ready(function () {
  $("#add-item").click(function (ev) { 
    ev.preventDefault();
    var count = ($('#order').children().length);
    var tmplMarkup = $("#item-order").html();
    var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
    $("div#order").append(compiledTmpl);        
    $('#id_product-TOTAL_FORMS').attr('value', count + 1);
  });
});

// Adiciona filtro por nome no modal cliente
function adicionarCliente() {
  $("#search-box-cliente").keypress(function(evento) { // Com leitura direta na tela
      if(evento.which == 13) {
          evento.preventDefault();
          let index = $(this).parent().index();
          let nth = "#tabela-cliente td:nth-child("+(index+1).toString()+")";
          let valor = $(this).val().toUpperCase();
          $("#tabela-cliente tbody tr").show();
          $(nth).each(function(){
              if($(this).text().toUpperCase().indexOf(valor) < 0){
                  $(this).parent().hide();
              }
          });
      }
  });
  $("#search-box-cliente").blur(function() {
      $(this).val("");
  });

// Envia informação selecionado no modal para os campos de cliente    
  $("#btn_importar_cliente").click(function() {
    if($("input[type='radio'].radioBtnClassCliente").is(':checked')) {
      var cliente = $("input[type='radio'].radioBtnClassCliente:checked").val();
      $("#id_main-Cod_Cli_VEN").val(cliente.split('-')[0]);
      $("#id_main-Cod_Cli_VEN_aux").val(cliente.split('-')[1]);
    }
  });
  $("input[type='radio'].radioBtnClassCliente").attr('checked', false);
  $("#tabela-cliente tbody tr").show();    
}

function adicionarItem(id) {
  $("#search-box-produto").keypress(function(evento) { // Com leitura direta na tela
      if(evento.which == 13) {
          evento.preventDefault();
          let index = $(this).parent().index();
          let nth = "#tabela-produto td:nth-child("+(index+1).toString()+")";
          let valor = $(this).val().toUpperCase();
          $("#tabela-produto tbody tr").show();
          $(nth).each(function(){
              if($(this).text().toUpperCase().indexOf(valor) < 0){
                  $(this).parent().hide();
              }
          });
      }
  });
  $("#search-box-produto").blur(function() {
      $(this).val("");
  });

 let idProduto = Number(id.split('-')[1]);
 setaDadosModal(idProduto);
  $(`#btn_importar_produto`).click(function() {
    if(document.getElementById('btn_importar_produto').value == idProduto) {
      if($("input[type='radio'].radioBtnClassProduto").is(':checked')) {
        var produto = $("input[type='radio'].radioBtnClassProduto:checked").val();
        $(`#id_product-${idProduto}-Cod_Pro_ITEVEN`).val(produto.split('-')[0]);
        $(`#id_product-${idProduto}-Cod_Pro_ITEVEN_aux`).val(produto.split('-')[1]);
        $(`#id_product-${idProduto}-unitario_ite`).val(itemven.split('-')[2]);
      }
    }
  });
  $("input[type='radio'].radioBtnClassProduto").attr('checked', false);
  $("#tabela-produto tbody tr").show();
}

function excluirItem(id) {
  let itens_venda = '{{ itens_venda | safe }}';
  let itensBD = '{{ qtd_itens | safe }}';
  let totalForms = document.querySelector('#id_product-TOTAL_FORMS');
  let btnID = Number(id.split('-')[1]);
  if(btnID === 0) {
    alert('Não é possível excluir o primeiro item!');
  } else if(btnID < totalForms.value) {
    tam = btnID;
    while(tam+1 < totalForms.value) {
      document.querySelector(`#id_product-${tam}-Cod_Pro_ITEVEN`).value = document.querySelector(`#id_product-${tam+1}-Cod_Pro_ITEVEN`).value;
      document.querySelector(`#id_product-${tam}-Cod_Pro_ITEVEN_aux`).value = document.querySelector(`#id_product-${tam+1}-Cod_Pro_ITEVEN_aux`).value;          
      document.querySelector(`#id_product-${tam}-Quant_ITEVEN`).value = document.querySelector(`#id_product-${tam+1}-Quant_ITEVEN`).value;
      document.querySelector(`#id_product-${tam}-Valor_Unit_ITEVEN`).value = document.querySelector(`#id_product-${tam+1}-Valor_Unit_ITEVEN`).value;
      tam++;
    }
    totalForms.value -= 1;
    document.querySelector(`#item-${totalForms.value}`).remove(); 
  } else {
    totalForms.value -= 1;
    document.querySelector(`#item-${totalForms.value}`).remove();       
  }
} 

