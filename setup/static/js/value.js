$(document).ready(function(){

    // Faz o cálculo do valor total
    function updateTotalValue() {
        var unitary_value = parseFloat($('#unitary_value').val().replace(/\./g, '').replace(',', '.')) || 0;
        var quantity = parseFloat($('#quantity').val().replace(/\./g, '').replace(',', '.')) || 0;
    
        if (isNaN(unitary_value) || isNaN(quantity)) {
            // Lidar com valores não numéricos, se necessário
        } else {
            var multiply = unitary_value * quantity;
            var formattedValue = multiply.toFixed(2).replace('.', ',');
    
            // Remover a máscara antes de atualizar o total_value
            $('#total_value').unmask().val(formattedValue);
    
            // Reaplicar a máscara
            $('#total_value').mask('000.000.000.000.000,00', {reverse: true});
        }
    };
    
    // Aplcia a máscara de valor
    $('.value').mask('000.000.000.000.000,00', {reverse: true});
    $('.value').on('input', function(e){
        var value = $(this).val().replace(/\D/g, '');

        if(value.length > 2){
            // Remove os zeros à esquerda
            value = value.replace(/^0+/, '');

            // Adiciona a vírgula e os centavos
            var cents = value.slice(-2);
            var integerPart = value.slice(0, -2) || '0';

            // Adiciona os pontos para separar as milhas
            var formattedValue = '';
            for (var i = integerPart.length; i > 0; i -= 3) {
                formattedValue = '.' + integerPart.slice(Math.max(0, i - 3), i) + formattedValue;
            }
            formattedValue = formattedValue.slice(1); // Remove o ponto inicial, se houver

            $(this).val(formattedValue + ',' + cents);
        } else if(value.length === 2){
            // Adiciona '0,' seguido dos centavos
            $(this).val('0,' + value);
        } else if(value.length === 1){
            // Adiciona '0,0' seguido do valor digitado
            $(this).val('0,0' + value);
        }

        updateTotalValue();
    });

        // Adiciona eventos de input nos campos unitary_value e quantity
        $('#unitary_value, #quantity').on('input', function() {
            // Chama a função para atualizar o campo total_value
            updateTotalValue();
        });

        // Chama a função inicialmente para garantir que o total_value seja definido corretamente
        updateTotalValue();
});