$(document).ready(
     function(){
     console.log("Ready!");
     var day_night = new Date().getHours();
     console.log(day_night);
     if (day_night > 12 && day_night <= 18) {
       /*$('.advance-link>img')*/
        
        $(".portrait").each(function(){
             console.log($(this).attr("href"));
             var img =$(this).find("img").attr("src");
             var partyimg = img.replace(".jpg","_party.jpg");
             console.log(partyimg, checkFileExist(partyimg));
             $(this).find("img").attr('src',partyimg);
             
        });
          
     }else{
     $(".portrait_image>img").attr('src','/images/member.jpg');
     }
          
     
      
});


function checkFileExist(urlToFile) {
    var xhr = new XMLHttpRequest();
    xhr.open('HEAD', urlToFile, false);
    xhr.send();
     
    if (xhr.status == "404") {
        return false;
    } else {
        return true;
    }
}
