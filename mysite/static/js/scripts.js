
// Global variables //
var originalText
var newText
var updatefield
var user

// Function: allow edit to selected field //
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
            $('select[name="contractor"]').prop('disabled', false);
            originalText = $('input[name="contractor"]').val();
            break;
        case 'appointmentDate':
            $('input[name="appointmentDate"]').prop('disabled', false);
            originalText = $('input[name="appointmentDate"]').val();
            break;
        case 'primaryContact':
            $('select[name="primaryContact"]').prop('disabled', false);
            originalText = $('select[name="primaryContact"]').val();
            break;
        case 'secondaryContact':
            $('input[name="secondaryContact"]').prop('disabled', false);
            originalText = $('input[name="secondaryContact"]').val();
            break;
        case 'notes':
            $('input[name="addnotes"]').prop('disabled', false);
            $('input[name="addnotes"]').css("background-color", '#C0DC3B');
            $('input[name="addnotes"]').css("color", 'white');
            $('input[name="addnotes"]').attr("placeholder", "Add notes here...");
            originalText = $('input[name="notes"]').val();
            break;
        default:
            break;
    }

    $("#order-submit").removeClass("hidden");
    $('input[name="submit"]').prop('disabled', false);
}

// Function: save edited order //
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
            newText = $('select[name="contractor"]').val();
            break;
        case 'appointmentDate':
            newText = $('input[name="appointmentDate"]').val();
            break;
        case 'primaryContact':
            newText = $('select[name="primaryContact"]').val();
            break;
        case 'secondaryContact':
            newText = $('input[name="secondaryContact"]').val();
            break;
        case 'secondaryContact':
            newText = $('input[name="secondaryContact"]').val();
            break;
        case 'notes':
            newText = $('input[name="addnotes"]').val();
            break;
        default:
            break;
    }

    $('input[name="csrfmiddlewaretoken"]').prop('disabled', false);
    $('input[name="orderNumber"]').prop('disabled', false);
    $('input[name="orderDescription"]').prop('disabled', false);
    $('input[name="name"]').prop('disabled', false);
    $('input[name="address"]').prop('disabled', false);
    $('select[name="contractor"]').prop('disabled', false);
    $('input[name="appointmentDate"]').prop('disabled', false);
    $('select[name="primaryContact"]').prop('disabled', false);
    $('input[name="secondaryContact"]').prop('disabled', false);
    $('input[name="notes"]').prop('disabled', false);
    $('input[name="dateLastUpdate"]').prop('disabled', false);
    $('input[name="dateCreated"]').prop('disabled', false);

    const d = new Date();
    const today = d.toLocaleString( 'sv' );
    $('input[name="dateLastUpdate"]').val(today);

    if (updatefield == 'notes') {
        updatetext = "";
    } else {
        updatetext = ': ' + originalText + ' -- changed to:';
    }

    username = $("#user-name").text();

    if (originalText != newText) {
        let notesVal =  $('input[name="notes"]').val();
        $('input[name="notes"]').val('{' 
                                + today + ': '
                                + username + ' || '
                                + updatefield + ': '
                                + updatetext
                                + newText + '}' + ' ------||------' 
                                + "\n" + notesVal);
    }

    $("#order-submit").addClass("unhidden");
}


// Function: open addnoteModal and add note //
function addNote() {

    updatefield = 'notes';
    newText = $('#editupdate').val();

    $("#order-submit").removeClass("hidden");
    $('input[name="submit"]').prop('disabled', false);

    $('input[name="csrfmiddlewaretoken"]').prop('disabled', false);
    $('input[name="orderNumber"]').prop('disabled', false);
    $('input[name="orderDescription"]').prop('disabled', false);
    $('input[name="name"]').prop('disabled', false);
    $('input[name="address"]').prop('disabled', false);
    $('select[name="contractor"]').prop('disabled', false);
    $('input[name="appointmentDate"]').prop('disabled', false);
    $('input[name="primaryContact"]').prop('disabled', false);
    $('input[name="secondaryContact"]').prop('disabled', false);
    $('input[name="notes"]').prop('disabled', false);
    $('input[name="dateLastUpdate"]').prop('disabled', false);
    $('input[name="dateCreated"]').prop('disabled', false);

    const d = new Date();
    const today = d.toLocaleString( 'sv' );
    $('input[name="dateLastUpdate"]').val(today);

    let notesVal =  $('input[name="notes"]').val();
    $('input[name="notes"]').val('{' 
                            + today + ' || '
                            + newText + '}' + ' -||-' 
                            + "\n" + notesVal);

    $('input[name="notes"]').prop('disabled', true);
}

// Function: set order for search view az //
function orderAz() {

    $('input[name="searchorder"]').val('az');
    
}

// Function: set order for search view za //
function orderZa() {

    $('input[name="searchorder"]').val('za');
    
}