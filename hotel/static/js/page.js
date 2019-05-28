$(function(){
   $("#ModeLogin").click(ModeSignIn);
   $("#ModeSignUp").click(ModeSignUp);
   $('#ModeCreation').click(gotoCreationRessource);
   $('#quitCreation').click(quitCreationRessource);
   $('#id_chambre1').click(gotoCreationCh);
   $('#id_SDC1').click(gotoCreationSDC);
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
  $('#infoRessource').css('display','none');
}
function quitCreationRessource() {
  $('#createRessource').css('display','none');
  $('#infoRessource').css('display','block');
}

function gotoCreationSDC() {
    var i = this.id.charAt(this.id.length - 1);
    $('#optionCh'+i).css('display','none');
    $('#optionSDC'+i).css('display','block');
}

function gotoCreationCh() {
    var i = this.id.charAt(this.id.length - 1);
    $('#optionCh'+i).css('display','block');
    $('#optionSDC'+i).css('display','none');
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
    if(nbPlan <= 5){
        var inputDemande = $('#inputDemande');
        inputDemande.children().remove();
        var i = 1;
        while(i <= nbPlan){
            var checkin = '<div class="form-group"><label>Check in date</label><input type="date" name="checkin'+ i + '" class="form-control" required placeholder="checkin date"/></div>';
            var checkout = '<div class="form-group"><label>Check out date</label><input type="date" name="checkout'+ i + '" class="form-control" required placeholder="checkout date"/></div>';
            var nbP = '<div class="form-group"><label>Nombre des personnes</label><input type="nummber" name="nb'+ i + '" class="form-control" required placeholder="nombre des personnes"/></div>';
            var type = '<div class="form-group"><label>Type: </label><input name="type'+ i + '"id="id_chambre'+i+'" value="Chambre" type="radio"  checked>Chambre ' +
                '<input name="type' + i + '"id="id_SDC'+i+'" value="SalleDeConference" type="radio" />Salle de conference</div>';

            var optionCh = '<div id="optionCh'+i+'"><div class="form-group">\n' +
                '<label>Niveau: </label>\n' +
                '<select name="niveau'+i+'" class="form-control" placeholder="type de ressource" required>\n' +
                '<option value="Standard">Standard</option>\n' +
                '<option value="Premium">Premium</option>\n' +
                '<option value="President">President</option>\n' +
                '</select>\n' +
                '</div><div class="form-group">\n' +
                '<label>Fumeurs: </label>\n' +
                '<select name="fumeur'+i+'" class="form-control" placeholder="type de ressource" required>\n' +
                '<option value="Fumeur">Oui</option>\n' +
                '<option value="Non Fumeur">Non</option>\n' +
                '</select></div></div>';

            var ens = '<div id="plan'+i+'"><h3>Plan'+ i + '</h3></div>';
            var $ens = $(ens);
            $ens.append($(checkin));
            $ens.append($(checkout));
            $ens.append($(nbP));
            $ens.append($(type));
            $ens.append($(optionCh));
            inputDemande.append($ens);
            var id = '#id_chambre'+i;
            $(id).click(gotoCreationCh);
            id = '#id_SDC'+i;
            $(id).click(gotoCreationSDC);
            i = i + 1;
        }
    }
}