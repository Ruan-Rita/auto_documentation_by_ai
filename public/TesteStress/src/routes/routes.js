const axios = require('axios')
const { tryCatch } = require("../utils/tryCatch");
const LogService = require('../service/LogService');
var fs = require('fs');
var path = require('path');
const crypto = require('crypto');

exports.routes = (app) => {
    // Test rota sem file
    app.get('/send-request', tryCatch(async (req, res, next) => {
        const { request, endPoint } = req.body;

        const quantityRequest = request;
        const header = {
            headers: {
                'Accept': '*/*',
                'Content-Type': 'application/json',
            }
        }

        for (let i = 0; i < quantityRequest; i++) {
            await axios.get(endPoint, header);
        }
        res.status(200).send({
            message: 'Dispatched ' + quantityRequest + ' requests',
        });
    }));

    /**
     * Test rota com file
     */
    app.post('/send-file', tryCatch(async (request, response) => {
        const { requestQTD, endPoint, authorization } = request.body;
        const fileBuffer = fs.createReadStream(path.join('./uploads', 'fake-pdf.pdf'));

        const quantityRequest = requestQTD || 2;
        const header = {
            headers: {
                'Accept': '*/*',
                'Content-Type': 'multipart/form-data',
                'Authorization': authorization
            }
        }

        for (let i = 0; i < quantityRequest; i++) {
            await postInvoiceAxios(endPoint, fileBuffer, header);
        }

        return response.status(200).send({
            message: 'Dispatched ' + quantityRequest + ' upload files',
        });
    }));
}

async function postInvoiceAxios(endPoint, fileBuffer, header) {
    const result = await axios.post(endPoint, { file: fileBuffer }, header).catch(error => {
        const { method, url, timeout } = error.config;

        if (error.response) {
            new LogService().error({ header: error.response.headers, body: error.response.data, config: { method, url, timeout } });
        } else if (error.request) {
            new LogService().error({ request: error.request, config: { method, url, timeout } });
        } else {
            new LogService().error({ message: error.message, config: { method, url, timeout } });
        }

        return 'error';
    });

    return result || 'error';
}
