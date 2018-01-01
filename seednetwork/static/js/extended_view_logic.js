/*
The code below hides the extended view form when the more info 
checkbox is unchecked
It also filters the choices available to the user for the 
subcategory field based on the grain selected
*/
var sel;
var origOptions=[];

if (document.getElementById('id_more_info') != null) {
    hide_extended_grain_form();
    document.getElementById('id_more_info').onchange=hide_extended_grain_form;

//'save' original list so that filter_choices operates on 
//original list instead of a filtered list

    sel  = document.getElementById("id_grain_subcategory");
    for (i = 0; i < sel.length; i++) {
        origOptions.push(sel[i]);
    }
    filter_choices();
    document.getElementById('id_crop_type').onchange=filter_choices;
}

function hide_extended_grain_form(){
    if (document.getElementById('id_more_info').checked) {
        document.getElementById('extended_form').hidden = false;
    } else {
        document.getElementById('extended_form').hidden = true;
    }
}

function filter_choices(){
//There is a js global variable called original_subcategory
    var subcategoryList = document.getElementById("id_grain_subcategory");
    var grain = document.getElementById("id_crop_type").value;
//There is a mismatch in the capitalization, so strip out the first letter
    var grain_lc = grain.toLowerCase().concat(':');
    var newList = [];
    var default_index = 0;
    var j = 0;

    while(subcategoryList.options.length) {
        subcategoryList.remove(0);
    }

    for (i = 0; i < origOptions.length; i++) {
        if (grain=='-'||origOptions[i].text.toLowerCase().includes(grain_lc)||i==0) {
	    newList.push(origOptions[i]);
            // The default selection is a rudimentary contains check with the original grain subcategory
            // This is currently sufficient with the present subcategories, but would break with a new  "sweet winter" 
            if (typeof original_subcategory !== 'undefined'  && origOptions[i].text.toLowerCase().includes(original_subcategory)) {
                default_index=j; 
            }
            j++;
        }
    }

    for (i = 0; i < newList.length; i++) {
        subcategoryList.add(newList[i]);
    }

    subcategoryList.selectedIndex = default_index;
}  
	

