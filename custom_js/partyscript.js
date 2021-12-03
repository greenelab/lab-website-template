$(document).ready(
     function(){
          console.log("Ready!");
          var day_night = new Date().getHours();
          console.log(day_night);
          if (day_night > 12 && day_night <= 23) {

               $(".portrait").each(function(){
                    var img =$(this).find("img").attr("src");
                    var partyimg = img.replace(".jpg","_party.jpg");
                    if (checkFileExist(partyimg)){
                         $(this).find("img").attr('src',partyimg);
                    }

             
               });
          
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
