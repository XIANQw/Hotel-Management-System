$(function(){
   $("#ModeLogin").click(ModeSignIn);
   $("#ModeSignUp").click(ModeSignUp);
   $('#ModeCreation').click(creationRessource);
   $('#ModeModification').click(modifyRessource);
   $('#ModeCancellation').click(deleteRessource);
   $('#gotoModifyCompte').click(gotoModifyCompte);
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

function creationRessource() {
  $('#createRessource').css('display','block');
  $('#modifyRessource').css('display','none');
  $('#deleteRessource').css('display','none');
  affiche("");
}

function modifyRessource() {
  $('#createRessource').css('display','none');
  $('#modifyRessource').css('display','block');
  $('#deleteRessource').css('display','none');
  affiche("");
}

function deleteRessource() {
  $('#createRessource').css('display','none');
  $('#modifyRessource').css('display','none');
  $('#deleteRessource').css('display','block');
  affiche("");
}

function gotoModifyCompte() {
    $('#modifyCompte').css('display', 'block');
    $('#createDemande').css('display', 'none');
    $('#infoDemande').css('display', 'none');
    affiche("");
}

function gotoCreateDemande() {
    $('#modifyCompte').css('display', 'none');
    $('#createDemande').css('display', 'block');
    $('#infoDemande').css('display', 'block');
    affiche("");
}

function affiche(chaine){
    $('#alert').html(chaine);
}