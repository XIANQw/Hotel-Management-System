$(function(){
   $("#ModeLogin").click(ModeSignIn);
   $("#ModeSignUp").click(ModeSignUp);
   $('#ModeCreation').click(gotoCreationRessource);
   $('#quitCreation').click(quitCreationRessource);
   $('#gotoCreateDemande').click(gotoCreateDemande);
})

function ModeSignIn(){
  $('#zoneLogin').css('display','block');
  $('#zoneSignUp').css('display','none');
}


function ModeSignUp(){
  $('#zoneSignUp').css('display','block');
  $('#zoneLogin').css('display','none');
}

function gotoCreationRessource() {
  $('#createRessource').css('display','block');
}
function quitCreationRessource() {
  $('#createRessource').css('display','none');
}


function gotoCreateDemande() {
    $('#modifyCompte').css('display', 'none');
    $('#createDemande').css('display', 'block');
    $('#infoDemande').css('display', 'block');
    affiche("Creez une nouvelle demande");
}

function affiche(chaine){
    $('#alert').html(chaine);
}