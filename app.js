const express = require('express')
const fileupload = require('express-fileupload')
const path = require('path');
var http = require('http')
var pyshell = require('python-shell');

// const spawn = require('child_process').spawn
// const process = spawn('python',["./verify.py"])

var bodyParser = require('body-parser')

const app = express()
app.set('view engine','ejs')
app.use(fileupload())

app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

app.get("/",async(req,res,next)=>{
  res.status(200)
  res.render("index")
})


app.post("/upload",async(req,res,next)=>{

try {

        const file = req.files.mFile
        const videotype = req.body.filename
        //console.log(videotype);
        const timeunique = new Date().getTime().toString()
        const filename = "Gautham.mp4";
        const savepath = path.join(__dirname,"public","uploads","GESTURE_PRACTICE_"+videotype+"_"+timeunique+"_"+filename)
        console.log(savepath);
        await file.mv(savepath)
        //await pyscripts();



        res.send({
          success:true,
          message:"File uploaded"
        });

        try {
          pyshell.PythonShell.run('./verify.py',null ,function (err,results) {
            if (err) throw err;
            console.log( results);
            console.log("\n");
            console.log( results[0]);
            console.log("\n");
            console.log(results[1]);
            console.log("\n");
            console.log(results[2]);
            console.log("\n");
            console.log(results[3]);
            console.log("\n");
            console.log( results[4]);
            console.log("\n");
          });

        } catch (e) {
          console.log("YAHOO");
          console.log(e);
        }

        //const spawn = require('child_process').spawn
        //const process = spawn('python',["./verify.py"])
        res.redirect('/')

} catch (e) {
  console.log(e);
}

})




app.listen(8080||process.env.IP||'192.168.0.220'||'192.168.0.171'|| '192.168.130.243'||'192.168.0.95' ||process.env.OPENSHIFT_NODEJS_IP||'192.168.1.4',()=>{
  console.log("Server started and listening on port 8080")
})
