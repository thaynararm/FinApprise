$(document).ready(function() {
    $( ".date" ).datepicker({
        showOtherMonths: true,
        selectOtherMonths: true,
        changeMonth: true,
        changeYear: true,
        dateFormat: 'dd/mm/yy',
    });

    $(".date").datepicker("setDate", new Date());
});