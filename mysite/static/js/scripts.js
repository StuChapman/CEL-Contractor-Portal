
// Global variables //
var originalText
var newText
var updatefield
var user
var dateYear
var expandvar

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
            console.log(originalText);
            break;
        case 'appointmentDate':
            $('input[name="appointmentDate"]').prop('disabled', false);
            originalText = $('input[name="appointmentDate"]').val();
            break;
        case 'primaryContact':
            $('select[name="primaryContact"]').prop('disabled', false);
            originalText = $('select[name="primaryContact"]').val();
            console.log(originalText);
            break;
        case 'secondaryContact':
            $('select[name="secondaryContact"]').prop('disabled', false);
            originalText = $('select[name="secondaryContact"]').val();
            console.log(originalText);
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
            if (!(/^[a-z A-Z?:',.-]+$/.test(newText)) || newText.length < 10) {
                alert('Please enter an OrderDescription of at least 10 characters, in text only.');
                $('input[name="orderDescription"]').focus();
                return false;
            }
            break;
        case 'name':
            newText = $('input[name="name"]').val();
            if (!(/^[a-z A-Z?:',.-]+$/.test(newText)) || newText.length < 1) {
                alert('Please enter a Name, in text only');
                $('input[name="name"]').focus();
                return false;
            }
            break;
        case 'address':
            newText = $('input[name="address"]').val();
            if (!(/^[0-9 a-z A-Z?:',.-]+$/.test(newText)) || newText.length  < 1) {
                alert('Please enter an Address, in text and numerals only');
                $('input[name="address"]').focus();
                return false;
            }
            break;
        case 'contractor':
            newText = $('select[name="contractor"]').val();
            break;
        case 'appointmentDate':
            newText = $('input[name="appointmentDate"]').val();
            if (!(/^[0-9 A-Z?:-]+$/.test(newText)) || newText.length  < 1) {
                alert('Appointment Date should be in the format: YYYY-MM-DD HH:MM:SS');
                $('input[name="address"]').focus();
                return false;
            }
            break;
        case 'primaryContact':
            newText = $('select[name="primaryContact"]').val();
            break;
        case 'secondaryContact':
            newText = $('select[name="secondaryContact"]').val();
            break;
        case 'notes':
            newText = $('input[name="addnotes"]').val();
            if (!(/^[0-9 a-z A-Z?:'@,.-]+$/.test(newText)) || newText.length < 10) {
                alert('Please enter Notes, of at least 10 characters, in text and numerals only');
                $('input[name="addnotes"]').focus();
                return false;
            }
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
        updatetext = originalText + ' -- changed to: ';
    }

    username = $("#user-name").text();

    if (originalText != newText) {
        let notesVal =  $('input[name="notes"]').val();
        $('input[name="notes"]').val('|| ' 
                                + today + ': '
                                + username + ' - '
                                + updatefield + ': '
                                + updatetext
                                + newText + ' ||' + ' -------X-------' 
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

    // populate year select //
    let thisyear = new Date().getFullYear();
    $('#id_yearpicker').empty();
    $('#id_yearpicker').append($('<option>', {value: '',  text: 'select year...'}));
    for (var i = thisyear -1; i < thisyear +2; i++) {
        $('#id_yearpicker').append($('<option>', {
            value: i,
            text: i
        }));
    }

    // populate month select //
    $('#id_monthpicker').empty();
    $('#id_monthpicker').append($('<option>', {value: '',  text: 'select month...'}));
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

    // populate hour select //
    $('#id_hourpicker').empty();
    $('#id_hourpicker').append($('<option>', {value: '',  text: 'select hour ...'}));
    for (var i = 1; i < 10; i++) {
        $('#id_hourpicker').append($('<option>', {
            value: '0' + i,
            text: '0' + i
        }));
    }
    for (var i = 10; i < 25; i++) {
        $('#id_hourpicker').append($('<option>', {
            value: i,
            text: i
        }));
    }

    // populate minute select //
    $('#id_minutepicker').empty();
    $('#id_minutepicker').append($('<option>', {value: '',  text: 'select minutes ...'}));
    for (var i = 0; i < 10; i++) {
        if (i % 10 === 0) {
            $('#id_minutepicker').append($('<option>', {
                value: '0' + i,
                text: '0' + i
            }));
        }
    }
    for (var i = 10; i < 51; i++) {
        if (i % 10 === 0) {
            $('#id_minutepicker').append($('<option>', {
                value: i,
                text: i
            }));
        }
    }
}


// Function: populate the appointment date field //
function appointmentDate() {

    let id_yearpicker = $("#id_yearpicker").val();
    if (!(/^[0-9 a-z A-Z?:',.-]+$/.test(id_yearpicker)) || id_yearpicker.length < 1) {
        alert('Please select a year');
        $('input[name="id_yearpicker"]').focus();
        return false;
    }

    let id_monthpicker = $("#id_monthpicker").val();
    if (!(/^[0-9 a-z A-Z?:',.-]+$/.test(id_monthpicker)) || id_monthpicker.length < 1) {
        alert('Please select a month');
        $('input[name="id_monthpicker"]').focus();
        return false;
    }

    let id_daypicker = $("#id_daypicker").val();
    if (!(/^[0-9 a-z A-Z?:',.-]+$/.test(id_daypicker)) || id_daypicker.length < 1) {
        alert('Please select a day');
        $('input[name="id_daypicker"]').focus();
        return false;
    }

    let id_hourpicker = $("#id_hourpicker").val();
    if (!(/^[0-9 a-z A-Z?:',.-]+$/.test(id_hourpicker)) || id_hourpicker.length < 1) {
        alert('Please select an hour');
        $('input[name="id_hourpicker"]').focus();
        return false;
    }

    let id_minutepicker = $("#id_minutepicker").val();
    if (!(/^[0-9 a-z A-Z?:',.-]+$/.test(id_minutepicker)) || id_minutepicker.length < 1) {
        alert('Please select minutes');
        $('input[name="id_minutepicker"]').focus();
        return false;
    }

    var apptdate = $("#id_yearpicker").val() + '-' +
                        $("#id_monthpicker").val() + '-' +
                            $('#id_daypicker').val() + ' ' +
                                $("#id_hourpicker").val() + ':' +
                                    $('#id_minutepicker').val() + ':00';
    $('input[name="appointmentDate"]').val(apptdate);

    $('#dateModal').modal('hide');
    $('body').removeClass('modal-open');
    $('body').css('padding-right', '0px');
    $('.modal-backdrop').remove();

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

// Function: validate the search text //
function validateSearch() {

    searchString = $('input[name="search_string"]').val();

    if (!searchString.length < 1) {
        if (!(/^[0-9 a-z A-Z?:'@,.-]+$/.test(searchString)) || searchString.length < 3) {
            alert('Please enter text to Search, in text and numerals only');
            $('input[name="search_string"]').focus();
            return false;
        }
    }    
}

// Function: expend the notes textarea //
function expandNotes() {

    if (expandvar == 'contract') {
        expandvar = 'expand';
        $('#id_notes').css('height','10vh');
    } else {
        expandvar = 'contract';
        $('#id_notes').css('height','30vh');
    }
    $('#expandnotes').html(expandvar).button("refresh");
}
