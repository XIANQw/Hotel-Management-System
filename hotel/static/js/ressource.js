$(function(){
   $("#hrefCreerMeu").click(showFormCreerMeu);
   $("#formCreerMeu").on("submit", check);

});
function showFormCreerMeu() {
    $("#formCreerMeu").css({ "display": "block"});
}
function hideFormCreerMeu() {
    $("#formCreerMeu").css({"display": "none"});
}
function check(){
    if($("#nomMeuble").val()&&$("#status").val()){
        return true;
    }
    else{
        alert("nom et status ne peuvenet pas etre vide");
        return false;
    }
}
