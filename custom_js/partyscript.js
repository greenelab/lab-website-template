$(document).ready(
     function(){
          console.log("Ready!");
          var today = new Date();
          var month = today.getMonth()
          var day = today.getDay()
          var partydates = JSON.parse(party);
          for(var i = 0; i < partydates.length; i++) {
               var obj = partydates[i];
               console.log(obj.month, obj.day);
          }
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
