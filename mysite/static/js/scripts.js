
// Function: open edit modal //
function editOrder(orderfield) {
    $('input[name="csrfmiddlewaretoken"]').prop('disabled', false);

    switch(orderfield) {
        case 'orderDescription':
            $('input[name="orderDescription"]').prop('disabled', false);
            $('input[name="dateLastUpdate"]').text(today);
            break;
        case 'name':
            $('input[name="name"]').prop('disabled', false);
            break;
        case 'address':
            $('input[name="address"]').prop('disabled', false);
            break;
        case 'contractor':
            $('input[name="contractor"]').prop('disabled', false);
            break;
        case 'appointmentDate':
            $('input[name="appointmentDate"]').prop('disabled', false);
            break;
        case 'primaryContact':
            $('input[name="primaryContact"]').prop('disabled', false);
            break;
        case 'secondaryContact':
            $('input[name="secondaryContact"]').prop('disabled', false);
            break;
        default:
            break;
    }



    $('input[name="submit"]').prop('disabled', false);
}

// Function: open edit modal //
function saveOrder() {
    $('input[name="csrfmiddlewaretoken"]').prop('disabled', false);
    $('input[name="orderNumber"]').prop('disabled', false);
    $('input[name="orderDescription"]').prop('disabled', false);
    $('input[name="name"]').prop('disabled', false);
    $('input[name="address"]').prop('disabled', false);
    $('input[name="contractor"]').prop('disabled', false);
    $('input[name="appointmentDate"]').prop('disabled', false);
    $('input[name="primaryContact"]').prop('disabled', false);
    $('input[name="secondaryContact"]').prop('disabled', false);
    $('input[name="notes"]').prop('disabled', false);
    $('input[name="dateLastUpdate"]').prop('disabled', false);
    $('input[name="dateCreated"]').prop('disabled', false);

    let today = new Date().toISOString().slice(0, 19)
    $('input[name="dateLastUpdate"]').val(today);
}