
// Function: open edit modal //
function editOrder(orderfield) {
    let orderfieldString = "#id_" + orderfield;
    $('#editModalLabel').html("Edit " + orderfield + " field");

    $('input[name="orderDescription"]').prop('disabled', false);
    $('#saveeditbtn').removeClass("hidden");
}

//Function: replace the appropriate field in portal.html with the text from #question and add a note //
function saveEdit() {
    $('input[name="orderDescription"]').prop('disabled', true);
    $('#saveeditbtn').addClass("hidden");
}
