"use strict";




function notify(mes){
    (mes).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    alert('$'+mes);
}


