
// Global variables //
var originalText
var newText
var updatefield

// Function: open edit modal //
function editOrder(orderfield) {

    updatefield = orderfield;
    $('input[name="csrfmiddlewaretoken"]').prop('disabled', false);

    switch(orderfield) {
        case 'orderDescription':
            $('input[name="orderDescription"]').prop('disabled', false);
            originalText = $('input[name="orderDescription"]').val();
            break;
        case 'name':
            $('input[name="name"]').prop('disabled', false);
            originalText = $('input[name="name"]').val();
            break;
        case 'address':
            $('input[name="address"]').prop('disabled', false);
            originalText = $('input[name="address"]').val();
            break;
        case 'contractor':
            $('input[name="contractor"]').prop('disabled', false);
            originalText = $('input[name="contractor"]').val();
            break;
        case 'appointmentDate':
            $('input[name="appointmentDate"]').prop('disabled', false);
            originalText = $('input[name="appointmentDate"]').val();
            break;
        case 'primaryContact':
            $('input[name="primaryContact"]').prop('disabled', false);
            originalText = $('input[name="primaryContact"]').val();
            break;
        case 'secondaryContact':
            $('input[name="secondaryContact"]').prop('disabled', false);
            originalText = $('input[name="secondaryContact"]').val();
            break;
        default:
            break;
    }

    $("#order-submit").removeClass("hidden");
    $('input[name="submit"]').prop('disabled', false);
}

// Function: open edit modal //
function saveOrder() {

    switch(updatefield) {
        case 'orderDescription':
            newText = $('input[name="orderDescription"]').val();
            break;
        case 'name':
            newText = $('input[name="name"]').val();
            break;
        case 'address':
            newText = $('input[name="address"]').val();
            break;
        case 'contractor':
            newText = $('input[name="contractor"]').val();
            break;
        case 'appointmentDate':
            newText = $('input[name="appointmentDate"]').val();
            break;
        case 'primaryContact':
            newText = $('input[name="primaryContact"]').val();
            break;
        case 'secondaryContact':
            newText = $('input[name="secondaryContact"]').val();
            break;
        default:
            break;
    }

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

    const d = new Date();
    const today = d.toLocaleString( 'sv' );
    $('input[name="dateLastUpdate"]').val(today);
    
    if (originalText != newText) {
        let notesVal =  $('input[name="notes"]').val();
        $('input[name="notes"]').val('{' 
                                + today + ' || '
                                + updatefield + ': '
                                + originalText 
                                + ' -- changed to: ' 
                                + newText + '}' + '|||' 
                                + "\n" + notesVal);
    }

    $("#order-submit").addClass("unhidden");
}