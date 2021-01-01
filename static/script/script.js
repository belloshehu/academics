
document.addEventListener('DOMContentLoaded', function(){
     
    document.querySelector('.searchbutton').onclick=function(){
        var url = document.querySelector('#locations').value;
        //searchalocation(url);
        
            //sendRequest(url);
       
       
    };  
  document.querySelector('#locations').onclick=function(){
      var location =this.value;
      try{
          sendRequest(location);
      }
      catch(exception){
          alert('Request failed!');
      }
  };
});
function searchalocation(){
   try{
       sendRequest(url)
   }
   catch(exception){
       alert('Request failed');
   }
}
function sendRequest(url){
//url ="locaton/"+url;
 var ajaxrequest =new XMLHttpRequest();
 ajaxrequest.onreadystatechange=onloadresult;
 ajaxrequest.open('GET',`/${url}`);
 ajaxrequest.send(null);
}

function onloadresult(){
    if(ajaxrequest.readyState==4 && ajaxrequest.status==200){
        //var location=document.querySelector('#locatioon').value;
         document.querySelector('#mosques').innerHTML=ajaxrequest.responseText;
    
    }
    else{
        document.querySelector('#mosques').innerHTML='No mosques in the selected locations. Please make a valid choice';
    }
}
