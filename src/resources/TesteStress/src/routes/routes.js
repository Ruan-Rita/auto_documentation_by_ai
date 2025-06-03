const axios = require('axios')
const { tryCatch } = require("../utils/tryCatch");
const LogService = require('../service/LogService');
var fs = require('fs');
var path = require('path');
const crypto = require('crypto');

// Armazena métricas em memória
const metrics = [];

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

        let success = 0;
        let errors = 0;

        for (let i = 0; i < quantityRequest; i++) {
            try {
                await axios.get(endPoint, header);
                success++;
            } catch (e) {
                errors++;
            }
        }

        const id = generateId();
        metrics.push({
            id,
            type: 'send-request',
            quantity: quantityRequest,
            success,
            errors,
            timestamp: new Date()
        });

        res.status(200).send({
            message: 'Dispatched ' + quantityRequest + ' requests',
            metric_id: id
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

        let success = 0;
        let errors = 0;
        let message = [];

        for (let i = 0; i < quantityRequest; i++) {
            const result = await postInvoiceAxios(endPoint, fileBuffer, header);
            const msg404 = 'Não encontrou nenhuma mensagem para essa requisição';

            if (result !== 'error') {
                success++;
                message.push(result.data ? result.data.message : msg404);
            } else {
                errors++;
                message.push('error');
            }

            new LogService().logg({ data: result.data ? result.data.message : msg404 });
        }

        const id = generateId();
        metrics.push({
            id,
            type: 'send-file',
            quantity: quantityRequest,
            success,
            errors,
            timestamp: new Date()
        });

        return response.status(200).send({
            message: 'Dispatched ' + quantityRequest + ' upload files',
            outro: message,
            metric_id: id
        });
    }));

    // Rota para consultar métricas
    app.get('/metrics/:id', (req, res) => {
        const { id } = req.params;
        const metric = metrics.find(m => m.id === id);

        if (!metric) {
            return res.status(404).send({ message: 'Metric not found' });
        }

        return res.status(200).send(metric);
    });
}

// Função auxiliar pra gerar ID único
function generateId() {
    return crypto.randomBytes(8).toString('hex');
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
