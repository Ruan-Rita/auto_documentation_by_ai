const fs = require('fs')
const path = require('path');
const { formatDate } = require('../utils/date');

class LogService {
    constructor() {
        this.directory = './src/logs/';
        this.loggFile = 'nodejs.log';
        this.errorFile = 'error.log';

        if (!fs.existsSync(this.directory)) {
            fs.mkdirSync(this.directory);
        }
    }
    logg(fileContent) {
        const filePath = path.join(this.directory, this.loggFile);
        this.addContent(filePath, `${formatDate(new Date())}: ${JSON.stringify(fileContent)}`)
    }
    error(fileContent) {
        const filePath = path.join(this.directory, this.errorFile);
        this.addContent(filePath, `${formatDate(new Date())}: ${JSON.stringify(fileContent)}`)
    }
    addContent(filePath, fileContent) {
        fs.appendFile(filePath, fileContent+'\n', bigError => {
            if (bigError)
                console.log('ErrorLogFile: ' + bigError)
        })
    }
}

module.exports = LogService;