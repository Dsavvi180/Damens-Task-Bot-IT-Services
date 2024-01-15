const { execSync } = require("child_process");
const fs = require("fs");

execSync("python3 /Users/damensavvasavvi/Desktop/Task-Bot/textParser.ipynb");
const finalObjectID = fs.readFileSync("ObjectIDFinal.txt", "utf-8");
console.log(finalObjectID);
