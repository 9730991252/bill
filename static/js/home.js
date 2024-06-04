
function check_number(){
    mobile=document.getElementById('number').value;

    if (mobile.length <= 9 ){
    document.getElementById('number').style.borderColor ='green';return false;
  }
    if (mobile.length >= 11 ){
    alert('only 10 digit number ')
  }
    if (mobile.length == 10 ){
        document.getElementById('number').style.borderColor ='';return true;
       
  }
}
function check_pin(){
    pin=document.getElementById('pin').value;

    if (pin.length <= 3 ){
    document.getElementById('pin').style.borderColor ='green';return false;
  }
    if (pin.length >= 5 ){
    alert('only 4 digit number Secret Pin')
  }
    if (pin.length == 4 ){
        document.getElementById('pin').style.borderColor ='';return true;
       
  }
}


