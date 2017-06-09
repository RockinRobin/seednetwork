if (document.URL.indexOf("search")>=0 || document.URL.indexOf("member")>=0) {
    hide_table_actions();
}

function hide_table_actions(){

   var table = document.querySelector( '.results');
   var cellIndex = table.rows[0].cells.length - 1;  // index for last column
   var num_columns = table.rows[0].cells.length;
   for (i = 0; i<table.rows.length; i++){
        table.rows[i].cells[cellIndex % num_columns].style.display = 'none';
    }

}
