
// Function: open edit modal //
function editOrder(orderfield) {
    let orderfieldString = "#id_" + orderfield;
    $('#editModalLabel').html("Edit " + orderfield + " field");

    $('input[name="orderDescription"]').prop('disabled', false);
}

//Function: replace the appropriate field in portal.html with the text from #question and add a note //
function saveEdit() {
    let orderfield = $('#editModalLabel').html();
    
    switch(orderfield) {
        case 'Edit orderDescription field':
            if (!(/^[a-z A-Z?:,.-]+$/.test(this.editupdate.value)) ||this.editupdate.value.length < 1) {
                alert('Please enter text only, with no special characters .');
                this.editupdate.focus();
                return false;
            } else {
                console.log(this.editupdate.value);
                $('input[name="orderDescription"]').val(this.editupdate.value);
            }
            break;
        default:
            break;
    }
}
