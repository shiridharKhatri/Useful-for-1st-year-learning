let time = 5000;
setInterval(()=>{
   time = time/1000 -1
},1000)

if(time <=0){
    console.log(time+"Finished")
}else{
    console.log(time)
}
