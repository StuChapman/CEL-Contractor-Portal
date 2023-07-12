
// Global variables //
var originalText
var newText
var updatefield
var user
var dateYear

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
            $('select[name="secondaryContact"]').prop('disabled', false);
            originalText = $('select[name="secondaryContact"]').val();
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
            newText = $('select[name="secondaryContact"]').val();
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
    $('select[name="secondaryContact"]').prop('disabled', false);
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
    $('select[name="primaryContact"]').prop('disabled', false);
    $('select[name="secondaryContact"]').prop('disabled', false);
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

// Function: populate the date modal //
function populateDateModal() {

    editOrder('appointmentDate');
    $('select[name="id_yearpicker"]').prop('disabled', false);

    // populate year select //
    let thisyear = new Date().getFullYear()
    for (var i = thisyear -1; i < thisyear +2; i++) {
        $('#id_yearpicker').append($('<option>', {
            value: i,
            text: i
        }));
    }

    // populate month select //
        $('#id_monthpicker').append($('<option>', {value: '01',  text: 'Jan'}));
        $('#id_monthpicker').append($('<option>', {value: '02',  text: 'Feb'}));
        $('#id_monthpicker').append($('<option>', {value: '03',  text: 'Mar'}));
        $('#id_monthpicker').append($('<option>', {value: '04',  text: 'Apr'}));
        $('#id_monthpicker').append($('<option>', {value: '05',  text: 'May'}));
        $('#id_monthpicker').append($('<option>', {value: '06',  text: 'Jun'}));
        $('#id_monthpicker').append($('<option>', {value: '07',  text: 'Jul'}));
        $('#id_monthpicker').append($('<option>', {value: '08',  text: 'Aug'}));
        $('#id_monthpicker').append($('<option>', {value: '09',  text: 'Sep'}));
        $('#id_monthpicker').append($('<option>', {value: '10',  text: 'Oct'}));
        $('#id_monthpicker').append($('<option>', {value: '11',  text: 'Nov'}));
        $('#id_monthpicker').append($('<option>', {value: '12',  text: 'Dec'}));

}


// Function: populate the appointment date field //
function appointmentDate() {

    var apptdate = $("#id_yearpicker").val() + '-' +
                        $("#id_monthpicker").val() + '-' +
                            $('#id_daypicker').val() + ' 00:00:00';
    $('input[name="appointmentDate"]').val(apptdate);

}

$(document).ready(function () {

    $("#id_yearpicker").change(function (event) {
        dateYear =  $(this).val();
    });
});


$(document).ready(function () {

    $("#id_monthpicker").change(function (event) {
        // populate day select //
        $('#id_daypicker').empty()
        $('#id_daypicker').append($('<option>', {value: '',  text: 'select day...'}));
        if ($('#id_monthpicker').val() == '01' || 
                $('#id_monthpicker').val() == '03' || 
                    $('#id_monthpicker').val() == '05'  || 
                        $('#id_monthpicker').val() == '07'  || 
                            $('#id_monthpicker').val() == '08'  || 
                                $('#id_monthpicker').val() == '09'  || 
                                    $('#id_monthpicker').val() == '10'  || 
                                        $('#id_monthpicker').val() == '12' ){
            for (var i = 1; i < 10; i++) {
                $('#id_daypicker').append($('<option>', {
                    value: '0' + i,
                    text: '0' + i
                }));
            }
            for (var i = 10; i < 32; i++) {
                $('#id_daypicker').append($('<option>', {
                    value: i,
                    text: i
                }));
            }
        }
        if ($('#id_monthpicker').val() == '02' ){
            for (var i = 1; i < 10; i++) {
                $('#id_daypicker').append($('<option>', {
                    value: '0' + i,
                    text: '0' + i
                }));
            }
            for (var i = 10; i < 29; i++) {
                $('#id_daypicker').append($('<option>', {
                    value: i,
                    text: i
                }));
            }
            var leapyear = $('#id_yearpicker').val();
            if ((leapyear & 3) == 0 && ((leapyear % 25) != 0 || (leapyear & 15) == 0)){
                console.log(leapyear);
                $('#id_daypicker').append($('<option>', {value: '29',  text: '29'}));
            }
        }
        if ($('#id_monthpicker').val() == '04' || 
                $('#id_monthpicker').val() == '06' || 
                    $('#id_monthpicker').val() == '09'  || 
                        $('#id_monthpicker').val() == '11' ){
                            for (var i = 1; i < 10; i++) {
                                $('#id_daypicker').append($('<option>', {
                                    value: '0' + i,
                                    text: '0' + i
                                }));
                            }
                            for (var i = 10; i < 31; i++) {
                                $('#id_daypicker').append($('<option>', {
                                    value: i,
                                    text: i
                                }));
                            }
        }
    });
});