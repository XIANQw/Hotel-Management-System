$(function(){
   $("#hrefCreerMeu").click(showFormCreerMeu);
   $("#formCreerMeu").on("submit", check);
   $(".modify").click(function() {
                    str = $(this).text()=="Modifier"?"Confirmer":"Modifier";
                    $(this).text(str);   // Le boutton change entre modifier et confirmer
                    $(this).parent().siblings("td:eq(0)").each(function() {
                        obj_text = $(this).find("input:text");
                        if(!obj_text.length)
                            $(this).html("<input type='text' class='form control' value='"+$(this).text()+"'>");
                        else
                            $(this).html(obj_text.val());
                    });
                });

});
function showFormCreerMeu() {
    $("#formCreerMeu").css({ "display": "block"});
}
function hideFormCreerMeu() {
    $("#formCreerMeu").css({"display": "none"});
}
function check(){
    if($("#nomMeuble").val()){
        return true;
    }
    else{
        alert("nom ne peut pas etre vide");
        return false;
    }
}