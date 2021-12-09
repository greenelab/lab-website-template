var partydates = '["1-12","18-10","9-12"]';
$(document).ready(
     function(){
          console.log("Ready!",partydates);
          var today = new Date();
          var month = today.getMonth()+1;
          var day = today.getDate();
          var md = day+"-"+month;
          console.log(md);
          var day_night = 13;
          if (partydates.includes(md)){

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
