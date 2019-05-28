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
   $('#subNbPlan').click(addNbPlanForm);
});


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

function addNbPlanForm(){
    nbPlan = $('#nbPlan').val();
    var inputDemande = $('#inputDemande');
    inputDemande.children().remove();
    var i = 1;
    while(i <= nbPlan){
        var formGroup1 = '<div class="form-group"><label>Check in date</label><input type="date" name="checkin'+ i + '" class="form-control" required placeholder="checkin date"/></div>';
        var formGroup2 = '<div class="form-group"><label>Check out date</label><input type="date" name="checkout'+ i + '" class="form-control" required placeholder="checkout date"/></div>';
        var formGroup3 = '<div class="form-group"><label>Nombre des personnes</label><input type="nummber" name="nb'+ i + '" class="form-control" required placeholder="nombre des personnes"/></div>';
        var ens = '<div id="plan'+i+'"><h3>Plan'+ i + '</h3></div>';
        var $ens = $(ens);
        $ens.append($(formGroup1));
        $ens.append($(formGroup2));
        $ens.append($(formGroup3));
        inputDemande.append($ens);
        i = i + 1;
    }
}