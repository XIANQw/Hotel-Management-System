$(function(){
   $("#ModeLogin").click(ModeSignIn);
   $("#ModeSignUp").click(ModeSignUp);
   $('#ModeCreation').click(gotoCreationRessource);
   $('#quitCreation').click(quitCreationRessource);
   $('#gotoCreateDemande').click(gotoCreateDemande);
   $('#gotoRes').click(gotoRes);
   $('#gotoUsers').click(gotoUser);
   $('#gotoCreateDemande').click(gotoCreateDemande);
   $('#gotoInfoDemande').click(gotoInfoDemande);
   $('#gotoDemendes').click(goDemandes);
})


// modify gestionnaire.html
function ModeSignIn(){
  $('#zoneLogin').css('display','block');
  $('#zoneSignUp').css('display','none');
}


function ModeSignUp(){
  $('#zoneSignUp').css('display','block');
  $('#zoneLogin').css('display','none');
}

function goDemandes(){
  $('#zoneRessource').css('display','none');
  $('#infoClient').css('display','none');
  $('#zoneDemande').css('display','block');
}


function gotoCreationRessource() {
  $('#createRessource').css('display','block');
}
function quitCreationRessource() {
  $('#createRessource').css('display','none');
}

function gotoRes() {
  $('#zoneRessource').css('display','block');
  $('#infoClient').css('display','none');
  $('#zoneDemande').css('display','none');
}
function gotoUser() {
  $('#zoneRessource').css('display','none');
  $('#infoClient').css('display','block');
  $('#zoneDemande').css('display','none');
}


// modify mainPage.html
function gotoCreateDemande() {
    $('#infoDemande').css('display', 'none');
    $('#createDemande').css('display', 'block');
}

function gotoInfoDemande(){
    $('#infoDemande').css('display', 'block');
    $('#createDemande').css('display', 'none');

}

