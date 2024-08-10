function fetchdata(url){
    return new Promise(function(reslove, reject){
        console.log("Starting fetching from ",url );
        setTimeout(function process(){
            let data ="dummy data";
            console.log("completed fetching the data")
            reslove(data)

        },4000)
        
    });
}

function fetch(url){
    return new Promise(function (resolve,reject){
        for(let i=0; i<100000;i++){
            console.log("hello")
        }
        console.log("completed")
        resolve("harsh")

    })
}