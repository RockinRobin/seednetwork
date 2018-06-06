if (document.getElementById('id_country_code')  != null) {
    hide_domestic_fields();
    document.getElementById('id_country_code').onchange=hide_domestic_fields;
}

function hide_domestic_fields(){
    if (document.getElementById('id_country_code').value != "US") {
        document.getElementById('id_street_line').parentElement.parentElement.hidden = true;
        document.getElementById('id_city').parentElement.parentElement.hidden = true;
        document.getElementById('id_state').parentElement.parentElement.hidden = true;
        document.getElementById('id_zipcode').parentElement.parentElement.hidden = true;
        document.getElementById('id_street_address_is_public').parentElement.parentElement.hidden = true;
    } else {
        document.getElementById('id_street_line').parentElement.parentElement.hidden = false;
        document.getElementById('id_city').parentElement.parentElement.hidden = false;
        document.getElementById('id_state').parentElement.parentElement.hidden = false;
        document.getElementById('id_zipcode').parentElement.parentElement.hidden = false;
        document.getElementById('id_street_address_is_public').parentElement.parentElement.hidden = false;
    }
}
