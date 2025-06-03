const express = require("express")
const bodyParser = require('body-parser')
const { errorHandler } = require("./errorHandling")
const { routes } = require("./routes/routes")
const fileUpload = require("express-fileupload")

const app = express()


// app.use(express.urlencoded({ extended: false }));
app.use(bodyParser.json())
// Note that this option available for versions 1.0.0 and newer.
// app.use(fileUpload({
//     useTempFiles : true,
//     tempFileDir : '/tmp/'
// }));
routes(app)

app.use(errorHandler)
app.listen(3333, () => {
    console.log('SERVER STARTING ON PORT 4500');
})