var pass = document.getElementById("password");
var btn_show = document.getElementById("show");
pass.oninput = function(){
  if(pass.value.length > 0){
    pass.classList.remove('pass');
    pass.classList.add('pass_show');
  }
  else{
    pass.classList.remove('pass_show');
    pass.classList.add('pass');
  }
}
btn_show.onclick = function(){
  if (pass.type == "password"){
    pass.type = "text";
    btn_show.value = "hide";
  }
  else{
    pass.type = "password";
    btn_show.value = "show";
  }
}
