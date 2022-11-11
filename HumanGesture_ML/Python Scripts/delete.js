const fs = require("fs");

let paths = "C:/Users/glakkava/Documents/ASU/CS535/AssignmentGestureDetection/HumanGesture/HumanGesture/public/Gautham_L_Recordings/";
fs.readdir(paths, function(err, files){

    files.forEach(function (file) {
      if (fs.existsSync(paths+file+"/data.csv")) {
        fs.unlinkSync(paths+file+"/data.csv")
}
        
    });

});
