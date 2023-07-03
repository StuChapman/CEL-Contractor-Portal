//Function: use emailjs account to email a question from the help? button on the header //
function sendEmail() {

    if (!(/^\S+@\S+\.\S+$/.test(this.email.value))) {
        alert('Please enter a valid email address.');
        this.email.focus();
        return;
    }

    if (!(/^[a-z A-Z?:,.-]+$/.test(this.question.value)) ||this.question.value.length < 10) {
        alert('Please enter a question of at least 10 characters, and no special characters .');
        this.question.focus();
        return false;
    }
    
    emailjs.init("user_37585cYmkMNZRiOobd27i");
    
    var template_params = {
    "from_email": "From: " + this.email.value,
    "question": "Question: " + this.question.value
    };
    
    var service_id = "continuous_engagement";
    var template_id = "template_6DMLrcJu";

    emailjs.send(service_id, template_id, template_params);
    
    alert('Email sent succesfully.');

}

function passwordReset() {

    if (!(/^\S+@\S+\.\S+$/.test(this.passwordemail.value))) {
        alert('Please enter a valid email address.');
        this.passwordemail.focus();
        return;
    }

    if (!(/^[a-z A-Z?:,.-]+$/.test(this.passwordmessage.value)) ||this.passwordmessage.value.length < 10) {
        alert('Please enter a question of at least 10 characters, and no special characters .');
        this.passwordmessage.focus();
        return false;
    }
    
    emailjs.init("user_37585cYmkMNZRiOobd27i");
    
    var template_params = {
    "from_email": "From: " + this.passwordemail.value,
    "question": "Question: " + this.passwordmessage.value
    };
    
    var service_id = "continuous_engagement";
    var template_id = "template_6DMLrcJu";

    emailjs.send(service_id, template_id, template_params);
    
    alert('Email sent succesfully.');

}

// Function: navigate to Continuous Engagament Ltd homepage //
function goCELHome() {
    window.location.replace('https://continuous-engagement.co.uk');
    }

// Function: navigate to Curo Ltd homepage //
function goCuroHome() {
    window.location.replace('https://www.curo-group.co.uk/');
    }