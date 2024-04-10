// Envia número do botão pesquisar clicado
//total = parseFloat(0);
function setaDadosModal(valor) {
  document.getElementById('btn_importar_produto').value = valor;
} 
var x  = parseInt(1)

$(document).ready(function () {
  var totalProdutos = parseInt('{{total_produtos}}');
  var barraProgresso = $('progress');
  
  $.ajax({
    url: '/api/produtos',
    xhr: function () {
      var xhr = new window.XMLHttpRequest();
      
      xhr.onprogress = function (event) {
        if (event.lengthComputable) {
          var progresso = event.loaded / event.total * totalProdutos;
          barraProgresso.attr('value', progresso);
        }
      };
      
      return xhr;
    }
  })
  .done(function () {
    barraProgresso.attr('value', totalProdutos);
    alert('Todos os produtos foram processados!');
    });
  });
  $("<div/>", {id:"divBtn-0","class":"form-group"}).appendTo("#item-0");  
  $("<button/>", {id:"id_product-0-btnModalProduto", "class":"btn btn-primary fa fa-search", "data-toggle":"modal", "data-target":"#ModalListaProdutos", title:"Clique para abrir a grade de pesquisa de produtos"}).appendTo("#divBtn-0");  
  $("<button/>", {id:"id_product-0-btnExcluirProduto", "class":"btn btn-danger fa fa-trash", title:"Clique para excluir o produto selecionado"}).appendTo("#divBtn-0");  
// Realiza ações após apertar o botão adicionar item
// Adiciona novas linhas de produtos (valor > 0)


  $("#add-item").click(function (ev) { 
    ev.preventDefault();
    var count = ($('#order').children().length);
    var tmplMarkup = $("#item-order").html();
    console.log($("#item-order").html())
    var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
    $("div#order").append(compiledTmpl);
    $("<div/>", {id:`divBtn-${count}`,"class":"form-group"}).appendTo(`#item-${count}`);  
    $("<button/>", {id:`id_product-${count}-btnModalProduto`, "class":"btn btn-primary fa fa-search", "data-toggle":"modal", "data-target":"#ModalListaProdutos", title:"Clique para abrir a grade de pesquisa de produtos"}).appendTo(`#divBtn-${count}`);  
    $("<button/>", {id:`id_product-${count}-btnExcluirProduto`, "class":"btn btn-danger fa fa-trash", title:"Clique para excluir o produto selecionado"}).appendTo(`#divBtn-${count}`); 
    $('#id_product-TOTAL_FORMS').attr('value', count + 1);
  });
});



$(document).ready(function() {
    $('.pagination a').click(function(event) {
        event.preventDefault();

        $.ajax({
            type: 'GET',
            url: '/venda/produto_list/',
            success: function(data) {
                $('#tabela-produto tbody').html(data);
            }
        });
    });
});

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
      let cliente = $("input[type='radio'].radioBtnClassCliente:checked").val();
      $("#id_main-cliente_ven_aux_cod").val(cliente.split('-')[0]);
      $("#id_main-cliente_ven_aux_nome").val(cliente.split('-')[1]);
      $("#id_main-cliente_ven_aux_cpf").val(cliente.split('-')[2]);
      $("#id_main-cliente_ven_aux_nasc").val(cliente.split('-')[3]);
  }
    $("input[type='radio'].radioBtnClassCliente").attr('checked', false);
    $("#tabela-cliente tbody tr").show();  
  });
}

  $("#btnModalCliente").click(function(evento) {
    evento.preventDefault();
    adicionarCliente();
  });

/*$(document).ready(function () {
// Botoes da primeira linha, inicial (valor = 0)
  $("<div/>", {id:"divBtn-0","class":"form_aux"}).appendTo("#data_aux-0");
  var count = 0;
  while(count < x)
  {
    $("div#order").append(compiledTmpl);
    $("<div/>", {id:`divBtn-${count}`,"class":"form-group"}).appendTo(`#data_aux-${count}`); 
  }
*/




function adicionarEspecie() {
  $("#search-box-especie").keypress(function(evento) { // Com leitura direta na tela
      if(evento.which == 13) { // enter
          evento.preventDefault();
          let index = $(this).parent().index();
          let nth = "#tabela-especie td:nth-child("+(index+1).toString()+")";
          let valor = $(this).val().toUpperCase();
          
          $("#tabela-especie tbody tr").show();
          $(nth).each(function(){
              if($(this).text().toUpperCase().indexOf(valor) < 0){
                  $(this).parent().hide();
              }
          });
      }
  });
  $("#search-box-especie").blur(function() {
      $(this).val("");
  });

// Envia informação selecionado no modal para os campos de formaPag    
  $("#btn_importar_especie").click(function() {
    if($("input[type='radio'].radioBtnClassEspecie").is(':checked')) {
      let especie = $("input[type='radio'].radioBtnClassEspecie:checked").val();
      $("#id_main-formapag_ven_aux_cod").val(especie.split('-')[0]);
      $("#id_main-formapag_ven_aux_nome").val(especie.split('-')[1]);
      x = especie.split('-')[2];
    }
    $("input[type='radio'].radioBtnClassEspecie").attr('checked', false);
    $("#tabela-formaPag tbody tr").show();  
  });
}


$("#btnModalEspecie").click(function(evento) {
  evento.preventDefault();
  adicionarEspecie();
});

