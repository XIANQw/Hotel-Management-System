$(function(){
   $("#ModeLogin").click(ModeSignIn);
   $("#ModeSignUp").click(ModeSignUp);
})


function ModeSignIn(){
  $('#zoneLogin').css('display','block');
  $('#zoneSignUp').css('display','none');

}


function ModeSignUp(){
  $('#zoneSignUp').css('display','block');
  $('#zoneLogin').css('display','none');
}