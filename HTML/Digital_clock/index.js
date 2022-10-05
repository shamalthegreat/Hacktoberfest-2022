function setDate(){
     date = new Date();
     var h = date.getHours();//h from 0-23
     var m = date.getMinutes()//m from 0-59
     var s = date.getSeconds();//s from 0-59
     var timeperiod = "AM";
     

     if(h == 0){
         h = 12;
     }

     else if(h > 12){
         h = h-12;
         timeperiod = "PM";
     }

     h = (h < 10) ? "0"+h : h;//ternary condition for h less hean 10 then 0h is printed and if it is more than 10 h is printed
     m = (m < 10) ? "0"+m : m;//ternary condition for m less hean 10 then 0m is printed and if it is more than 10 m is printed
     s = (s < 10) ? "0"+s : s;//ternary condition for s less hean 10 then 0s is printed and if it is more than 10 s is printed

      var time = h + ":" + m + ":" + s + " " + timeperiod;

      document.getElementById("MyClockDisplay").innerText = time;
      document.getElementById("MyClockDisplay").textContent = time;

      setTimeout(setDate, 1000);

}
setDate();