$("#btn_efetivar").click(function() {
  $("#id_main-formapag_ven_aux_cod").val(56);
  $("#id_main-formapag_ven_aux_nome").val('7 DIAS BOLETO');
});
function parcelar(evento)
{}
//--------------------------------------------------------------------------------------------- ITENS
function adicionarItem(id) {
  $("#search-box-produto").focus();  
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

  setaDadosModal(id);
  $(`#btn_importar_produto`).click(function() {
   
    if(document.getElementById('btn_importar_produto').value == id) {
      if($("input[type='radio'].radioBtnClassProduto").is(':checked')) {
        
        var produto = $("input[type='radio'].radioBtnClassProduto:checked").val();
        $(`#id_product-${id}-produto_ite_aux_cod`).val(produto.split('-')[0]);
        $(`#id_product-${id}-produto_ite_aux_nome`).val(produto.split('-')[1]); 
        $(`#id_product-${id}-produto_ite_aux_valor`).val(produto.split('-')[2]);
        var unitario =$(`#id_product-${id}-produto_ite_aux_valor`).val();
        var quantidade = $(`#id_product-${id}-produto_ite_aux_quant`).val();
        somartudo(id);
        //unitario = parseFloat(unitario);
        //quantidade = parseInt(quantidade);       
        //console.log(total);  
        //total = unitario*quantidade +total;
        //console.log(total);
        //$(`#totalParcial`).val(total); 

          //$(`id_product - `)
            /*.keyup(function() {    
            if(preco == null)
            {
            console.log('passou')
            preco = parseFloat(preco);
            total = parseFloat(total);  
            var total = total  +   $(`#id_product-${id}-unitario_ite`).val(produto);
             console.log(total)  
            $(`#id_totalparcial`).val(total);
            }
          })*/

        
        } 

    }

  });
  
  $("input[type='radio'].radioBtnClassProduto").attr('checked', false);
  $("#tabela-produto tbody tr").show();
  somartudo(id);
}

function somartudo(id){
 if(id==0)
 {
        var total = parseFloat(0);
        var unitario =$(`#id_product-${id}-produto_ite_aux_valor`).val();
        var quantidade = $(`#id_product-${id}-produto_ite_aux_quant`).val();
        unitario = parseFloat(unitario);
        quantidade = parseFloat(quantidade);       
        console.log(total);  
        total = unitario*quantidade +total;
        console.log(total);
        $(`#totalParcial`).val(total); 
 }

  else if(id>0){
    var tam = parseInt(0);

    total = 0;
    total = parseFloat(0);
     for (tam >= 0 ; tam< id+1; tam++) {
        var unitario =$(`#id_product-${tam}-produto_ite_aux_valor`).val();
        var quantidade = $(`#id_product-${tam}-produto_ite_aux_quant`).val();
        unitario = parseFloat(unitario);
        quantidade = parseFloat(quantidade);       
        console.log(total);  
        total = unitario*quantidade +total;
        console.log(total);
        $(`#totalParcial`).val(total);
         
     }
  }
}


function excluirItem(id) {
  let totalForms = document.querySelector('#id_product-TOTAL_FORMS');
  var unitario =$(`#id_product-${id}-produto_ite_aux_valor`).val();
  var quantidade = $(`#id_product-${id}-produto_ite_aux_quant`).val();
  unitario = parseFloat(unitario)
  quantidade= parseFloat(quantidade)
  if(id == 0) {
    alert('Não é possível excluir o primeiro item!');
  } else if(id+1 < totalForms.value) {
    tam = id;
    while(tam+1 < totalForms.value) {
      document.querySelector(`#id_product-${tam}-produto_ite_aux_cod`).value = document.querySelector(`#id_product-${tam+1}-produto_ite_aux_cod`).value;
      document.querySelector(`#id_product-${tam}-produto_ite_aux_nome`).value = document.querySelector(`#id_product-${tam+1}-produto_ite_aux_nome`).value;          
      document.querySelector(`#id_product-${tam}-produto_ite_aux_valor`).value = document.querySelector(`#id_product-${tam+1}-produto_ite_aux_valor`).value;
      document.querySelector(`#id_product-${tam}-produto_ite_aux_quant`).value = document.querySelector(`#id_product-${tam+1}-quantidade_ite`).value;
      
      tam++;
    }
    totalForms.value -= 1;
    document.querySelector(`#item-${totalForms.value}`).remove(); 
        var total =  $(`#totalParcial`).val();
        total =parseFloat(total)           
        console.log(total);  
        total = -unitario*quantidade +total;
        console.log(total);
        $(`#totalParcial`).val(total); 
  } else {
    totalForms.value -= 1;
    document.querySelector(`#item-${totalForms.value}`).remove();       
        var total =  $(`#totalParcial`).val();
        total = parseFloat(total)      
        console.log(total);  
        total = -unitario*quantidade +total;
        console.log(total);
        $(`#totalParcial`).val(total); 
  }
} 

$("#order").on('click', '.btn', function(evento) {
    evento.preventDefault();
    if(this.id.split("-")[2] === 'btnModalProduto') {
        adicionarItem(Number(this.id.split("-")[1]));
    } else {
        excluirItem(Number(this.id.split("-")[1]));
    }
});

/*function TOTAL_GERAL() {
  let = totalp = $(`#totalParcial`).val();
  let =  acrescimo = $(`#id_main-acrescimo-ven`).val();
  let = desconto = $(`#id_main-desconto-ven `).val();
  let totalF = float(0);
  totalF = totalp + acrescimo - desconto 
  $(`#totalFinal`).val(totalF)
}
*/
